import requests

geturl="http://127.0.0.1:5001/users"

headers={
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Client",
}
response=requests.get(geturl,headers=headers,timeout=10)
print(response.status_code)
print(response.json())

posturl="http://127.0.0.1:5001/users"
body1={
    "name":"Joseph"
}
response=requests.post(posturl,json=body1)
print(response.status_code)
print(response.json())

puturl="http://127.0.0.1:5001/users/2"
body2={
    "name":"Preethi"
}
response=requests.put(puturl,json=body2)
print(response.status_code)
print(response.json())

patchurl="http://127.0.0.1:5001/users/1"
body3={
    "name":"Pavani Kalla"
}
response=requests.patch(patchurl,json=body3)
print(response.status_code)
print(response.json())

deleteurl="http://127.0.0.1:5001/users/2"
response=requests.delete(deleteurl)
print(response.status_code)
print(response.json())