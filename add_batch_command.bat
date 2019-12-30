@echo off
:create
cd
py create.py %1 %2
cd /d D:/Dokumenty/Projekty/%1/%2
git init
git remote add origin https://github.com/Raviraven/%1-%2.git
type nul > README.md
git add .
git commit -m "Initial commit"
git push -u origin master
exit /B 0