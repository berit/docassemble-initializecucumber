from docassemble.base.util import DAOAuth, interview_url
import oauth2client.client
import re

__all__ = ['GitHubAuth']

class GitHubAuth(DAOAuth):
    def init(self, *pargs, **kwargs):
        super().init(*pargs, **kwargs)
        self.appname = 'mygithub'
        self.token_uri = "https://github.com/login/oauth/access_token"
        self.auth_uri = "https://github.com/login/oauth/authorize"
        self.scope = "repo"
        
    def test(self):
        return "test"
    
    def _get_flow(self):
        app_credentials = {
          'id': 'b087d29cfdb4655001af',
          'secret': '08568657a317587127db6609b439bfee3cdca931'
        }
        client_id = app_credentials.get('id', None)
        client_secret = app_credentials.get('secret', None)
        if client_id is None or client_secret is None:
            raise Exception('The application ' + self.appname + " is not configured in the Configuration")
        flow = oauth2client.client.OAuth2WebServerFlow(
            client_id=client_id,
            client_secret=client_secret,
            scope=self.scope,
            redirect_uri=re.sub(r'\?.*', '', interview_url()),
            auth_uri=self.auth_uri,
            token_uri=self.token_uri,
            access_type='offline',
            prompt='consent')
        return flow
