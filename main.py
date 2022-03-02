from lpgit import * 
from env import token
import os
path = 'mysite'
ls_list(path)
git = GitAccount(token.token)
git.initialize(path=path, project_name='autocloudtest', org='LogicPlum')
# git.push_dir(path=path, project_name='autocloudtest', org='LogicPlum')