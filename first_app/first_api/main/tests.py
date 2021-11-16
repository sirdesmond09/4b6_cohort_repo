# from django.test import TestCase

# # Create your tests here.


import requests

url = 'http://localhost:8000/students/'

res = requests.get(url)

print(res.json())