from flask import Flask, render_template, request, redirect, session
                                          
app = Flask(__name__)                     
app.secret_key = 'ThisIsSecret'                                         

@app.route('/')                           
                                      
def index():
  return render_template('index.html')
@app.route('/survey', methods=['post'])
def insert_survey():
   print "Got Post Info"
   session['name'] = request.form['name']
   session['location'] = request.form['location']
   session['language'] = request.form['language']
   session['comment'] = request.form['comment']
   return redirect('/show') 
@app.route('/show')
def show_user():
  return render_template('result_page.html', name=session['name'], location=session['location'],language=session['language'], comment=session['comment'])
app.run(debug=True)                       