from flask import Flask,url_for,render_template,request
import spacy
import wikipedia
from spacy import displacy
# # import en_core_web_sm
# nlp = spacy.load('en_core_web_sm')

from spacy.lang.en import English
# from flaskext.markdown import Markdown
nlp = spacy.load("en_core_web_sm")
import random

import json

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)


# def analyze_text(text):
# 	return nlp(text)

@app.route('/')
def index():
	# raw_text = "Bill Gates is An American Computer Scientist since 1986"
	# docx = nlp(raw_text)
	# html = displacy.render(docx,style="ent")
	# html = html.replace("\n\n","\n")
	# result = HTML_WRAPPER.format(html)

	return render_template('index.html')


	
	
@app.route('/extract',methods=["GET","POST"])
def extract():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		txt = wikipedia.summary(raw_text)
		docx = nlp(txt)
		html = displacy.render(docx,style="ent")
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)

	return render_template('result.html',rawtext=txt,result=result)


@app.route('/previewer')
def previewer():
	return render_template('previewer.html')

@app.route('/preview',methods=["GET","POST"])
def preview():
	if request.method == 'POST':
		newtext = request.form['newtext']
		data = wikipedia.summary(newtext)
		doc = nlp(data)
		result1 = displacy.render(doc,style="ent")

	return render_template('preview.html',data=data,result1=result1)


if __name__ == '__main__':
	app.run(debug=True)
