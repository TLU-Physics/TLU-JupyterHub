c = get_config()

c.JupyterHub.port = 443
c.JupyterHub.ssl_cert = '/opt/mambaforge/etc/jupyter/star_tlu_edu.pem'
c.JupyterHub.ssl_key = '/opt/mambaforge/etc/jupyter/star_tlu_edu.key'

# consider LocalAzureAdOAuthenticator instead which may allow the creation of user accounts on the system
import os
from oauthenticator.azuread import LocalAzureAdOAuthenticator
c.JupyterHub.authenticator_class = LocalAzureAdOAuthenticator

c.Application.log_level = 'DEBUG'

c.LocalAzureAdOAuthenticator.tenant_id = os.environ.get('AAD_TENANT_ID')
c.LocalAzureAdOAuthenticator.oauth_callback_url = 'https://jupyter.tlu.edu/hub/oauth_callback'
c.LocalAzureAdOAuthenticator.client_id = os.environ.get('AAD_JH_CLIENT_ID')
c.LocalAzureAdOAuthenticator.client_secret = os.environ.get('AAD_JH_CLIENT_SECRET')
c.LocalAzureAdOAuthenticator.username_claim = 'upn'

# This may allow the system to create users automatically at login
# see https://jupyterhub.readthedocs.io/en/stable/tutorial/getting-started/authenticators-users-basics.html
c.LocalAuthenticator.create_system_users = True
# Someone who was working with the local version of Azure AD had the following line included. I am not sure how much of this we need, but we might need a custom add user command at least to deal with the --force-badname issue
c.LocalAzureAdOAuthenticator.add_user_cmd =  ['adduser', '--gecos', '""', '--disabled-password', '--force-badname']

# c.Authenticator.allowed_users = [
#     'rspence@tlu.edu',
#     'cberggren@tlu.edu',
#     'tsauncy@tlu.edu',
#     'grader-coursephys371',
#     'grader-coursephys241l',
#     'stud1@tlu.edu',
#     'aarcsalinas@tlu.edu',
#     'ajsilva@tlu.edu',
#     'hhernandez@tlu.edu',
#     'adrimartinez@tlu.edu',
#     'tmharrison@tlu.edu',
#     'jasacastro@tlu.edu'
# ]

c.Authenticator.admin_users = [
    'azureuser',
    'rspence@tlu.edu',
    'cberggren@tlu.edu'
]

# TODO: this format for groups is deprecated
c.JupyterHub.load_groups = {
    'instructors': [
        'cberggren@tlu.edu',
        'tsauncy@tlu.edu',
    ],
    'formgrade-coursePHYS371': [
        'cberggren@tlu.edu',
        'grader-coursephys371',
    ],
    'formgrade-coursePHYS241L': [
        'tsauncy@tlu.edu',
        'grader-coursephys241l',
    ],
    'nbgrader-coursePHYS371': [
        'cberggren@tlu.edu',
        'stud1@tlu.edu',
        'aarcsalinas@tlu.edu'
    ],
    'nbgrader-coursePHYS241L': [
        'tsauncy@tlu.edu',
        'ajsilva@tlu.edu',
        'hhernandez@tlu.edu',
        'adrimartinez@tlu.edu',
        'tmharrison@tlu.edu',
        'jasacastro@tlu.edu'
    ],
}

c.JupyterHub.load_roles = roles = [
    {
        'name': 'instructor',
        'groups': ['instructors'],
        'scopes': [
            # these are the scopes required for the admin UI
            'admin:users',
            'admin:servers',
        ],
    },
    # The class_list extension needs permission to access services
    {
        'name': 'server',
        'scopes': [
            'inherit',
            # in JupyterHub 2.4, this can be a list of permissions
            # greater than the owner and the result will be the intersection;
            # until then, 'inherit' is the only way to have variable permissions
            # for the server token by user
            # "access:services",
            # "list:services",
            # "read:services",
            # "users:activity!user",
            # "access:servers!user",
        ],
    },
]
for course in ['coursePHYS371', 'coursePHYS241L']:
    # access to formgrader
    roles.append(
        {
            'name': f'formgrade-{course.lower()}',
            'groups': [f'formgrade-{course}'],
            'scopes': [
                f'access:services!service={course}',
            ],
        }
    )
    # access to course materials
    roles.append(
        {
            'name': f'nbgrader-{course.lower()}',
            'groups': [f'nbgrader-{course}'],
            'scopes': [
                # access to the services API to discover the service(s)
                'list:services',
                f'read:services!service={course}',
            ],
        }
    )

c.JupyterHub.services = [
    {
        'name': 'coursePHYS371',
        'url': 'http://127.0.0.1:9999',
        'command': [
            'jupyterhub-singleuser',
            '--debug'
        ],
        'user': 'grader-coursephys371',
        'cwd': '/home/grader-coursephys371',
        'environment': {
            # specify lab as default landing page
            'JUPYTERHUB_DEFAULT_URL': '/lab'
        },
        'api_token': ''
    },
    {
        'name': 'coursePHYS241L',
        'url': 'http://127.0.0.1:9998',
        'command': [
            'jupyterhub-singleuser',
            '--debug'
        ],
        'user': 'grader-coursephys241l',
        'cwd': '/home/grader-coursephys241l',
        'environment': {
            # specify lab as default landing page
            'JUPYTERHUB_DEFAULT_URL': '/lab'
        },
        'api_token': ''
    }
]
