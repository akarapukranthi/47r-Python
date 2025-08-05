import requests

api="https://fakestoreapi.com/products"
requests.get(api)
var=requests.get(api)
products_data=var.json()
print(products_data)

for prod in products_data:
    print(prod["title"])
    


