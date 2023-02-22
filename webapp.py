from flask import Flask, render_template, request 
app = Flask(__name__)

# a get request with a variable id 

@app.get('/pets/<animal_id>')
def pet(animal_id):
    return "This is a pet page"

# a starightforward get request 

@app.get('/')
def user():
    return "This is a profile page"
