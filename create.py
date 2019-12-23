import sys
import os
from github import Github

path = ""
username = ""
password = ""


def create():
    folder_name = str(sys.argv[1])
    os.makedirs(path + folder_name)
    user = Github(username, password).get_user()
    repo = user.create_repo(folder_name)
    print("Repository {0} created successfully".format(folder_name))


if __name__ == "__main__":
    create()