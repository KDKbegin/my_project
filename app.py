from flask import Flask, render_template

#it means from flask module import flask class
#when we install the frame work diff modules get installed
#and modules have lowercase names always
app = Flask(__name__)


#to create object of the class Flask
#name refers from where the it is called
#execute only print(__name__) o/p=__main__
@app.route("/")
def hellowebpage():
  return render_template('home.html')


if (__name__ == '__main__'):
  app.run('0.0.0.0', debug=True)
