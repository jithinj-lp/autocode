from github import Github


g = Github('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')
u = g.get_user()
try:
    u.create_repo('newrepo', gitignore_template='Python', private=True)
except Exception as e:
    print(e)

