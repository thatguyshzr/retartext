from flask import Flask, request, render_template
from retartext import *

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
	get_text=''
	if request.method == 'POST':
		get_text = request.form.get('msg')
		get_text = add_emoji(get_text)

	return render_template('index.html', retard_text= get_text)

if __name__ == '__main__':
 	app.run(debug= True)