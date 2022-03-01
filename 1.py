from lpgit import * 
from env import token
import os
path = 'mysite'
git = GitAccount(token.token)
# git.push_dir(path=path, repo='jithinj-lp/newrepo')
git.initialize(path=path, repo='jithinj-lp/newrepo')

# print(ls_list(path))