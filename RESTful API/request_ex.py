import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')

print(r.url)
print(r.status_code)
print(r.text)