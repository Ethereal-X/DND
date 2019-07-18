from app import app
from flask import render_template, request
from app.models import model, formopener, Boss
global character
global health

@app.route('/')

def index():
    return render_template('index.html')

# @app.route('/showchar', methods=['GET','POST'])
# def showchar():
#     userdata = request.form.to_dict()
#     print(userdata)
#     character = userdata["character"]
#     character = model.makechar(character)
#     return render_template('showchar.html',userdata=userdata, character = character)

@app.route('/Boss', methods=['GET','POST'])
def boss():
    userdata = request.form.to_dict()
    stats, character,health,strength = model.makechar(userdata["character"])
    outcome = Boss.Fight(health, strength, character,stats)
    return render_template('Boss.html',stats = stats, character = character, health = health, strength= strength, outcome = outcome)
    
    
    