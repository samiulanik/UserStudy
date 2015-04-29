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


@app.route('/time_demo')
def time_demo():
    return render_template('time-demo.html')

@app.route('/time_watch')
def time_watch():
    return render_template('time-watch.html')

@app.route('/time_task_1')
def time_task_1():
    return render_template('time-task-1.html')


@app.route('/time_task_2')
def time_task_2():
    return render_template('time-task-2.html')


@app.route('/time_task_3')
def time_task_3():
    return render_template('time-task-3.html')


@app.route('/baseline_demo')
def baseline_demo():
    return render_template('baseline-demo.html')

@app.route('/baseline_watch')
def baseline_watch():
    return render_template('baseline-watch.html')

@app.route('/baseline_task_1')
def baseline_task_1():
    return render_template('baseline-task-1.html')

@app.route('/baseline_task_2')
def baseline_task_2():
    return render_template('baseline-task-2.html')

@app.route('/baseline_task_3')
def baseline_task_3():
    return render_template('baseline-task-3.html')



@app.route('/saveLog', methods=['POST'])
def saveLog():
    print"working!!";
    content = request.json    
    #print(content.get('time'))
    outfile = open('data.txt', 'a')
    json.dump(content,outfile)
    outfile.write('\n')
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
