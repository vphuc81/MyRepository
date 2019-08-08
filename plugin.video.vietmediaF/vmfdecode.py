import binascii, hashlib,urlfetch,json,re
from array import array
from addon import alert, notify,notify1, TextBoxes, ADDON, ADDON_ID, ADDON_PROFILE, LOG, PROFILE

aes_sbox = array('B',
	'637c777bf26b6fc53001672bfed7ab76'
	'ca82c97dfa5947f0add4a2af9ca472c0'
	'b7fd9326363ff7cc34a5e5f171d83115'
	'04c723c31896059a071280e2eb27b275'
	'09832c1a1b6e5aa0523bd6b329e32f84'
	'53d100ed20fcb15b6acbbe394a4c58cf'
	'd0efaafb434d338545f9027f503c9fa8'
	'51a3408f929d38f5bcb6da2110fff3d2'
	'cd0c13ec5f974417c4a77e3d645d1973'
	'60814fdc222a908846eeb814de5e0bdb'
	'e0323a0a4906245cc2d3ac629195e479'
	'e7c8376d8dd54ea96c56f4ea657aae08'
	'ba78252e1ca6b4c6e8dd741f4bbd8b8a'
	'703eb5664803f60e613557b986c11d9e'
	'e1f8981169d98e949b1e87e9ce5528df'
	'8ca1890dbfe6426841992d0fb054bb16'.decode('hex')
)

aes_inv_sbox = array('B',
	'52096ad53036a538bf40a39e81f3d7fb'
	'7ce339829b2fff87348e4344c4dee9cb'
	'547b9432a6c2233dee4c950b42fac34e'
	'082ea16628d924b2765ba2496d8bd125'
	'72f8f66486689816d4a45ccc5d65b692'
	'6c704850fdedb9da5e154657a78d9d84'
	'90d8ab008cbcd30af7e45805b8b34506'
	'd02c1e8fca3f0f02c1afbd0301138a6b'
	'3a9111414f67dcea97f2cfcef0b4e673'
	'96ac7422e7ad3585e2f937e81c75df6e'
	'47f11a711d29c5896fb7620eaa18be1b'
	'fc563e4bc6d279209adbc0fe78cd5af4'
	'1fdda8338807c731b11210592780ec5f'
	'60517fa919b54a0d2de57a9f93c99cef'
	'a0e03b4dae2af5b0c8ebbb3c83539961'
	'172b047eba77d626e169146355210c7d'.decode('hex')
)

aes_Rcon = array('B',
	'8d01020408102040801b366cd8ab4d9a'
	'2f5ebc63c697356ad4b37dfaefc59139'
	'72e4d3bd61c29f254a943366cc831d3a'
	'74e8cb8d01020408102040801b366cd8'
	'ab4d9a2f5ebc63c697356ad4b37dfaef'
	'c5913972e4d3bd61c29f254a943366cc'
	'831d3a74e8cb8d01020408102040801b'
	'366cd8ab4d9a2f5ebc63c697356ad4b3'
	'7dfaefc5913972e4d3bd61c29f254a94'
	'3366cc831d3a74e8cb8d010204081020'
	'40801b366cd8ab4d9a2f5ebc63c69735'
	'6ad4b37dfaefc5913972e4d3bd61c29f'
	'254a943366cc831d3a74e8cb8d010204'
	'08102040801b366cd8ab4d9a2f5ebc63'
	'c697356ad4b37dfaefc5913972e4d3bd'
	'61c29f254a943366cc831d3a74e8cb'.decode('hex')
)

def galois_multiply(a, b):
	p = 0
	while b:
		if b & 1:
			p ^= a
		a <<= 1
		if a & 0x100:
			a ^= 0x1b
		b >>= 1

	return p & 0xff

gf_mul_by_9  = array('B', [galois_multiply(x,  9) for x in range(256)])
gf_mul_by_11 = array('B', [galois_multiply(x, 11) for x in range(256)])
gf_mul_by_13 = array('B', [galois_multiply(x, 13) for x in range(256)])
gf_mul_by_14 = array('B', [galois_multiply(x, 14) for x in range(256)])

class AES(object):
	block_size = 16

	def __init__(self, key):
		self.setkey(key)

	def setkey(self, key):
		self.key = key
		self.key_size = len(key)

		if self.key_size == 16:
			self.rounds = 10
		elif self.key_size == 24:
			self.rounds = 12
		elif self.key_size == 32:
			self.rounds = 14
		else:
			raise ValueError, "Key length must be 16, 24 or 32 bytes"

		self.expand_key()

	def expand_key(self):
		exkey = array('B', self.key)

		if self.key_size == 16:
			extra_cnt = 0
		elif self.key_size == 24:
			extra_cnt = 2
		else:
			extra_cnt = 3

		word = exkey[-4:]
        
		for i in xrange(1, 11):
			word = word[1:4] + word[0:1]

			for j in xrange(4):
				word[j] = aes_sbox[word[j]]

			word[0] = word[0] ^ aes_Rcon[i]

			for z in xrange(4):
				for j in xrange(4):
					word[j] ^= exkey[-self.key_size + j]
				exkey.extend(word)

			if len(exkey) >= (self.rounds+1) * self.block_size:
				break

			if self.key_size == 32:
				for j in xrange(4):
					word[j] = aes_sbox[word[j]] ^ exkey[-self.key_size + j]
				exkey.extend(word)

			for z in xrange(extra_cnt):
				for j in xrange(4):
					word[j] ^= exkey[-self.key_size + j]
				exkey.extend(word)

		self.exkey = exkey

	def add_round_key(self, block, round):
		offset = round * 16
		exkey = self.exkey

		for i in xrange(16):
			block[i] ^= exkey[offset + i]

	def sub_bytes(self, block, sbox):
		for i in xrange(16):
			block[i] = sbox[block[i]]

	def shift_rows_inv(self, b):
		b[ 5], b[ 9], b[13], b[ 1] = b[1], b[5], b[ 9], b[13]
		b[10], b[14], b[ 2], b[ 6] = b[2], b[6], b[10], b[14]
		b[15], b[ 3], b[ 7], b[11] = b[3], b[7], b[11], b[15]

	def mix_columns_inv(self, block):
		mul_9  = gf_mul_by_9
		mul_11 = gf_mul_by_11
		mul_13 = gf_mul_by_13
		mul_14 = gf_mul_by_14

		for i in xrange(4):
			col = i * 4

			v0, v1, v2, v3 = (block[col], block[col + 1], block[col + 2], block[col + 3])
			block[col  ] = mul_14[v0] ^ mul_9[v3] ^ mul_13[v2] ^ mul_11[v1]
			block[col+1] = mul_14[v1] ^ mul_9[v0] ^ mul_13[v3] ^ mul_11[v2]
			block[col+2] = mul_14[v2] ^ mul_9[v1] ^ mul_13[v0] ^ mul_11[v3]
			block[col+3] = mul_14[v3] ^ mul_9[v2] ^ mul_13[v1] ^ mul_11[v0]

	def decrypt_block(self, block):
		self.add_round_key(block, self.rounds)

		for round in xrange(self.rounds-1, 0, -1):
			self.shift_rows_inv(block)
			self.sub_bytes(block, aes_inv_sbox)
			self.add_round_key(block, round)
			self.mix_columns_inv(block)

		self.shift_rows_inv(block)
		self.sub_bytes(block, aes_inv_sbox)
		self.add_round_key(block, 0)

class CBCMode(object):
	def __init__(self, cipher, IV):
		self.cipher = cipher
		self.block_size = cipher.block_size
		self.IV = array('B', IV)

	def decrypt(self, data):
		block_size = self.block_size
		if len(data) % block_size != 0:
			raise ValueError, "Ciphertext length must be multiple of 16"

		data = array('B', data)
		IV = self.IV

		for offset in xrange(0, len(data), block_size):
			ctext = data[offset : offset+block_size]
			block = ctext[:]
			self.cipher.decrypt_block(block)

			for i in xrange(block_size):
				block[i] ^= IV[i]
			data[offset : offset+block_size] = block

			IV = ctext

		self.IV = IV
		return data.tostring()

def evpKDF(passwd, salt, key_size=8, iv_size=4, iterations=1, hash_algorithm="md5"):
	target_key_size = key_size + iv_size
	block = ""
	derived_bytes = ""
	number_of_derived_words = 0
	while number_of_derived_words < target_key_size:
		block = hashlib.md5(block+passwd+salt).digest()
		derived_bytes += block[0: min(len(block), (target_key_size - number_of_derived_words) * 4)]
		number_of_derived_words += len(block)/4

	return {
		"key": derived_bytes[0: key_size * 4],
		"iv": derived_bytes[key_size * 4:]
	}

def decode(ciphertext,passphrase,salt):
	ciphertext=ciphertext.decode('base64')
	data = evpKDF(passphrase, salt)
	decryptor = CBCMode(AES(data['key']), data['iv'])
	text = decryptor.decrypt(ciphertext)
	l = len(text) - int(binascii.hexlify(text[-1]), 16)
	return text[:l]
def XvaYOy8Z4Djz(t):
	return t.decode('base64')
def gibberishAES(string, key=''):
	import ctypes
	def aa(l,s=4):
		a=[]
		for i in range(0,len(l),s):a.append((l[i:i+s]))
		return a

	def j2p(v):return ctypes.c_int(v).value
	def rshift(val, n): return (val % 0x100000000) >> n

	e = 14
	r = 8
	n = False
		
	def f(e):
		#try:result=urllib.quote(e)
		#except:result=str(e)
		return str(e)
		
	def c(e):
		#try:result=urllib.quote(e, safe='~()*!.\'')
		#except:result=str(e)
		return str(e)

	def t(e):
		f = [0]*len(e)
		if 16 >len(e):
			r = 16 - len(e)
			f = [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r]
		for n in range(len(e)):f[n] = e[n]
		return f

	def o(e):
		n = ""
		for r in len(e):n += ("0" if 16 > e[r] else "") + format(e[r], 'x')
		return n

	def u(e, r):
		c = []
		if not r:e=f(e)
		for n in range(len(e)):c.append(ord(e[n]))
		return c

	def i(n):
		if n==128:e = 10; r = 4
		elif n==192:e = 12;r = 6
		elif n==256:e = 14;r = 8

	def b(e):
		n = []
		for r in range(e):n.append(256)
		return n

	def h(n, f):
		d=[];t= 3 if e >= 12 else 2; i = n + f; d.append(L(i));u=[c for c in d[0]]
		for c in range(1,t):d.append(L(d[c - 1] + i));u+=d[c]
		return {'key': u[0 : 4 * r],'iv': u[4 * r : 4 * r + 16]}

	def a1(e, r=False):
		c = ""
		if (r):
			n = e[15]
			#if n > 16:print "Decryption error: Maybe bad key"
			if 16 != n:
				for f in range(16 - n):c += chr(e[f])
		else:
			for f in range(16):c += chr(e[f])
		return c

	def a(e, r=False):
		if not r:c=''.join(chr(e[f])for f in range(16))
		elif 16!=e[15]:c=''.join(chr(e[f]) for f in range(16-e[15]))
		else:c=''
		return c

	def v(e, r, n, f=''):
		r = S(r); o = len(e) / 16; u = [0]*o
		d=[e[16 * t: 16 * (t + 1)] for t in range(o)]
		for t in range(len(d) - 1,-1,-1):
			u[t] = p(d[t], r)
			u[t] = x(u[t], n) if 0 == t else x(u[t], d[t - 1])
		
		i=''.join(a(u[t]) for t in range(o-1))
		i += a(u[o-1], True)
		return i if f else c(i)

	def s(r, f):
		n = False
		t = M(r, f, 0)
		for c in (1, e + 1 ,1):
			t = g(t)
			t = y(t)
			if e > c:t = k(t)
			t = M(t, f, c)
		return t

	def p(r, f):
		n = True
		t = M(r, f, e)
		for c in range(e - 1,-1,-1):
			t = y(t,n)
			t = g(t,n)
			t = M(t, f, c)
			if c > 0 : t = k(t,n)
		return t

	def g(e,n=True):#OK
		f = D if n else B; c = [0]*16
		for r in range(16):c[r] = f[e[r]]
		return c

	def y(e,n=True):
		f = []
		if n: c = [0, 13, 10, 7, 4, 1, 14, 11, 8, 5, 2, 15, 12, 9, 6, 3] 
		else:c =[0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]
		for r in range(16):f.append(e[c[r]])
		return f

	def k(e,n=True):
		f = [0]*16
		if (n):
			for r in range(4):
				f[4 * r] = F[e[4 * r]] ^ R[e[1 + 4 * r]] ^ j[e[2 + 4 * r]] ^ z[e[3 + 4 * r]]
				f[1 + 4 * r] = z[e[4 * r]] ^ F[e[1 + 4 * r]] ^ R[e[2 + 4 * r]] ^ j[e[3 + 4 * r]]
				f[2 + 4 * r] = j[e[4 * r]] ^ z[e[1 + 4 * r]] ^ F[e[2 + 4 * r]] ^ R[e[3 + 4 * r]]
				f[3 + 4 * r] = R[e[4 * r]] ^ j[e[1 + 4 * r]] ^ z[e[2 + 4 * r]] ^ F[e[3 + 4 * r]]
		else:
			for r in range(4):
				f[4 * r] = E[e[4 * r]] ^ U[e[1 + 4 * r]] ^ e[2 + 4 * r] ^ e[3 + 4 * r]
				f[1 + 4 * r] = e[4 * r] ^ E[e[1 + 4 * r]] ^ U[e[2 + 4 * r]] ^ e[3 + 4 * r]
				f[2 + 4 * r] = e[4 * r] ^ e[1 + 4 * r] ^ E[e[2 + 4 * r]] ^ U[e[3 + 4 * r]]
				f[3 + 4 * r] = U[e[4 * r]] ^ e[1 + 4 * r] ^ e[2 + 4 * r] ^ E[e[3 + 4 * r]]
		return f	

	def M(e, r, n):#OK
		c = [0]*16
		for f in range(16):c[f] = e[f] ^ r[n][f]
		return c

	def x(e, r):
		f = [0]*16
		for n in  range(16):f[n] = e[n] ^ r[n]
		return f

	def S(n):#r=8;e=14
		o=[[n[4 * f + i] for i in range(4)] for f in range(r)]
		
		for f in range(r,4 * (e + 1)):
			d=[t for t in o[f-1]]
			if 0 == f % r:d = m(w(d)); d[0] ^= K[f / r - 1]
			elif r > 6 and 4 == f % r : d = m(d)
			o.append([o[f - r][t] ^ d[t] for t in range(4)])
		
		u = []
		for f in range(e + 1):
			u.append([])
			for a in range(4):u[f]+=o[4 * f + a]
		return u

	def m(e):
		return [B[e[r]] for r in range(4)]

	def w(e):
		e.insert(4,e[0])
		e.remove(e[4])
		return e

	def A(e, r):return [int(e[n:n+r], 16) for n in range(0,len(e),r)]

	def C(e):
		n=[0]*len(e)
		for r in range(len(e)):n[e[r]] = r
		return n

	def I(e, r):
		f=0
		for n in range(8):
			f = f ^ e if 1 == (1 & r) else f
			e = j2p(283 ^ e << 1) if e > 127 else j2p(e << 1)
			r >>= 1
		return f

	def O(e):
		n = [0]*256
		for r in range(256):n[r] = I(e, r)
		return n

	B = A("637c777bf26b6fc53001672bfed7ab76ca82c97dfa5947f0add4a2af9ca472c0b7fd9326363ff7cc34a5e5f171d8311504c723c31896059a071280e2eb27b27509832c1a1b6e5aa0523bd6b329e32f8453d100ed20fcb15b6acbbe394a4c58cfd0efaafb434d338545f9027f503c9fa851a3408f929d38f5bcb6da2110fff3d2cd0c13ec5f974417c4a77e3d645d197360814fdc222a908846eeb814de5e0bdbe0323a0a4906245cc2d3ac629195e479e7c8376d8dd54ea96c56f4ea657aae08ba78252e1ca6b4c6e8dd741f4bbd8b8a703eb5664803f60e613557b986c11d9ee1f8981169d98e949b1e87e9ce5528df8ca1890dbfe6426841992d0fb054bb16", 2)
	D = C(B)
	K = A("01020408102040801b366cd8ab4d9a2f5ebc63c697356ad4b37dfaefc591", 2)
	E = O(2)
	U = O(3)
	z = O(9)
	R = O(11)
	j = O(13)
	F = O(14)

	def G(e, r, n):
		c = b(8); t = h(u(r, n), c); a = t.key; o = t.iv; d = [83, 97, 108, 116, 101, 100, 95, 95]+c
		e = u(e, n)
		f = l(e, a, o)
		f = d+f
		return T.encode(f)

	def H(e, r, n=''):
		f = decode(e)
		c = f[8 : 16]
		t = h(u(r, n), c)
		a = t['key']
		o = t['iv']
		f = f[16 : len(f)]
		return v(f, a, o, n)

	def decode(r):#OK
		def indexOfchar(n):
			try:a=e.index(r[n])
			except:a=-1
			return a
		
		e="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
		r=r.replace('\n','');f=[];c=[0]*4
		for n in range(0,len(r),4):
			for i in range(len(c)):c[i]=indexOfchar(n+i)
			f.append(j2p(c[0]<<2|c[1]>>4))
			f.append(j2p((15&c[1])<<4|c[2]>>2))
			f.append(j2p((3&c[2])<<6|c[3]))
		return f[0:len(f)-len(f)%16]

	def L(e):
		def r(e, r):return j2p(e << r) | j2p(rshift(e, 32-r))

		def n(e, r):
			c = 2147483648 & e
			t = 2147483648 & r
			n = 1073741824 & e
			f = 1073741824 & r
			a = (1073741823 & e) + (1073741823 & r)
			i = 2147483648^a^c^t
			j = 3221225472^a^c^t
			k = 1073741824^a^c^t
			return j2p(i if n & f else ((j if 1073741824 & a else k) if n | f else a^c^t))		

		def f(e, r, n):return j2p(e & r) | j2p(~e & n)

		def c(e, r, n):return j2p(e & n) | j2p(r & ~n)

		def t(e, r, n):return e ^ r ^ n

		def a(e, r, n):return r ^ (e | ~n)

		def o(e, c, t, a, o, d, u):
			e = n(e, n(n(f(c, t, a), o), u))
			return n(r(e, d), c)

		def d(e, f, t, a, o, d, u):
			e = n(e, n(n(c(f, t, a), o), u))
			return n(r(e, d), f)

		def u(e, f, c, a, o, d, u):
				e = n(e, n(n(t(f, c, a), o), u))
				return n(r(e, d), f)

		def i(e, f, c, t, o, d, u):
			e = n(e, n(n(a(f, c, t), o), u))
			return n(r(e, d), f)

		def b(e):
			n=len(e); f = n + 8; c = (f - f % 64) / 64; t = 16 * (c + 1); a = [0]*t; o = 0
			for d in range(n):r = (d - d % 4) / 4; o = 8 * (d % 4);	a[r] = a[r] | j2p(e[d] << o)
			d+=1
			r = (d - d % 4) / 4
			o = 8 * (d % 4)
			a[r] = a[r] | j2p(128 << o)
			a[t - 2] = j2p(n << 3)
			a[t - 1] = j2p(rshift(n,29))
			return a

		def h(e):
			f = []
			for n in range(4):
				r = j2p(255 & rshift(e, 8 * n))
				f.append(r)
			return f

		m = A("67452301efcdab8998badcfe10325476d76aa478e8c7b756242070dbc1bdceeef57c0faf4787c62aa8304613fd469501698098d88b44f7afffff5bb1895cd7be6b901122fd987193a679438e49b40821f61e2562c040b340265e5a51e9b6c7aad62f105d02441453d8a1e681e7d3fbc821e1cde6c33707d6f4d50d87455a14eda9e3e905fcefa3f8676f02d98d2a4c8afffa39428771f6816d9d6122fde5380ca4beea444bdecfa9f6bb4b60bebfbc70289b7ec6eaa127fad4ef308504881d05d9d4d039e6db99e51fa27cf8c4ac5665f4292244432aff97ab9423a7fc93a039655b59c38f0ccc92ffeff47d85845dd16fa87e4ffe2ce6e0a30143144e0811a1f7537e82bd3af2352ad7d2bbeb86d391", 8)
		S = [];  S = b(e); y = m[0]; k = m[1]; M = m[2]; x = m[3]; l = 0
		for l in range(0,len(S),16):
			v = y
			s = k
			p = M
			g = x
			y = o(y, k, M, x, S[l + 0], 7, m[4])
			x = o(x, y, k, M, S[l + 1], 12, m[5])
			M = o(M, x, y, k, S[l + 2], 17, m[6])
			k = o(k, M, x, y, S[l + 3], 22, m[7])
			y = o(y, k, M, x, S[l + 4], 7, m[8])
			x = o(x, y, k, M, S[l + 5], 12, m[9])
			M = o(M, x, y, k, S[l + 6], 17, m[10])
			k = o(k, M, x, y, S[l + 7], 22, m[11])
			y = o(y, k, M, x, S[l + 8], 7, m[12])
			x = o(x, y, k, M, S[l + 9], 12, m[13])
			M = o(M, x, y, k, S[l + 10], 17, m[14])
			k = o(k, M, x, y, S[l + 11], 22, m[15])
			y = o(y, k, M, x, S[l + 12], 7, m[16])
			x = o(x, y, k, M, S[l + 13], 12, m[17])
			M = o(M, x, y, k, S[l + 14], 17, m[18])
			k = o(k, M, x, y, S[l + 15], 22, m[19])
			y = d(y, k, M, x, S[l + 1], 5, m[20])
			x = d(x, y, k, M, S[l + 6], 9, m[21])
			M = d(M, x, y, k, S[l + 11], 14, m[22])
			k = d(k, M, x, y, S[l + 0], 20, m[23])
			y = d(y, k, M, x, S[l + 5], 5, m[24])
			x = d(x, y, k, M, S[l + 10], 9, m[25])
			M = d(M, x, y, k, S[l + 15], 14, m[26])
			k = d(k, M, x, y, S[l + 4], 20, m[27])
			y = d(y, k, M, x, S[l + 9], 5, m[28])
			x = d(x, y, k, M, S[l + 14], 9, m[29])
			M = d(M, x, y, k, S[l + 3], 14, m[30])
			k = d(k, M, x, y, S[l + 8], 20, m[31])
			y = d(y, k, M, x, S[l + 13], 5, m[32])
			x = d(x, y, k, M, S[l + 2], 9, m[33])
			M = d(M, x, y, k, S[l + 7], 14, m[34])
			k = d(k, M, x, y, S[l + 12], 20, m[35])
			y = u(y, k, M, x, S[l + 5], 4, m[36])
			x = u(x, y, k, M, S[l + 8], 11, m[37])
			M = u(M, x, y, k, S[l + 11], 16, m[38])
			k = u(k, M, x, y, S[l + 14], 23, m[39])
			y = u(y, k, M, x, S[l + 1], 4, m[40])
			x = u(x, y, k, M, S[l + 4], 11, m[41])
			M = u(M, x, y, k, S[l + 7], 16, m[42])
			k = u(k, M, x, y, S[l + 10], 23, m[43])
			y = u(y, k, M, x, S[l + 13], 4, m[44])
			x = u(x, y, k, M, S[l + 0], 11, m[45])
			M = u(M, x, y, k, S[l + 3], 16, m[46])
			k = u(k, M, x, y, S[l + 6], 23, m[47])
			y = u(y, k, M, x, S[l + 9], 4, m[48])
			x = u(x, y, k, M, S[l + 12], 11, m[49])
			M = u(M, x, y, k, S[l + 15], 16, m[50])
			k = u(k, M, x, y, S[l + 2], 23, m[51])
			y = i(y, k, M, x, S[l + 0], 6, m[52])
			x = i(x, y, k, M, S[l + 7], 10, m[53])
			M = i(M, x, y, k, S[l + 14], 15, m[54])
			k = i(k, M, x, y, S[l + 5], 21, m[55])
			y = i(y, k, M, x, S[l + 12], 6, m[56])
			x = i(x, y, k, M, S[l + 3], 10, m[57])
			M = i(M, x, y, k, S[l + 10], 15, m[58])
			k = i(k, M, x, y, S[l + 1], 21, m[59])
			y = i(y, k, M, x, S[l + 8], 6, m[60])
			x = i(x, y, k, M, S[l + 15], 10, m[61])
			M = i(M, x, y, k, S[l + 6], 15, m[62])
			k = i(k, M, x, y, S[l + 13], 21, m[63])
			y = i(y, k, M, x, S[l + 4], 6, m[64])
			x = i(x, y, k, M, S[l + 11], 10, m[65])
			M = i(M, x, y, k, S[l + 2], 15, m[66])
			k = i(k, M, x, y, S[l + 9], 21, m[67])
			y = n(y, v)
			k = n(k, s)
			M = n(M, p)
			x = n(x, g)
		return h(y)+h(k)+h(M)+h(x)

		
	def recode(b):
		def getcode(s):
			w, i, s, e=s.split(',')
			a=b=c=0;d=[];f=[]
			while True:
				if a < 5:f.append(w[a])
				elif a < len(w):d.append(w[a])
				a+=1
				
				if  b < 5 :f.append(i[b])
				elif  b < len(i):d.append(i[b])
				b+=1
				
				if  c < 5:f.append(s[c])
				elif  c < len(s):d.append(s[c])
				c+=1
				
				if len(w) + len(i) + len(s) + len(e) == len(d) + len(f) + len(e):break

			k=''.join(s for s in d);m=''.join(s for s in f);b=0;o=[]
			for a in range(0,len(d),2):
				n = -1
				if ord(m[b]) % 2:n = 1
				o.append(chr(int(k[a:a+2], 36) - n))
				b+=1
				if b >= len(f):b = 0
			return ''.join(s for s in o)
		l=0
		while l<5 or 'decodeLink' not in b:
			try:b=getcode(xsearch("(\w{100,},\w+,\w+,\w+)",b.replace("'",'')));l+=1
			except:break
		return b
	
	return H(string, key) if key else recode(string)
def get_fptplay(url):
	#fptplay_option = ADDON.getSetting('fptplay_option')
	
	user = ADDON.getSetting('fptplay_user')
	password = ADDON.getSetting('fptplay_pass')
	country_code = ADDON.getSetting('country_code')
	
	exec(fuck('cj11cmxmZXRjaC5nZXQoJ2h0dHBzOi8vdGV4dHVwbG9hZGVyLmNvbS9kejdweS9yYXcnKQ=='))
	headers = {
			'cookie': fuck(r.body) ,
			'origin': 'https://fptplay.vn',
			'accept-encoding': 'gzip, deflate, br',
			'x-requested-with': 'XMLHttpRequest',
			'accept-language': 'en,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6',
			'x-key': '123456',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'accept': 'application/json, text/javascript, */*; q=0.01',
			'referer': url,
			'authority': 'fptplay.vn',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		}
	if 'livetv' in url:
		match = re.search(r"livetv\/(.+)",url)
		tv_id = match.group(1)
		
		data = {"id":tv_id,"type":"newchannel","quality":"3","mobile":"web"}
		
		exec(fuck('cmVzcG9uc2UgPSB1cmxmZXRjaC5wb3N0KCdodHRwczovL2ZwdHBsYXkudm4vc2hvdy9nZXRsaW5rbGl2ZXR2JywgaGVhZGVycz1oZWFkZXJzLCBkYXRhPWRhdGEp'))
		video_url=json.loads(response.body)['stream']
		
	else:
		match = re.search(r"(.{24})\.html",url)
		movie_id = match.group(1)
		if 'tap' in url:
			match = re.search(r"tap-(\d+)",url)
			episode = match.group(1)
		else: episode = '1'
		data = {"id":movie_id,"type":"newchannel","quality":"3","episode":episode,"mobile":"web"}
		exec(fuck('cmVzcG9uc2UgPSB1cmxmZXRjaC5wb3N0KCdodHRwczovL2ZwdHBsYXkudm4vc2hvdy9nZXRsaW5rJywgaGVhZGVycz1oZWFkZXJzLCBkYXRhPWRhdGEp'))
		video_url=json.loads(response.body)['stream']
		
	return video_url+"|User-Agent=vietmediaf&Origin=https%3A%2F%2Ffptplay.vn"
