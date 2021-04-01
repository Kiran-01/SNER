from flask import Flask,url_for,render_template,request
import spacy
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
# def extract():
#     if request.method == 'POST':
#         choice = request.form['taskoption']
#         rawtext = request.form['rawtext']
#         try:
#             data = wikipedia.summary(rawtext)
#         except wikipedia.DisambiguationError as e:
#             text = random.choice(e.options)
#             data = wikipedia.summary(text, sentences)
#         doc = nlp(txt)
#         result = displacy.render(docx, style='ent', jupyter=True)
#     return render_template('result.html', txt=txt, result=result)

def extract():
    if request.method == 'POST':
        raw_text = request.form['rawtext']
        try:
            data = wikipedia.summary(raw_text)
        except wikipedia.DisambiguationError as e:
            text = random.choice(e.options)
            data = wikipedia.summary(text)
            doc = nlp(txt)
            html = displacy.render(doc, style="ent")
            html = html.replace("\n\n", "\n")
            result = HTML_WRAPPER.format(html)

    return render_template('result.html', rawtext=data, result=result)

		
		
# 		docx = nlp(raw_text)
# 		html = displacy.render(doc,style="ent")
# 		html = html.replace("\n\n","\n")
# 		result = HTML_WRAPPER.format(html)

# 	return render_template('result.html',rawtext=raw_text,result=result)


@app.route('/previewer')
def previewer():
	return render_template('previewer.html')

@app.route('/preview',methods=["GET","POST"])
def preview():
	if request.method == 'POST':
		newtext = request.form['newtext']
		result = newtext

	return render_template('preview.html',newtext=newtext,result=result)


if __name__ == '__main__':
	app.run(debug=True)
