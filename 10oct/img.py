
from flask import Flask,request,jsonify

app=Flask(__name__)



@app.route('/img',methods=['POST'])

def main():
    try:
        if request.method=='POST':
            # print("request",request.form)
            image=request.files['image']
            image_name=image.filename
            if '.jpg' in image_name:
            
                
                image.save(image_name)

                return {"response":"file saved successfully in your current durectory"}
            elif '.jpeg' in image_name: 
                image.save(image_name)

                return {"response":"file saved successfully in your current durectory"}
            else:
                return {"error":"select you image file"}
    except Exception as e:
        return {"error":str(e)}

    

if __name__=="__main__":

    app.run(debug=True,port=8332)