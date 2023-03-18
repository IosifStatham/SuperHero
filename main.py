import requests
import json

def w_in_file(file1):
    file2 = file1.json()
    with open ("DATA\data.json", "w") as f:
        json.dump(file2, f)
        
def requests_1():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    #print(response.status_code)
    w_in_file(response)
    if response.status_code == 200:
        return "Операция выполнена успешно"
    else:
        return "Операция не выполнена" 

def clever():
   s_h = {}
   with open ("DATA\data.json", "r") as f:
       data_json = json.load(f)
       for i in data_json:
           
           "Thanos"
           if i["name"] == "Thanos":
              intel = i["powerstats"]["intelligence"]
              s_h[i["name"]] = intel
           elif i["name"] == "Captain America":
              intel = i["powerstats"]["intelligence"]
              s_h[i["name"]] = intel
           elif i["name"] == "Hulk":
              intel = i["powerstats"]["intelligence"]
              s_h[i["name"]] = intel
       
       a = max(s_h, key = s_h.get)
       
       return f"Самый умный супер герой: {a}"
                      
print(requests_1())
print(clever())