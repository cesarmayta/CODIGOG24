import jwt

payload = {
    'usuario':'cesar',
    'email':'cesarmayta@gmail.com',
    'id':1
}

SECRET_KEY = 'QWERTY123'

token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')
print('mi token es :',token)