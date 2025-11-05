Install :
pip install requests


Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The requests library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python’s built-in libraries and tools enable effortless data manipulation and processing.

Behold, the power of Requests:

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

r.status_code
200

r.headers['content-type']
'application/json; charset=utf8'

r.encoding
'utf-8'

r.text
'{"type":"User"...'

r.json()
{'private_gists': 419, 'total_private_repos': 77, ...}