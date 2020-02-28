schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'require': ['result'],
    'additionalProperties': False,
    'properties': {
        'result': {
            'type': 'object',
            'required': ['token', 'id'],
            'properties': {
                'type': 'object',
                'token': {  'type': 'string'  },
                'id': {  'type': 'integer'  },
                'roles'
                'additionalProperties': False,
            },


            'roles':
                ['Access-To-The-Functions-Of-Video-Analytics',
                 'ChangePassword',
                 'Personal-Settings',
                 'ROLE_ABM_ADMIN',
                 'ROLE_MAIN_OPERATOR',
                 'See-Cameras',
                 'See-Cameras-Video',
                 'SeeArchiveVideo']
            },
    },
    'done': True
}
