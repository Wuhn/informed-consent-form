from flask import Flask, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)
app.config.from_object(__name__)

##################################################################
#		WEBEND
##################################################################

@app.route('/')
@app.route('/index', methods = ['POST','GET'])
def index(name=None):
    return render_template('study_informed_consent_1.html', name=name, data={})

@app.route('/next')
def informed_consent_2(name=None):
    return render_template('study_informed_consent_2.html', name=name, data={})

@app.route('/agree')
def give_consent(name=None):
    return index()
    
@app.route('/disagree')
def reject_consent(name=None):
    flash('No worries; we have deleted your participation key. If you reconsider your participation please register anew.')
    return index()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)





