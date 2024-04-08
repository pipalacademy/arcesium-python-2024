import os

def get_config(name):
    return os.getenv("SIGMA_" + name)

PROBLEM_REPOSITORY_PATH = get_config("PROBLEM_REPOSITORY_PATH")

