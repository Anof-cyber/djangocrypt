from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import status 

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import asymmetric
from cryptography.hazmat.backends import default_backend
import json
import base64
import hashlib
from django.http import JsonResponse, HttpResponseBadRequest
from django.db import connection
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from cryptography.hazmat.primitives import hashes
from .rsa import decrypt_with_private_key
import json
from urllib.parse import unquote_plus





def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def login2(request):
    return render(request, 'login2.html')


def login3(request):
    return render(request, 'login3.html')

def login4(request):
    return render(request, 'login4.html')

def login5(request):
    return render(request, 'login5.html')

def login6(request):
    return render(request, 'login6.html')


def login7(request):
    return render(request, 'login7.html')


def RSALogin(request):
    return render(request, 'login8.html')

@api_view(['POST'])
def loginuser(request):
    
    if request.method == 'POST':
        try:
            encrypted_data = json.loads(request.body)
            
            key = encrypted_data['key']
            iv = encrypted_data['iv']
            data = encrypted_data['data']
            
            decrypted_data = decrypt_data2(data, key, iv)
            
            
            username = decrypted_data['username']
            password = decrypted_data['password']
            hashed_password = make_password(password)

            query = f"SELECT * FROM auth_user WHERE username = '{username}' and password = '{hashed_password}'"
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                print(cursor)
                if row:
                    return JsonResponse({'message': 'Login successful'})
                    
                else:
                    # User not found
                    return JsonResponse({'message': 'Invalid Cred'}, status=400)
    


        except Exception as e:
            return HttpResponseBadRequest('Invalid request data')
    else:
        return HttpResponseBadRequest('Invalid request method')



@api_view(['POST'])
def loginuser2(request):
    
    if request.method == 'POST':
        try:

            encrypted_data_b64 = request.body.decode('utf-8')
            print(encrypted_data_b64)
    
            decrypted_data = decrypt_data(encrypted_data_b64)
            username = decrypted_data['username']
            password = decrypted_data['password']
            hashed_password = make_password(password)    
            print(username)  
            print(password)
            print(hashed_password)      
            

            query = f"SELECT * FROM auth_user WHERE username = '{username}' and password = '{hashed_password}'"
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                
                
                if row:
                   
                    return Response(encrypt_data({'message': 'Login successful'}))
                    
                else:
                    
                    return Response(encrypt_data({'message': 'Invalid Cred'}), status=400)
    


        except Exception as e:
            return HttpResponseBadRequest('Invalid request data')
    else:
        return HttpResponseBadRequest('Invalid request method')












@api_view(['POST'])
def loginuser3(request):   
    if request.method == 'POST':
        try:
            username = decrypt_data(request.data.get('username'))
            print(username)  
            password = decrypt_data(request.data.get('password'))

            hashed_password = make_password(password)    
            
            print(password)
            print(hashed_password)      
            

            query = f"SELECT * FROM auth_user WHERE username = '{username}' and password = '{hashed_password}'"
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                
                
                if row:
                   
                    return Response(encrypt_data({'message': 'Login successful'}))
                    
                else:
                    
                    return Response(encrypt_data({'message': 'Invalid Cred'}), status=400)
    


        except Exception as e:
            return HttpResponseBadRequest('Invalid request data')
    else:
        return HttpResponseBadRequest('Invalid request method')






@api_view(['POST'])
def loginuser4(request):   
    if request.method == 'POST':
        try:
            encrypted_data  = json.loads(request.body.decode('utf-8'))
            decrypted_data = {}
            for key, value in encrypted_data.items():
                try:
                    # Use the key and value for decryption
                    decrypted_key = decrypt_data(key)
                    decrypted_value = decrypt_data(value)
                    
                    # Add the decrypted key-value pair to the decrypted_data dictionary
                    decrypted_data[decrypted_key] = decrypted_value

                except Exception as e:
                    # Handle decryption errors here (if any)
                    print(f"Error during decryption: {e}")

            username = decrypted_data['username']
            print(username)  
            password = decrypted_data['password']

            hashed_password = make_password(password)    
            
            print(password)
            print(hashed_password)      
            

            query = f"SELECT * FROM auth_user WHERE username = '{username}' and password = '{hashed_password}'"
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                
                
                if row:
                   
                    return Response(encrypt_data({'message': 'Login successful'}))
                    
                else:
                    
                    return Response(encrypt_data({'message': 'Invalid Cred'}), status=400)
    


        except Exception as e:
            return HttpResponseBadRequest('Invalid request data')
    else:
        return HttpResponseBadRequest('Invalid request method')






@api_view(['POST'])
def loginuser5(request):
    
    if request.method == 'POST':
        try:
            encrypted_data = request.body.decode('utf-8')
            
            iv = request.META.get('HTTP_IV')
            key = request.META.get('HTTP_KEY')
            print(iv)
            
            decrypted_data = decrypt_data2(encrypted_data, key, iv)
            print(decrypted_data)
            
            
            username = decrypted_data['username']
            print(username)
            password = decrypted_data['password']
            hashed_password = make_password(password)

            query = f"SELECT * FROM auth_user WHERE username = '{username}' and password = '{hashed_password}'"
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                print(cursor)
                if row:
                    return JsonResponse({'message': 'Login successful'})
                    
                else:
                    # User not found
                    return JsonResponse({'message': 'Invalid Cred'}, status=400)
    


        except Exception as e:
            return HttpResponseBadRequest('Invalid request data')
    else:
        return HttpResponseBadRequest('Invalid request method')


@api_view(['POST'])
def loginuser6(request):   
    if request.method == 'POST':
        try:

            orignalhash = request.META.get('HTTP_SIGNATURE')
            rquestbody = request.body.decode('utf-8')
            hash_object = hashlib.md5(rquestbody.encode())
            md5_hash = hash_object.hexdigest()
            if str(orignalhash) == str(md5_hash):
                username = decrypt_data(request.data.get('username'))
                print(username)  
                password = decrypt_data(request.data.get('password'))

                hashed_password = make_password(password)    
                
                print(password)
                print(hashed_password)      
                

                query = f"SELECT * FROM auth_user WHERE username = '{username}' and password = '{hashed_password}'"
                
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    row = cursor.fetchone()
                    
                    
                    if row:
                    
                        return Response(encrypt_data({'message': 'Login successful'}))
                        
                    else:
                        
                        return Response(encrypt_data({'message': 'Invalid Cred'}), status=400)
    
            else:
                return Response(encrypt_data({'message': 'Invalid Signature'}), status=400)


        except Exception as e:
            return HttpResponseBadRequest('Invalid request data')
    else:
        return HttpResponseBadRequest('Invalid request method')


@api_view(['POST'])
def loginuser7(request):   
    if request.method == 'POST':
        try:

            orignalhash = request.META.get('HTTP_SIGNATURE')
            rquestbody = request.body.decode('utf-8')
            hash_object = hashlib.md5(rquestbody.encode())
            md5_hash = hash_object.hexdigest()
            if str(orignalhash) == str(md5_hash):
                username = request.data.get('username')
                print(username)  
                password = request.data.get('password')

                hashed_password = make_password(password)    
                
                print(password)
                print(hashed_password)      
                

                query = f"SELECT * FROM auth_user WHERE username = '{username}' and password = '{hashed_password}'"
                
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    row = cursor.fetchone()
                    
                    
                    if row:
                    
                        return Response(encrypt_data({'message': 'Login successful'}))
                        
                    else:
                        
                        return Response(encrypt_data({'message': 'Invalid Cred'}), status=400)
    
            else:
                return Response(encrypt_data({'message': 'Invalid Signature'}), status=400)


        except Exception as e:
            return HttpResponseBadRequest('Invalid request data')
    else:
        return HttpResponseBadRequest('Invalid request method')





@api_view(['POST'])
def loginuser8(request):   
    if request.method == 'POST':
        try:
            private_key_pem = "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBANDvGZTWCCTFIm+mVrqWb1M032ZNYFOi3Y1tKOtDf8S5+/20lUXhX778NK4shQSuX2lKpM6S/NygejKT3LTIDXOnPgvkjmfI+E/3TdA5aKK+fTeKo9UGoWiNsu2FgXwWwxOod80ppocq6v6hITouW4TfTz9TjU9uurGj1OZuqLXZAgMBAAECgYAhkEdrwXZNcd22UeJc1w3LMBMzO/rddKxiq8aHBLDhyX7RotDYCPx4kctkr4Iu3lQ1dehDxxkX2C/JMDekUv7V6wPugOkapqCitPWNzgwPZmo1Y6XSkaaqo7AwvDCDDgVBDQsMwcr30KP1iDbHdMZ80Guk6NcoMyz7nsRGAWuKAQJBAPKdcBUmfXELauhXMLPMPt5f9Y1HUnunS72fyRdsqFcFTIX1IN/o6cXlAemf3U1wB/ZuZxOlgFgxSDriRhnazF0CQQDcdfhJxizg/QIaC5CmcOCz6shESUuBBqcQyLmG82L1OrAf4cD8IV55W24GkuDglLB8g7r2FIZ416RC0puGLVetAkEApyDhRxCetTLiUG9Ps2vtmw6Lfuk03s2eFWBvDF3jkR6rWlREczplX9ej+6YOsvuL4KypARWvVhGM6lNZaxIYWQJBALUISnKKQaAfIvKwPH/wgRQ832bzqQSyqc2mhnLCuagWITqM7yQbYrDU22yaf/7rGmGk6onYIPRqX4Bf4UY1RaECQFQ5Zy2hveW9YDHpu5yfU2/GqTtx2Dckjk7MDG1TaNDreuovJkrIGITcOi+GNvub40hRUbsx58jP7v2jDcn/sC4="
           
            username = decrypt_with_private_key(request.data.get('username'))
            print(username)  
            password = decrypt_with_private_key(request.data.get('password'))

            hashed_password = make_password(password)    
            
            print(password)
            print(hashed_password)      
            

            query = f"SELECT * FROM auth_user WHERE username = '{username}' and password = '{hashed_password}'"
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                
                
                if row:
                   
                    return Response({'message': 'Login successful'})
                    
                else:
                    
                    return Response({'message': 'Invalid Cred'}, status=400)
    


        except Exception as e:
            return HttpResponseBadRequest('Invalid request data')
    else:
        return HttpResponseBadRequest('Invalid request method')
















@api_view(['GET'])
def myprofile(request):
    data = {"data": "data"}
    encrypted_data = encrypt_data(data)
    return Response(encrypted_data)


@api_view(['GET'])
def getallusers(request):
    userdetails = User.objects.all()
    serializer = UserSerializer(userdetails, many=True)
    return Response(encrypt_data(serializer.data))


@api_view(['GET'])
def getall(request):
    userdetails = User.objects.all()
    serializer = UserSerializer(userdetails, many=True)
    data = {"data": encrypt_data(serializer.data)}
    return Response(data)



@api_view(['GET'])
def getall2(request):
    userdetails = User.objects.all()
    serializer = UserSerializer(userdetails, many=True)
    data = {encrypt_data("data"): encrypt_data(serializer.data)}
    return Response(data)


@api_view(['POST'])
def getuser(request):
    encrypted_data_b64 = request.body.decode('utf-8')
    
    decrypted_data = decrypt_data(encrypted_data_b64)
    
    user_id = decrypted_data.get('user_id')
    user = User.objects.get(pk=user_id)

    serializer = UserSerializer(instance=user)
    return Response(encrypt_data(serializer.data))
    


@api_view(['POST'])
def getuser2(request):
    
    print(request.data.get('user_id'))
    user_id = decrypt_data(request.data.get('user_id'))
    user = User.objects.get(pk=user_id)

    serializer = UserSerializer(instance=user)
    data = {"data": encrypt_data(serializer.data)}
    return Response(data)
    


@api_view(['POST'])
def getuser3(request):
    
    user_id = decrypt_data(request.data.get('elHLzVxVH4e3AayiZkfB9g=='))
    user = User.objects.get(pk=user_id)

    serializer = UserSerializer(instance=user)
    data = {encrypt_data("data"): encrypt_data(serializer.data)}
    return Response(data)



@api_view(['POST'])
def getuser4(request):
    orignalhash = request.META.get('HTTP_SIGNATURE')
    rquestbody = request.body.decode('utf-8')
    hash_object = hashlib.md5(rquestbody.encode())
    md5_hash = hash_object.hexdigest()
    if str(orignalhash) == str(md5_hash):

        user_id = decrypt_data(request.data.get('user_id'))
        user = User.objects.get(pk=user_id)

        serializer = UserSerializer(instance=user)
        return Response(serializer.data)
    else:
        data = {"error": "Data is tampered, signature doesn't match"}
        return Response(data)



import urllib.parse

@api_view(['POST'])
def getuser5(request):
    user_id = request.GET.get('user_id')
    user_id = user_id.replace(" ", "+")
    print(user_id)
    user_id = decrypt_data(user_id)
    
    user = User.objects.get(pk=user_id)

    serializer = UserSerializer(instance=user)
    data = {"data": encrypt_data(serializer.data)}
    return Response(serializer.data)
    




def encrypt_data(data):
    # Convert the data to a string using JSON encoding
    #data_str = json.dumps(data)
    if isinstance(data, dict):
        # Convert the data to a string using JSON encoding
        data_str = json.dumps(data)
    else:
        # Convert the data to a string
        data_str = str(data)
    # Readable key and IV for development purposes
    key = b'mysecretkey12345'
    iv = b'n2r5u8x/A%D*G-Ka'

    # Pad the data using PKCS7 padding
    padder = PKCS7(128).padder()
    padded_data = padder.update(data_str.encode('utf-8')) + padder.finalize()

    # Create a Cipher object with AES CBC mode and PKCS7 padding
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Encrypt the data
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Convert the encrypted data to hexadecimal format
    #encrypted_data_hex = ciphertext.hex()
    encrypted_data_b64 = base64.b64encode(ciphertext).decode('utf-8')
    iv_b64 = base64.b64encode(iv).decode('utf-8')

    # Return the encrypted data and IV as a dictionary
    return encrypted_data_b64

   



def decrypt_data(encrypted_data_b64):
    # Convert the IV to bytes
    key = b'mysecretkey12345'
    iv = b'n2r5u8x/A%D*G-Ka'

    # Convert the encrypted data to bytes
    ciphertext = base64.b64decode(encrypted_data_b64.encode('utf-8'))

    # Readable key and IV for development purposes
    

    # Create a Cipher object with AES CBC mode and PKCS7 padding
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Decrypt the data
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted data using PKCS7 padding
    unpadder = PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
   
    # Convert the data from a string to a dictionary using JSON decoding
    try:
        data = json.loads(unpadded_data.decode('utf-8'))
    
    # Return the decrypted data as a dictionary
        return data
    except json.JSONDecodeError as e:
        return unpadded_data.decode('utf-8')




def decrypt_data2(encrypted_data_b64,key, iv):
    # Convert the encrypted data to bytes
    ciphertext = base64.b64decode(encrypted_data_b64.encode('utf-8'))

    # Create a Cipher object with AES CBC mode and PKCS7 padding
    cipher = Cipher(algorithms.AES(key.encode('utf-8')), modes.CBC(iv.encode('utf-8')), backend=default_backend())

    # Decrypt the data
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted data using PKCS7 padding
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Convert the data from bytes to a dictionary using JSON decoding
    data = json.loads(unpadded_data.decode('utf-8'))

    # Return the decrypted data as a dictionary
    return data




