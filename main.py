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

def name_all(hero):
   s_h_all = []
   with open ("DATA\data.json", "r") as f:
       data_json = json.load(f)
       for i in data_json:
           a = i["name"]
           s_h_all.append(a)
       hero_len = len(hero)
       resualt_name_all = list(set(hero) & set(s_h_all))
       if len(resualt_name_all) == hero_len:
          return f"Вcе супер герои есть в нашем списке"
       else:
          return 

def clever(hero):
   s_h = {}
   with open ("DATA\data.json", "r") as f:
       data_json = json.load(f)
       data_len = len(data_json)
       for n1 in hero:
           count = 0
           while data_json[count]['name'] != n1:
               count += 1
           else:
              intel = data_json[count]["powerstats"]["intelligence"]
              s_h[n1] = intel
       #print(list(s_h))
       a = max(s_h, key = s_h.get)
       return f"Самый умный супер герой: {a}"
       
 
print(requests_1())

def main ():
    yes_no = "да"
    while yes_no == "да":
        input_hero = input('Введите Супергероев которых Вы хотите сравнить: ')
        input_hero2 = input_hero.split(', ')
        while name_all(input_hero2) == None:
            input_hero = input('Введите других Супергероев: ')
            input_hero2 = input_hero.split(', ')
        else:    
            print(clever(input_hero2))
        
        yes_no = input("Хотите продолжить сравнение?")
 
print(main())   