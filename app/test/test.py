
import requests 

resp = requests.post("https://127.0.0.1:5000//predict",files={'file': open('images.jpg', 'rb')})

print(resp.text)
