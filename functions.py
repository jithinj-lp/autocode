import requests
from pprint import pprint
import base64
from github import Github
from pprint import pprint
import json
import base64
from github import Github
from pprint import pprint

# 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
class GitAccount:
    def __init__(self, username, password:str=None, token:str=None) -> None:
        self.username = username
        url = f"https://api.github.com/users/{username}"
        user_data = requests.get(url).json()
        print(json.dumps(user_data, indent = 3, ))
        g = Github()
        self.user = g.get_user(self.username)
        if password:
            try:
                user = g.get_user(self.username, password)
            except:
                print('password or username is incorrect')
        if token:
            user = g.get_user()
        self.repos = list(self.user.get_repos())


def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-"*50)
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    try:
        # repo license
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass