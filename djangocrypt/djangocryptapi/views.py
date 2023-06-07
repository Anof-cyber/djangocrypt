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
from cryptography.hazmat.backends import default_backend
import json
import base64
import hashlib

from urllib.parse import unquote_plus


def home(request):
    return render(request, 'home.html')


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
    data = json.loads(unpadded_data.decode('utf-8'))

    # Return the decrypted data as a dictionary
    return data