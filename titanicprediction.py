import json
import requests

# data input
PassengerId= int(input("enter the passenger id: "))
Pclass	=   int(input("enter the passenger class: "))
Age	=       int(input("enter the age of the passenger: "))
SibSp=	    int(input("enter the sibsp of passenger: "))
Fare=	    float(input("enter the fair of passenger: ")) 
male=	     int(input("enter the sex of passenger typr 1 for male and 0 for female:"))
Q	=         int(input("enter the embarked if it'q type 0:"))   
S=             int(input("enter the s type 1 for it: "))

url  = "http://127.0.0.1:5000/"
data = {"PassengerId": PassengerId, "Pclass":Pclass, "Age":Age, "SibSp":SibSp , "Fare": Fare, "male":male, "Q":Q, "S":S}

dataJSON = json.dumps(data)
headers = {"Content-type":"application/json"}
responce = requests.post(url=url, data = dataJSON, headers=headers)
print(responce)
output = json.loads(responce.text)

prediction = output["prediction"]

if prediction == 1:
    print("congo ! the passenger you search is alive ")

else:
    print("i am sorry !! the pasenger you search is no alive ")