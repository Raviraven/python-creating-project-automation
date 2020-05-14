import sys
import os
from github import Github
import Credentials


def create():
    project_language = str(sys.argv[1])
    project_name = str(sys.argv[2])
    access_mode = get_access_mode()

    create_repo_directory(project_language=project_language, project_name=project_name)
    create_repository(project_language=project_language, project_name=project_name, access_mode=access_mode)


def get_access_mode():
    try:
        access_mode = bool(sys.argv[3].capitalize())
        if not access_mode:
            raise Exception("wrong 3rd argument")
    except IndexError:
        access_mode = False
    except Exception as error:
        print("An error occured: {0}".format(error))
    return access_mode


def create_repo_directory(project_language, project_name):
    try:
        directory = get_dir_path_linux(project_language, project_name)
        os.makedirs(directory)
        print("Directory {0} created".format(directory))
    except Exception as error:
        print("Error occured during creating directory: {0}".format(error))


def create_repository(project_language, project_name, access_mode):
    try:
        user = Github(login_or_token=Credentials.git_token).get_user()
        repo = user.create_repo(name="{0}-{1}".format(project_language, project_name), private=access_mode)
        print("Repository {0}-{1} created successfully, private set to: {2}".format(project_language, project_name, access_mode))
    except Exception as error:
        print("Error occured during deleting repository: {0}".format(error))


def get_dir_path_windows(project_language, project_name):
    directory = "{0}\\{1}\\{2}".format(Credentials.path, project_language, project_name)
    return directory


def get_dir_path_linux(project_language, project_name):
    directory = "{0}/{1}/{2}".format(Credentials.path, project_language, project_name)
    return directory


if __name__ == "__main__":
    create()
