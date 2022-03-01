from lpgit import * 
from env import token
import os
path = 'mysite'
ls_list(path)
git = GitAccount(token.token)
git.initialize(path=path, project_name='autocloudone')
git.push_dir(path=path, repo='jithinj-lp/autocloudone')
