from nbgrader.auth import JupyterHubAuthPlugin
c = get_config()
c.Exchange.path_includes_course = True
c.Authenticator.plugin_class = JupyterHubAuthPlugin
c.NbGrader.logfile = "/usr/local/share/jupyter/nbgrader.log"
c.NbGrader.log_level = 'DEBUG'
