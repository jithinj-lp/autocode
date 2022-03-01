from github import Github
import os


class GitAccount:
    '''This class creates a git account intance
    Make sure that git token is not exposed in github'''
    def __init__(self, token:str=None) -> None:
        try:
            print('connecting to git server')
            self.g = Github(token)
            self.user = self.g.get_user()
            self.repos = list(self.user.get_repos())
            print('connection successfull')
        except Exception as e:
            print(e)
            self.__del__()

    def __str__(self) -> str:
        return self.user.name
    
    def push_dir(self,repo:str,  path:str,branch:str='main', message:str='New commit') -> None:
        rep = self.g.get_repo(repo)
        print('getting files ready for updating...')
        ls = self.__ls_list(path)       
        for i in ls:
            try:
                print('uploading', i, end='  ')
                with open(i) as f:
                    content = open(i, 'rb').read()
                    try:rep.create_file(i, message, content ,branch=branch)
                    except:
                        contents = rep.get_contents(i)
                        rep.update_file(contents.path, message, content,contents.sha ,branch=branch)
                print('100%')
            except Exception as e:
                print('Error uploading', i,'\n', e)

    def initialize(self,path:str, project_name:str,branches=['main', 'develop'], private=True, gitignore_template:str='Python'):
        # try:
            try:
                self.user.create_repo(project_name, gitignore_template=gitignore_template, private=private)
                repo = self.g.get_repo('jithinj-lp/'+project_name)
            except:
                repo = self.g.get_repo('jithinj-lp/'+project_name)
            print(repo)
            sb = repo.get_branch('main')
            for i in branches:
                try:
                    repo.create_git_ref(ref='refs/heads/' + i, sha=sb.commit.sha)
                except Exception as e:
                    print(e)

    def __ls_list(self,dirName, out=True):
        listOfFile = os.listdir(dirName)
        result = []
        allFiles = list()
        for entry in listOfFile:
            fullPath = os.path.join(dirName, entry)
            if os.path.isdir(fullPath):
                allFiles = allFiles + self.__ls_list(fullPath)
            else:
                allFiles.append(fullPath)  
        for i in allFiles:
            result.append(i.replace(f'\\', f'/')) 
        if out:
            for i in result:
                print('>',i)          
        return result

def ls_list(dirName):
    listOfFile = os.listdir(dirName)
    result = []
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + ls_list(fullPath)
        else:
            allFiles.append(fullPath)  
    for i in allFiles:
        result.append(i.replace(f'\\', f'/'))           
    return result


# source_branch = 'master'
# target_branch = 'newfeature'

# repo = g.get_user().get_repo(repoName)
# sb = repo.get_branch(source_branch)
# repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)