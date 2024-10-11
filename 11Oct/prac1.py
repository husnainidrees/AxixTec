

from flask import Flask,request,jsonify

import requests

app=Flask(__name__)


store=[

 {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
        ]
    }
]









@app.route('/task',methods=['POST'])

def create_store():


    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]

        }
    store.append(new_store)



    return jsonify(new_store),200









if __name__=="__main__":

    app.run(debug=True,port=8333)