import os
from flask import Flask,render_template, request,json
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/categorization_task_1')
def categorization_task_1():
    return render_template('categorization-task-1.html')


@app.route('/categorization_task_2')
def categorization_task_2():
    return render_template('categorization-task-2.html')

@app.route('/categorization_task_3')
def categorization_task_3():
    return render_template('categorization-task-3.html')

@app.route('/categorization_demo')
def categorization_demo():
    return render_template('categorization-demo.html')

@app.route('/categorization_watch')
def categorization_watch():
    return render_template('categorization-watch.html')


@app.route('/saveLog', methods=['POST'])
def saveLog():
    print"working!!";
    content = request.json    
    #print(content.get('time'))
    outfile = open('data.txt', 'a')
    json.dump(content,outfile)
    outfile.write('\n')
    
if __name__=="__main__":
    app.run()
