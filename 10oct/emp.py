
import json

from flask import Flask,jsonify,request

app=Flask(__name__)






# nextEmpID = len(employees) + 1  

@app.route('/api/employees',methods=['POST'])


def create_login():

    data=request.get_json()
    re={"rec":data}

    print(re)

    return jsonify(re),201



















# from flask import Flask, request
# import speech_recognition as sr

# app = Flask(__name__)

# @app.route('/upload-audio', methods=['POST'])
# def upload_audio():
    

#     file = request.files['file']

   

#         # Initialize recognizer
# #         recognizer = sr.Recognizer()
        
#         # Use the audio file for recognition
#         with sr.AudioFile(file) as source:
#             audio_data = recognizer.record(source)  # Read the audio file
#             try:
#                 # Convert audio to text
#                 text = recognizer.recognize_google(audio_data)
#                 return {'text': text}, 200
#             except sr.UnknownValueError:
#                 return "Google Speech Recognition could not understand audio", 400
#             except sr.RequestError as e:
#                 return f"Could not request results from Google Speech Recognition service; {e}", 400
#     else:
#         return "Invalid file format. Please upload a WAV or MP3 audio file.", 400

# if __name__ == '__main__':
#     app.run(debug=True)











if __name__=='__main__':

    app.run(debug=True,port=8332)













# Data wo Get kr k display kr rha ha hum ko 

# def get_employee():

#     return jsonify(employees)










# employees = [
#  { 'id': 1, 'name': 'Ashley' },
#  { 'id': 2, 'name': 'Kate' },
#  { 'id': 3, 'name': 'Joe' }
# ]



# @app.route('/employees',methods=['POST'])
# def create_employe():
#     # ik employee id global

#     global nextEmployeeId

#     employee=json.loads(request.data)

#     if employee is None:
      
#       return jsonify({'error':'This is invalid employee'}),400
    
#     employee['id']= nextEmployeeId
#     nextEmployeeId += 1
#     employees.append(employee)
    
    
#     return '', 201, { 'location': f'/employees/{employee["id"]}' }
    





# if __name__=='__main__':
  
#   app.run(debug=True,port=8332)





























# @app.route('/employees', methods=['POST'])
# def create_employee():
#  global nextEmployeeId
#  employee = json.loads(request.data)
#  if not employee_is_valid(employee):
#    return jsonify({ 'error': 'Invalid employee properties.' }), 400

#  employee['id'] = nextEmployeeId
#  nextEmployeeId += 1
#  employees.append(employee)

#  return '', 201, { 'location': f'/employees/{employee["id"]}' }

# @app.route('/employees/<int:id>', methods=['PUT'])
# def update_employee(id: int):
#  employee = get_employee(id)
#  if employee is None:
#    return jsonify({ 'error': 'Employee does not exist.' }), 404

#  updated_employee = json.loads(request.data)
#  if not employee_is_valid(updated_employee):
#    return jsonify({ 'error': 'Invalid employee properties.' }), 400

#  employee.update(updated_employee)

#  return jsonify(employee)

# @app.route('/employees/<int:id>', methods=['DELETE'])
# def delete_employee(id: int):
#  global employees
#  employee = get_employee(id)
#  if employee is None:
#    return jsonify({ 'error': 'Employee does not exist.' }), 404

#  employees = [e for e in employees if e['id'] != id]
#  return jsonify(employee), 200