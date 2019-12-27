import sys
import os
from github import Github
# from selenium import webdriver
import Credentials

#browser = webdriver.Firefox()
#browser.get('http://github.com/login')


# def create():
#     project_language = str(sys.argv[1])
#     project_name = str(sys.argv[2])
#     browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(Credentials.username)
#     browser.find_elements_by_xpath("//*[@id='password']")[0].send_keys(Credentials.password)
#     browser.find_element_by_xpath("//*[@id='login']/form/div[3]/input[8]").click()
#     browser.get('https://github.com/new')
#     browser.find_element_by_xpath("//*[@id='repository_name']").send_keys("{0}-{1}".format(project_language, project_name))
#     browser.find_element_by_xpath("//*[@id='repository_visibility_private']").click()
#     browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[3]/button").click()
#     print("Repository {0}-{1} created successfully".format(project_language, project_name))


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
        directory = "{0}\\{1}\\{2}".format(Credentials.path, project_language, project_name)
        os.makedirs(directory)
        print("Directory {0} created".format(directory))
    except Exception as error:
        print("Error occured during creating directory: {0}".format(error))


def create_repository(project_language, project_name, access_mode):
    try:
        user = Github(Credentials.username, Credentials.password).get_user()
        repo = user.create_repo(name="{0}-{1}".format(project_language, project_name), private=access_mode)
        print("Repository {0}-{1} created successfully, private set to: {2}".format(project_language, project_name, access_mode))
    except Exception as error:
        print("Error occured during deleting repository: {0}".format(error))


if __name__ == "__main__":
    create()
