

# hum ny audio data postman  k through krna ha 




from flask import Flask, request,jsonify

# yeh library ha speech recogintion 

app = Flask(__name__)


@app.route('/convert_text',methods=['POST'])

def convert_image():

    data = request.files['audio']

    if data.filename.endswith('mp3'):
        
        audio_data=data.read()

        return audio_data ,200
    else:
        return "Invalid file format ", 400





if __name__=='__main__':
    app.run(debug=True,port=8332)









# from flask import Flask ,request

# app= Flask(__name__)



# @app.route('/audio',methods=['POST'])

# def audio_file():

#     try:

#         if request.method=='POST':
#             audio=request.files['audio']
#             audio_name=audio.filename

        
#             if audio.save(audio_name):

#                 return {"response":"file saved successfully in your current durectory"}
#             else:
        
#                 return {"error":"select you wave file"}
#     except Exception as e:
     
#      return {"error":str(e)}






# if __name__=='__main__':
#     app.run(debug=True,port=8333)