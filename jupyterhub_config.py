c = get_config()

# c.JupyterHub.port = 443
# c.JupyterHub.ssl_cert = '/opt/mambaforge/etc/jupyter/star_tlu_edu.pem'
# c.JupyterHub.ssl_key = '/opt/mambaforge/etc/jupyter/star_tlu_edu.key'

# consider LocalAzureAdOAuthenticator instead which may allow the creation of user accounts on the system
# from oauthenticator.azuread import AzureAdOAuthenticator
# c.JupyterHub.authenticator_class = AzureAdOAuthenticator

c.Application.log_level = 'DEBUG'

# import os
# c.AzureAdOAuthenticator.tenant_id = os.environ.get('AAD_TENANT_ID')

# c.AzureAdOAuthenticator.oauth_callback_url = 'https://jupyter.tlu.edu/hub/oauth_callback'
# c.AzureAdOAuthenticator.client_id = ''
# c.AzureAdOAuthenticator.client_secret = ''
# c.AzureAdOAuthenticator.username_claim = 'upn'

# This may allow the system to create users automatically at login
# see https://jupyterhub.readthedocs.io/en/stable/tutorial/getting-started/authenticators-users-basics.html
# c.LocalAuthenticator.create_system_users = True

c.Authenticator.whitelist = [
    'cberggren@tlu.edu',
    'tsauncy@tlu.edu',
    'grader-coursePHYS371',
    'grader-coursePHYS241L',
    'rspence@tlu.edu',
]

c.Authenticator.admin_users = [
    'azureuser',
    'rspence@tlu.edu',
    'cberggren@tlu.edu',
    'tsauncy@tlu.edu'
]

c.JupyterHub.load_groups = {
    'formgrade-coursePHYS371': {
        'users': [
            'cberggren@tlu.edu',
            'grader-coursePHYS371'
        ]
    },
    'formgrade-coursePHYS241L': {
        'users': [
            'tsauncy@tlu.edu',
            'grader-coursePHYS241L'
        ]
    },
    'nbgrader-coursePHYS371': {},
    'nbgrader-coursePHYS241L': {}
}

c.JupyterHub.services = [
    {
        'name': 'coursePHYS371',
        'url': 'http://127.0.0.1:9999',
        'command': [
            'jupyterhub-singleuser',
            '--group=formgrade-coursePHYS371',
            '--debug'
        ],
        'user': 'grader-coursePHYS371',
        'cwd': '/home/grader-coursePHYS371',
        'api_token': ''
    },
    {
        'name': 'coursePHYS241L',
        'url': 'http://127.0.0.1:9998',
        'command': [
            'jupyterhub-singleuser',
            '--group=formgrade-coursePHYS241L',
            '--debug'
        ],
        'user': 'grader-coursePHYS241L',
        'cwd': '/home/grader-coursePHYS241L',
        'api_token': ''
    }
]
