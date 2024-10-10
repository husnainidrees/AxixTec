
from flask import Flask ,request,jsonify

app=Flask(__name__)


@app.route('/arms',methods=['POST'])

def arm(n):
    sum=0
    order=len(str(n))
    copy_n=n
    while (n>0):
        digit=n%10
        sum+= digit** order
        n=n/10
    if sum == copy_n:
        print(f"{copy_n} is an armstrong number ha ")
        result={
            "Number":copy_n,
            "Armstrong":True,
            "Server":"127.0.0.1"

        }
    else:
         print(f"{copy_n} is not an armstrong number ha ")
         result={
            "Number":copy_n,
            "Armstrong":True,
            "Server":"127.0.0.1"

        }
    return jsonify(result)



if __name__=='__main__':

    app.run(debug=True,port=8332)