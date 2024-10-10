



# yeh code pdf ka data la kr dy ga hum k
from flask import Flask, request
import docx

app = Flask(__name__)

@app.route('/upload_word', methods=['POST'])

def upload_file():


    file = request.files['file']


    if file and file.filename.endswith('.docx'):
        
        # Word file ko read karen python-docx ka istemal karte hue

        doc = docx.Document(file)
        text = ""

        # Paragraph ke text ko print krway gy yeh 

        for paragraph in doc.paragraphs:
            text += paragraph.text   

        return text, 200
    else:
        return "Invalid file format. Please upload a Word document (DOCX).", 400

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True,port=8332)















