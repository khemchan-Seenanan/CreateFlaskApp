def init_code(name):
    initcode = f'''
from flask import Flask
{name} = Flask(__name__)

from {name} import views '''
    
    return initcode

def index_code(name):
    indexcode = f'''
<!-- Code for the index page -->
{{% extends 'public/base_templates/public_base.html' %}}
{{% block content %}}
    <h1 class='container mt-5' style="text-align:center;font-family: 'Oleo Script',cursive ;">Name of App: {name}</h1>
{{% endblock content %}}
    '''
    return indexcode

def views_code(name):
    viewscode = f''' 
#Define all your routes in this file

from {name} import {name}
from flask import render_template, redirect, request, jsonify,make_response

@{name}.route("/")
def index():
    return render_template("public/index.html")
    '''
    return viewscode

def css_code():
    csscode = '''
.container{
    width: 80%;
    margin: auto;
}
    '''
    return csscode

def js_code():
    jscode = '''
console.log("Flask Application!!!!")
    '''
    return jscode

def base_code():
    basecode = '''
<!-- Base template for all html files  -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Flask App</title>
    <link rel="stylesheet" href=" {{ url_for('static', filename='css/style.css') }} ">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Oleo+Script&display=swap" rel="stylesheet">
</head>
<body style="background-color: #32A9DE;">
    <h1 class="mt-5"  style="font-family: 'Oleo Script', cursive; text-align:center;" >Create Flask App</h1>
   
    
    {% block content %}{% endblock content %}  
    <script src="{{ url_for('static', filename='JAVASCRIPT/script.js') }} "></script>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>  
</body>
</html>
    '''
    return basecode


def run_code(name):
    runcode = f'''
#Entry point of the flask Application

from {name} import {name}

if __name__ == "__main__":
    {name}.run()
    
    '''
    return runcode

