


# Yeh Wala Audio ka Jo Code ha Hum k Data Extract kr k Dy Rha ha 




from flask import Flask, request, jsonify


import speech_recognition as sr

app = Flask(__name__)

# @app.route('/audio', methods=['POST'])


@app.post('/audio')
def audio_to_text():


        audio_file = request.files['audio']

        #intialized the recogitor
        if audio_file.filename.endswith('.wav'):

            recognizer = sr.Recognizer()
    
       
        # Audio ko SpeechRecognition ke format mein convert karo
            audio = sr.AudioFile(audio_file)


        # jo hamary pas yeh 3 lines ha yeh main kam krti ha k convert krny k liye
            with audio as source:


                audio_data = recognizer.record(source)
        
        # Speech ko text mein convert 
        
                text = recognizer.recognize_google(audio_data)

                print("You GotIT to Acieve the data! ", text)
            return jsonify({'text': text}), 200
        

        else:
             print("Please provide the .wav this format file ")






        return "Invalid Format ", 201

 

    

if __name__ == '__main__':

    app.run(debug=True,port=8332)