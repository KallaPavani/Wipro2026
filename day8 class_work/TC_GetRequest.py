import requests

geturl="https://api.restful-api.dev/objects"

response=requests.get(geturl)
print(response.json())
print(response.status_code)

posturl="https://api.restful-api.dev/objects"

body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r1=requests.post(posturl,json=body1)
print(r1.json())
print(r1.status_code)

puturl="https://api.restful-api.dev/objects/ff8081819782e69e019be405eeb12e84"

body2={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
r2=requests.put(puturl,json=body2)
print(r2.json())
print(r2.status_code)

patchurl="https://api.restful-api.dev/objects/ff8081819782e69e019be405eeb12e84"

body3={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}
r3=requests.patch(patchurl,json=body3)
print(r3.json())
print(r3.status_code)

deleteurl="https://api.restful-api.dev/objects/ff8081819782e69e019be405eeb12e84"

r4=requests.delete(deleteurl)
print(r4.json())
print(r4.status_code)
