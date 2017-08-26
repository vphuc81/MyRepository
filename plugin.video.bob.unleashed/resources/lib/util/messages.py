# -*- coding: utf-8 -*-

"""
    messages.py ---
    Copyright (C) 2017, Midraal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import xbmcaddon
import random


def get_link_message():
    """
    helper function to get a random message when selecting links
    """
    import random
    messages = [
        {'HD': 'If Available',
         'SD': 'Most Likely Works'
         },
        {'HD': 'Bob\'s Ya Uncle',
         'SD': 'Bob\'s NOT Ya Cousin'
         },
        {'HD': 'Checking Top Sites',
         'SD': 'Sitting In Cinema Recording'
         },
        {'HD': 'This quality is being looked for by top men, who? Top....Men!',
         'SD': 'This quality is sold on the corner by a shady guy'
         },
        {'HD': 'Google Fiber',
         'SD': 'Waiting For Dialup Connection'
         },
        {'HD': 'Great! Worth the wait',
         'SD': 'Good Enough. I just want to watch'
         },
        {'HD': 'BluRay Quality',
         'SD': 'VHS Quality'
         },
        {'HD': 'Tsingtao ',
         'SD': 'Budweiser'
         },
        {'HD': 'I must see this film in the highest quality',
         'SD': 'Flick probably sucks so lets just get it over'
         },
        {'HD': 'Looks like a Maserati',
         'SD': ' Looks like a Ford Focus'
         },
        {'HD': 'Supermodel Quality',
         'SD': ' Looks like Grandma Thelma'
         },
        {'HD': 'ARB',
         'SD': 'ARD'
         },
        {'HD': 'Merc the pinnacle of brilliance',
         'SD': 'The john harrison of quality'
         },
    ]

    if xbmcaddon.Addon().getSetting('enable_offensive') == 'true':
        messages.extend([
            {'HD': 'Kicks Ass!!',
             'SD': 'Gets ass kicked repeatedly'
             },
            {'HD': 'Fucking Rocks!!',
             'SD': 'Fucking Sucks!!'
             },
            {'HD': 'Big Bodacious Breasts',
             'SD': 'Saggy Milk Teats',
             },
        ])

    if xbmcaddon.Addon().getSetting('disable_messages') == 'true':
        message = {
            'HD': 'If Available',
            'SD': ''
        }
    else:
        message = random.choice(messages)
    return message


def get_searching_message(preset):
    """
    helper function to select a message for video items
    Args:
        preset: search quality preset ("HD", "SD" or None)
    Returns:
        random message for video items
    """
    if xbmcaddon.Addon().getSetting('disable_messages') == "true":
        return ' '
    messages = [
        '',
        'Bob\'s just nipping to blockbusters won\'t be but a sec',
        'Bob fell asleep during this flick',
        'Bob\'s movie collection has no limits',
        'Searching the Internet for your selection',
        'Bob has seen your taste in movies and is very disappointed ',
        'Bob thinks he\'s got that DVD laying around here',
        'Bob says you\'re a movie geek just like him',
        'Bob says get off of twitter and enjoy his addon',
        'Bob is a wanted man in 125 countries',
        'Bob said your taste in films is top notch',
        'When Bob chooses a movie, servers shake in fear',
        'They fear Bob. Don\'t listen to haters',
        'Bob said he works so hard for YOU, the end user',
        'Bob does this cause he loves it, not for greed',
        'That\'s not Bobs butt crack, it\'s his remote holder',
        'Bob...I Am Your Father!!',
        'I\'m going to make Bob an offer he can\'t refuse.',
        'Here\'s looking at you, Bob',
        'Go ahead, make Bob\'s day.',
        'May the Bob be with you',
        'You talking to Bob??',
        'I love the smell of Bob in the morning',
        'Bob, phone home',
        'Made it Bob! Top of the World!',
        'Bob, James Bob',
        'There\'s no place like Bob',
        'You had me at "Bob"',
        "YOU CAN\'T HANDLE THE BOB",
        'Round up all the usual Bobs',
        'I\'ll have what Bob\'s having',
        'You\'re gonna need a bigger Bob',
        'Bob\'ll be back',
        'If you build it. Bob will come',
        'We\'ll always have Bob',
        'Bob, we have a problem',
        'Say "hello" to my little Bob',
        'Bob, you\'re trying to seduce me. Aren\'t you?',
        'Elementary, my dear Bob',
        'Get your stinking paws off me, you damned dirty Bob',
        'Here\'s Bob!',
        'Hasta la vista, Bob.',
        'Soylent Green is Bob!',
        'Open the pod bay doors, BOB.',
        'Yo, Bob!',
        'Oh, no, it wasn\'t the airplanes. It was Beauty killed the Bob.',
        'A Bob. Shaken, not stirred.',
        'Who\'s on Bob.',
        'I feel the need - the need for Bob!',
        'Nobody puts Bob in a corner.',
        'I\'ll get you, my pretty, and your little Bob, too!',
        'I\'m Bob of the world!',
        'Shan of Bob',
        'Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb, Bøb',
        'We can rebuild Bob, we have the technology',
    ]

    if xbmcaddon.Addon().getSetting('enable_offensive') == "true":
        messages.extend([
            'Fuck Shit Wank -- Costa',
            'Frankly my dear, I don\'t give a Bob',
            'Beast Build Detected, Installing dangerous pyo file'
        ])

    if preset == "search":
        messages.extend([
            'Bob is popping in Blu Ray Disc'
        ])
    elif preset == "searchsd":
        messages.extend([
            'Bob rummaging through his vhs collection',
        ])

    return random.choice(messages)
