# -*- coding: utf-8 -*-
"""

    Copyright (C) 2018-2018 plugin.video.youtube

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only for more information.
"""

from . import JSONStore


class APIKeyStore(JSONStore):
    def __init__(self):
        JSONStore.__init__(self, 'api_keys.json')

    def set_defaults(self):
        data = self.get_data()
        #if 'keys' not in data:
        if 'keys' in data:
            data = {'keys': {'personal': {'api_key': 'AIzaSyDLB3CmWGN8JjWI4SLLtGLeXFiiurWIXts', 'client_id': '8747499188-751rfl8ep7oem9fqi82i52po6u9p77fb', 'client_secret': '_Th67iEwJBsF7D4CQvIiAJa-'}, 'developer': {}}}
        if 'personal' not in data['keys']:
            data['keys']['personal'] = {'api_key': '', 'client_id': '', 'client_secret': ''}
        if 'developer' not in data['keys']:
            data['keys']['developer'] = {}
        self.save(data)
