
from flask import Flask,jsonify,request

app=Flask(__name__)


@app.route('/api/post_name/',methods=['POST'])

def user_info():

    data=request.get_json()
    res={'rec':data}

    user_name=data['name']
    user_age=data['age']
    user_region=['region']

    print(user_name,user_age)

    if user_age > 18 and user_name[0] == 'h' :
        print("Congratulation You are Pakistani")
    else:
        print("Oh Sorry You are not eligiable for This Criteria")


    return jsonify(res),201





if __name__=="__main__":

    app.run(debug=True,port='8332')