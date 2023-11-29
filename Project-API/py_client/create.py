import requests

headers = {'Authorization': 'Token d8c11e7f5b187c7e288c39dbbefe9a7b3a745a93'}

endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.post(endpoint, json = {"title":"Niraj", "price":"20"})

print(get_response.json())

"""
python manage.py shell
from rest_framework.authtoken.models import *
locals()
Token.objects.all()
Token.objects.all().first()
dir(Token.objects.all().first())
token_obj = Token.objects.first()
token_obj.created
exit()
"""