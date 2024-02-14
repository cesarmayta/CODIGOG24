import jwt
SECRET_KEY = 'QWERTY123'

token = input('inserta token :')

try:
    validate_jwt = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
    print('token valido')
    print(validate_jwt)
except Exception as error:
    print("Error : ",error)