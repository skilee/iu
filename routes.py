from flask import Flask, render_template,request,url_for
import subprocess

app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/url',methods=["POST"])
def pUrl():
	url = request.form['url']
	cmd = "youtube-dl --id "+url
	process = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE)

	# wait for the process to terminate
	out, err = process.communicate()
	errcode = process.returncode
	return out
	#--id option saves file as unique id of youtube video

if __name__ == '__main__':
  app.run(debug=True)