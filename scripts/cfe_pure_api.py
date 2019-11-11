import requests 

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    #print(type(json.dumps(data)))
    for obj in data:
        print(obj['id'])
        if obj ['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
    return data


#print (get_list())
get_list()