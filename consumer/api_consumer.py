import requests
import json

hit= 'http://127.0.0.1:8000/api/all_todo/'


def get_data(id=None):
    data={}

    if id is not None:

        data={'id':id}
        
    headers={'content-Type':'application/json'}
 
    json_datas=json.dumps(data)
    res=requests.get(url = hit,headers=headers, data = json_datas)
    pdatas=res.json()
    print(pdatas)


def post_data():
    data={
        'name':"Create django api",
        'description':'I will create a django api',
        'complete':'2025-07-08',
        "is_complete": False
    }
    headers={'content-Type':'application/json'}

   

    
    res=requests.post(url = hit,headers=headers ,json=data)
    pdatas=res.json()
    print(pdatas)

post_data()


