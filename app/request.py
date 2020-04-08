from requests import put, get, post
''' put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
print(get('http://localhost:5000/todo1').json())
put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
print(get('http://localhost:5000/todo2').json()) '''

post('http://localhost:5000/todos', data={'task': 'play ping pong'}).json()
