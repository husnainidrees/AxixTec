

# hum ny audio data postman  k through krna ha 

# yhe speech recognition k sath ho ga


from flask import Flask, request,jsonify

import speech_recognition as sr

# yeh library ha speech recogintion 

app = Flask(__name__)


@app.route('/convert_text1',methods=['POST'])

def convert_image():

    data = request.files['audio2']

    if data.filename.endswith('wav'):

        
        # Initialize recognizer
        # yeh recoginze kry ga audio k
        
        recognizer = sr.Recognizer()
        
        # Use the audio file for recognition
        with sr.AudioFile(data) as source:

            # yeh cheez hum ny is liye k ha jo data hamry pas ha 
            # hum k handle kr saky source k through

            audio_data = recognizer.record(source) 

            # ab us k hum ny text mein covert b krna ha 
            # hum google ka speech recgintion use kr rhy ha 
            text = recognizer.recognize_google(audio_data)

            # x=list(audio_data)
        
   
        return  {"text": text} ,200
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