

# yeh wala code theek ho ga 



from flask import Flask, request,jsonify

# yeh library ha base64 jo convert krti ha 
import base64

app = Flask(__name__)


@app.route('/convert',methods=['POST'])

def convert_image():

    data = request.files['imag']

    if data.filename.endswith('jpg'):
        
        img_data=data.read()

        base64_co=base64.b64encode(img_data).decode()
        
        # print(base64_co)
        
        # return {'base64': base64_co}, 200
        return base64_co,200
    else:
        return "Invalid file format ", 400









if __name__=='__main__':
    app.run(debug=True,port=8332)








































# @app.route('/upload-image', methods=['POST'])
# def upload_image():
 
#     file = request.files['file']

#     if file.filename == '':
#         return "No selected file", 400

#     # Check if the uploaded file is an image
#     if file and (file.filename.endswith('.png') or file.filename.endswith('.jpg') or file.filename.endswith('.jpeg')):
#         # Read the image file and convert it to Base64
#         image_data = file.read()
#         base64_encoded = base64.b64encode(image_data).decode('utf-8')

#         return {'base64': base64_encoded}, 200
#     else:
#         return "Invalid file format. Please upload a PNG or JPEG image.", 400

# if __name__ == '__main__':
#     app.run(debug=True)