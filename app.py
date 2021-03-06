from flask import Flask, render_template, request, redirect

import Caption_it
#------------------------
from gtts import gTTS
import os
#--------------

app = Flask(__name__)

@app.route('/')
def hello():

	return render_template("index.html")

@app.route('/', methods=['POST'])
def marks():
	if request.method == 'POST':

		f = request.files['userfile']
		
		path = "./static/{}".format(f.filename)
		
		f.save(path)

		caption = Caption_it.caption_this_image(path)

		speech = "I think it's" + caption

		language = 'en'

		output = gTTS(text=speech, lang=language, slow=False)
		output.save(path+".mp3")


		result_dic = {
		'image' : path,
		'caption' : caption,
		'speech' : output,
		'location' : path
		}
		return render_template("index.html", your_result = result_dic)



if __name__ == '__main__':
	app.run(debug=True)