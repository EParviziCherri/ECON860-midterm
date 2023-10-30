import requests
import os
import time
import datetime
import pandas 
import json


if not os.path.exists("json_files"):
    os.mkdir("json_files")

access_point = "https://api.github.com"

f = open("token", "r")
token = f.read()
f.close()

dataset = pandas.read_csv("parsed_files/new_dataset.csv")
login_ids = dataset["Login_ID"]

github_session = requests.Session()
github_session.auth = ("EParviziCherri", token)

response_text = github_session.get(access_point + "/rate_limit").text
print(json.loads(response_text))

for Login_ID in login_ids:
    user_id = Login_ID
    file_name = "json_files/"+user_id+ ".json"

    if os.path.exists(file_name):
        print("File exists", user_id)
    else:
        try:
            print(user_id)
            response_text = github_session.get(Login_ID).text

            json_text = json.loads(response_text)

            f = open(file_name + ".tmp", "w")
            f.write(json.dumps(json_text))
            f.close()
      
            os.rename(file_name + ".tmp", file_name)
        except Exception as e:
            print(e)

    time.sleep(5)
