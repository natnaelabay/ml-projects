import requests

response = requests.post("http://localhost:5000/classify",files={'file' : open('pneumonia2.jpeg','rb')})
print(response.text)