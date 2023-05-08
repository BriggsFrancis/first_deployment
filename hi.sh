#!/bin/bash
function act(){
    echo "===============$1================="
}


act "Making Migrations"
python3 manage.py makemigrations 

act "Migrating"
python3 manage.py migrate 

act "Runserver"
python3 manage.py runserver 



