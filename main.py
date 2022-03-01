from github import Github
from env.token import token
import os

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles  

for i in getListOfFiles('venv'):
    print(i.replace(r'\\\\', f'\\'))

g = Github(token)
u = g.get_user()
# u.create_ m,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
repo = g.get_repo('jithinj-lp/newrepo')
repo.

repo.update_file()
repo.create_git_ref()
repo.create_git_tree()
# try:
#     u.create_repo('newrepo', gitignore_template='Python', private=True)
# except Exception as e:
#     print(e)
# try:
#     repo = g.get_repo('jithinj-lp/newrepo')
#     repo.create_file('myfolder/newfiles.py', 'mymessage', 'my content', branch='main')
# except Exception as e:
#     print(e)

content = repo.get_contents('myfolder/newfiles.py')
print(content.decoded_content)

PATH = ''
