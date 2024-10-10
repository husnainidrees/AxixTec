
import json


# jo hamary pas json object ha wo string honi chaiye ist accept nai krta 

colors= '["Red","Yellow","White"]'

#list1=json.loads(colors)



# Convert Python Dictionary To JSOn

color1= ["Red","Yellow","White"]

JsonObj=json.dumps(color1)

print(JsonObj)

