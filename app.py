from flask import Flask, render_template, request
from googletrans import Translator
app = Flask(__name__)
translator = Translator()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/translate', methods=['POST'])
def translate():
    source_text = request.form['source_text']
    target_language = request.form['target_language']
    translated = translator.translate(source_text, src='en', dest=target_language)
    translated_text = translated.text
    return render_template('index.html', translated_text=translated_text)
if __name__ == '__main__':
    app.run(debug=True)
