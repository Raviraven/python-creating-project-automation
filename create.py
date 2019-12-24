import sys
import os
#from github import Github
from selenium import webdriver
import Credentials

browser = webdriver.Chrome()
browser.get('http://github.com/login')

def create():
    browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(Credentials.username)
    browser.find_elements_by_xpath("//*[@id='password']")[0].send_keys(Credentials.password)
    browser.find_element_by_xpath("//*[@id='login']/form/div[3]/input[8]").click()


# def create_using_github_package():
#     project_folder_type = str(sys.argv[1])
#     folder_name = str(sys.argv[2])
#     os.makedirs(Credentials.path + project_folder_type + "/" + folder_name)
#     user = Github(Credentials.username, Credentials.password).get_user()
#     repo = user.create_repo(folder_name)
#     print("Repository {0} created successfully".format(folder_name))


if __name__ == "__main__":
    create()
