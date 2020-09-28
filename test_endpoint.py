import requests 

r = requests.post("http://127.0.0.1:8000/sendPatientData", json = {"id": "1", "idnumber": "2222", "name": "gert", "surname": "pineapple", "telephone number1": "0000000000", "telephonenumber2" : "1234" , "emailaddress" :"a@a.tld", "male": "yes", "language": "xhosa", "dead": "2020/01/01 01:01"   })
