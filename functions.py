import subprocess

def execute(command:str, out=True):
    subp = subprocess.Popen(str(command), shell=True, stdout=subprocess.PIPE)
    subprocess_return = str(subp.stdout.read())
    if out:print(subprocess_return) 
    return subprocess_return