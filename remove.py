from github import Github
import Credentials
import sys
import os
import shutil
import stat


def remove():
    project_language = str(sys.argv[1])
    project_name = str(sys.argv[2])
    remove_repo_directory(project_language=project_language, project_name=project_name)
    remove_repository(project_language=project_language, project_name=project_name)


def remove_repo_directory(project_language, project_name):
    try:
        directory = "{0}\\{1}\\{2}".format(Credentials.path, project_language, project_name)
        shutil.rmtree(path=directory, onerror=remove_readonly)
        #os.removedirs(directory)
        print("Directory {0} deleted".format(directory))
    except Exception as error:
        print("Error occured during deleting directory: {0}".format(error))


def remove_repository(project_language, project_name):
    try:
        repo_name = "{0}/{1}-{2}".format(Credentials.username, project_language, project_name)
        repo = Github(login_or_token=Credentials.git_token).get_repo(repo_name)
        repo.delete()
        print("Repository {0}-{1} deleted successfully".format(project_language, project_name))
    except Exception as error:
        print("Error occured during deleting repository: {0}".format(error))


def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


if __name__ == "__main__":
    remove()
