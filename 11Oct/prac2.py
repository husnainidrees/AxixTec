
from flask import Flask ,request ,jsonify

app =Flask(__name__)

model=[]

# @app.get('/friend/<int:id>')

# def get_one_fre(id):
#     return model[id] ,200


@app.post('/friend')

def create_friend():
    req_data=request.get_json()
    new_friend={"name":req_data["name"],"id":len(model)}
    model.append(new_friend)

    return new_friend,201


@app.delete('/friend/<int:id>')
def delet_friend(id):
    del model[id]

    return{"success":"Data sucessfully deleted from"}




if __name__=="__main__":
    
    app.run(debug=True,port=8332)



