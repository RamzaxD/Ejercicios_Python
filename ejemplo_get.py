"""Si necesita verificar si la variable es un diccionario antes de llamar get(), use el isinstance()método.

principal.py
"""
my_dict = {'name': 'Alice', 'age': 30}

if isinstance(my_dict, dict):
    print(my_dict.get('name'))  # 👉️ 'Alice'
    print(my_dict.get('age'))  # 👉️ 30
else:
    print('The value is NOT a dictionary')