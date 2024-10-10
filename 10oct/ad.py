





from flask import Flask, request,jsonify


app=Flask(__name__)

@app.route('/audi_upload',methods=['POST'])

def post_name():
    
   data=request.files['audio2']

   res={'rec':data}
   print(res)

   return jsonify(res),201


if __name__=='__main__':
  
  app.run(debug=True,port=8332)
