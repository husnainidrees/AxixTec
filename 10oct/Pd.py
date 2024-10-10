

# yeh code pdf ka data la kr dy ga hum k
# Bilkul Perfect Code ha yeh 

from flask import Flask, request
import PyPDF2


app=Flask(__name__)

@app.route('/pdf_upload',methods=['POST'])

def check_pdf():
    
    data=request.files['file']

    if data.filename.endswith('.pdf'):

        reader=PyPDF2.PdfReader(data)

        text=""
        for page in reader.pages:

            text=text+page.extract_text()
            print(text)

        return text,200
    else:
        return "Invalid file format "





if __name__ == '__main__':
    app.run(debug=True,port=8332)




















    
    #     for page in reader.pages:
    #         text += page.extract_text()

    #     return text, 200
    # else:
    #     return "Invalid file format. Please upload a PDF.", 400
