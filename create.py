import sys
import os
from github import Github
from selenium import webdriver
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
    os.makedirs("{0}\\{1}\\{2}".format(Credentials.path, project_language, project_name))
    user = Github(Credentials.username, Credentials.password).get_user()
    repo = user.create_repo("{0}-{1}".format(project_language, project_name))
    print("Repository {0}-{1} created successfully".format(project_language, project_name))


if __name__ == "__main__":
    create()
