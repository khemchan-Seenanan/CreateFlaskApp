def init_code(name):
    initcode = f'''
from flask import Flask
{name} = Flask(__name__)

from {name} import views '''
    
    return initcode

def index_code():
    indexcode = '''
{% extends 'public/base_templates/public_base.html' %}
{% block content %}
    <h1 class='container mt-5'> First Flask Application!!!!</h1>
{% endblock content %}
    '''
    return indexcode

def views_code(name):
    viewscode = f''' 
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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Flask App</title>
    <link rel="stylesheet" href=" {{ url_for('static', filename='css/style.css') }} ">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Flask App</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="/">Home</a>
            </li>
          </ul>
        </div>
      </nav>
    
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
