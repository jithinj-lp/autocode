from functions import *

USERNAME = 'jithinj-lp'
USER_EMAIL = 'jithin.j@logicplum.com'

execute('git init')
execute('django-admin startproject mysite')
execute('git config --global user.name "%s"'%USERNAME)
execute('git config --global user.email "%s"'%USER_EMAIL)
execute('git config --global --list')

l = '''git add .
git commit -m "first commit"
git remote add origin git@github.com:jithinj-lp/newrepo.git
git push -u origin master'''.split('\n')

for i in l:
    execute(i)