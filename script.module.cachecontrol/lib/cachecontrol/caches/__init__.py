from .file_cache import FileCache  # noqa
from .redis_cache import RedisCache  # noqa
try:
    from .hay_cache import HayCache  # noqa
except ImportError:
    pass
