a = [1, 2, 3, 4]
print(a[-1])
a.reverse()
print(a)

b = [1, 2, 3, 4, 5, 6]
print(len(b))
for i in range(len(b) -1, -1, -1):
	print('index: {}, value: {}'.format((i), b[i]))

dict = {'id': 89, 'name': "John"}
print(dict['id'])
print(dict.get('id'))
print(dict.get('age', 0))
print(dict.get('age'))

dict2 = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
print(dict2.get('friends')[-1].get("name"))