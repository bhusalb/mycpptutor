from invoke import run, task
from termcolor import colored

@task
def hello():
    print(colored("hey", "green"))

