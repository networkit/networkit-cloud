import os
pjoin = os.path.join

## Basic variables (don't change)
c.JupyterHub.admin_access = False
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.Authenticator.check_common_password = True
c.Authenticator.minimum_password_length = 10
c.JupyterHub.cleanup_proxy = False
c.JupyterHub.cleanup_servers = False
c.JupyterHub.cookie_secret_file = pjoin('/persistent/', 'cookie_secret')
c.JupyterHub.db_url = pjoin('/persistent/', 'jupyterhub.sqlite')
c.JupyterHub.hub_ip = ''
c.JupyterHub.spawner_class = 'kubespawner.KubeSpawner'
c.KubeSpawner.cmd = ['start-notebook.sh']
c.KubeSpawner.image_pull_policy = 'Always'
c.KubeSpawner.start_timeout = 60 * 5
c.Spawner.cpu_guarantee = 2.0
c.Spawner.cpu_limit = 10.0

## Custom variables (change)

# Enter the same path as <URL-SUBPATH>
c.JupyterHub.base_url = ''

# Change <URL-SUBPATH> to the non-domain part of the URL of the service. E.g. https://www.my-data-service.com/this-is-the-subpath/
c.KubeSpawner.environment = {'JUPYTERHUB_API_URL': 'http://jhub-service:8081/<URL-SUBPATH>/hub/api'}

# Set here a possible admin user. In combination with nativeauthenticator this 
# user can register directly and hereby setup the password for the admin-account.
# After that the admin is used to manage and authorize normal users. 
# For details: https://github.com/jupyterhub/nativeauthenticator
c.Authenticator.admin_users = {'<ADMIN-USER>'}

# Optional: Change this to any other container based on Jupyter base variants
c.KubeSpawner.image = 'fabratu/networkit-cloud:latest'

# Optional: Change this to open a default notebook on launching
c.KubeSpawner.default_url = '/lab/tree' # EDIT THIS TO OPEN DEFAULT NOTEBOOK 

# Optional: KubeSpawner.image_pull_secrets only needs to be set, if the image is on a private registry
# For details: https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets
c.KubeSpawner.image_pull_secrets = ['<NAME-OF-SECRET>']

# Optional: Minimum number of bytes a single-user notebook server is guaranteed to have. Change if needed.
c.Spawner.mem_guarantee = '4G'

# Optional: Maximum number of bytes a single-user notebook server is allowed to use. Change if needed.
c.Spawner.mem_limit = '16G'