#! /bin/bash

function create(){
    cd
    python path-to/create.py $1 $2 $3
    cd /home/michal/Dev/$1/$2/
    git init
    git remote add origin https://github.com/Raviraven/$1-$2.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
}