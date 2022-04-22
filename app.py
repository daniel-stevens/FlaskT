#Import Flask
from flask import Flask, render_template, url_for

#__name__ Refers to the namespace this is running in.
#App.py directly so namespace is __name__ - if we import this to be used elsewhere it will take on the name of the file, eg in this case is app.py
app = Flask(__name__)

#Route - a command to run a funtion which returns response to user
#This is a decorator, what one looks like
#Decorator - A function which wraps around another funtion and lets us do things with them.
#This decorator will call our root app - So index funtion
@app.route('/')
#Just our home page
def index():
    return render_template('index.html')

@app.route('/pet')
#Pet page
def pet():
    return render_template('pet.html')

@app.route('/add-pet')
#Pet page
def add_pet():
    return render_template('addpet.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')