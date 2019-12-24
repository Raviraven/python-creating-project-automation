@echo off
:create
cd
py create.py %1 %2
cd E:/Dokumenty/Projekty/%1/%2
git init
git remote add origin git@github.com:Raviraven/%2.git
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin master
exit /B 0