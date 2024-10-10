

# # import os
# # from flask import Flask, make_response, send_file
# # from werkzeug.utils import secure_filename

# # app = Flask(__name__)
# # PDF_FOLDER = 'Flask\10oct\test.pdf'  

# # @app.route("/pdf/<string:filename>", methods=['GET'])
# # def return_pdf(filename):
# #     try:
# #         filename = secure_filename(filename)  # Sanitize the filename
# #         file_path = os.path.join(PDF_FOLDER, filename)
# #         if os.path.isfile(file_path):
# #             return send_file(file_path, as_attachment=True)
# #         else:
# #             return make_response(f"File '{filename}' not found.", 404)
# #     except Exception as e:
# #         return make_response(f"Error: {str(e)}", 500)
    



# # if __name__=='__main__':

# #     app.run(debug=True,port=8332)









# # ik terminal mein library

# # cls 

# # method retur krny k liye jsonify,request

# from flask import Flask,jsonify,request
# import PyPDF2


# app=Flask(__name__)


# # HOme page pr kuch nai hota ha
# # decorator app ka

# # @app.route('/pdfw',methods=['POST'])

# # def post_name():
# #     data=request.get_json()
# #     res={'rec':data}
# #     file = request.files["test.pdf"]
# #     pdf_reader = PyPDF2.PdfReader(file)
# #     text = ""
# #     for page in pdf_reader.pages:
# #         text += page.extract_text()
# #     return text

# #     return jsonify(res),201



# @app.route('/api/data',methods=['GET'])
# def get_data():
#     try:
#         response = request.get("test.pdf")
#         # Raises an HTTPError if the HTTP request returned an unsuccessful status code
#         response.raise_for_status()  
#         data = response.json()


#     except request.exceptions.HTTPError as http_err:
#         return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
#     except Exception as err:
#         return jsonify({'error': f'Other error occurred: {err}'}), 500
    
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True,port=8332)






# if __name__ =="__main__":

#     # server bar bar run na krny pady
#     # host Ip

#     app.run(debug=True,port='8332')







# from flask import Flask, jsonify ,request
# import PyPDF2

# app=Flask(__name__)




# @app.route('/generate_pdf',methods=['GET'])
# def generate_pdf():

#     data=PyPDF2.PdfFileReader('test.pdf')

#     print(data.extractText())

#     return jsonify(data)


       


    





# if __name__=='__main__':

#     app.run(debug=True,port=8333)








from flask import Flask,jsonify,request
import PyPDF2
from PyPDF2 import PdfReader

app=Flask(__name__)


@app.route('/api/post_name/',methods=['POST'])

def user_info():

    data=request.get_json()
    res={'rec':data}

    user_name=data['url']
    page=user_name.pages[0]
    x= page.extract_text()

    print(x)


    return jsonify(res),201





if __name__=="__main__":

    app.run(debug=True,port='8332')





































