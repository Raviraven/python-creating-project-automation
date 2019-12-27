# Project automation

1. python needs to be installed 
2. install requirements.txt by command 
                                                           
       pip install -r requirements.txt

3. Add Credentials.py file with properties:

       path=""
       username=""
       password=""
      
   filled with your data
   
4. Change paths in batch commands
5. Add add_batch_command to system environment variables as create 
6. Add remove_batch_command to system environment variables as remove 
7. create usage, type: 

       "%create%" folder/language-name project/project-name private-repository:bool

8. remove usage, type: 

       "%remove%" folder/language-name project/project-name
