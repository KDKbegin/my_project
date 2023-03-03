from flask import Flask, render_template, jsonify
#we are creating a list of dictionary of jobs,where each list item is corresponding
#to one job.
JOBS = [{
  'id': 1,
  'title': 'Software Engineer',
  'requirements': 'Frontend + backend',
  'location': 'Mumbai',
  'salary': '800000'
}, {
  'id': 2,
  'title': 'Frontend Engineer',
  'requirements': 'HTML + Javascript + CSS',
  'location': 'Pune',
  'salary': '400000'
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'requirements': 'backend, Python, Databases',
  'location': 'Banglore',
  'salary': '850000'
},
        {
  'id': 4,
  'title': 'Database Administrator',
  'requirements': 'backend, Python, Databases, MySQL ',
  'location': 'Pune',
   
}
       
       ]

#it means from flask module import flask class
#when we install the frame work diff modules get installed
#and modules have lowercase names always
app = Flask(__name__)


#to create object of the class Flask
#name refers from where the it is called
#execute only print(__name__) o/p=__main__
@app.route("/")
def hellowebpage():
  return render_template('home.html', jobs=JOBS)

  #we are passing the list as an argument.providing data to render in the template.
  #way to insert dynamic data into html/css
#this will return the data in the json format.
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if (__name__ == '__main__'):
  app.run('0.0.0.0', debug=True)
