from lpgit import * 
from env import token
import os
path = 'mysite'
print('---',ls_list(path))
git = GitAccount(token.token)
git.initialize(path=path, project_name='newsample')
git.push_dir(path=path, repo='jithinj-lp/newsample')

