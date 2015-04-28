import os
from flask import Flask,render_template, request,json
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/video')
def video():
    #print "loading html";
    return render_template('categorization-task-1.html')


@app.route('/saveLog', methods=['POST'])
def saveLog():
    print"working!!";
    content = request.json    
    print(content)
    obj = open('data.txt', 'wb')
    json.dump(content,obj)
    
if __name__=="__main__":
    app.run()
