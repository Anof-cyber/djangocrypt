from base64 import b64decode, b16decode
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.PublicKey import RSA
from base64 import b64decode, b16decode

def decrypt_with_private_key(encrypted_data_b64):
    # Read the private key from the file
    with open('private_key.pem', 'rb') as f:
        private_key_pem = f.read()

    
  

        # Decode the base64-encoded encrypted data
    
    decode_data = b64decode(encrypted_data_b64)
    private_key  = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCQY+VdHitfi0U2PjsSYhdiOLyJL4MYWoT1MjnbOYcpDPXk+C9TnPMItNJPVATV/+LM90BeSYWY0xE2RtddSF8qE6/nn8MFipBoKMSf+vlmMWDA4gLSPo9TWMIDcubR6fchk5ulxu8z2caul3qbSf1/ZC/OIRYNhQ3QtS1oTemvL0G1ELIVL2GIESD1WjUYsc3aSiosNqzHMl7eI7XttH4tiruPF/H8dBpbJanwO/11cRrrWLJ2mX4oV3L8v7nP1UEteeaEPzaYV+R6c+RgMi/5nXpFSKeJDNS7LMRotxOVIz6foyuO4aW7Y0dI9AbKRekPRTjyNNWaAFiIm7XPEZH1AgMBAAECggEADls4X3P+o68mcGMV9C53nRGqFp54PjrQfyFWz6geew4/AVyh4VeOHJP/WIQwlOcuhur15fS7yVBXJO/nPZmoCKLQzyAQlSOhVxHn9vDOd62Pgq4WJ2Rb/iapkmE2zQaicUlgD5wXhYQbipl6HH2UrGQVkr0HGHddwnN5MnvosRJvYL8iyUdOiQoBdD3nq5GqQshKtTVWQSha4UquuY2R9sqjAIjDJgTtxeX5Qt+oqwE2bq9ZQ9QXvRT7HI0TAw2+UjeauxdZUZfJrDiyn+PZRLg1dTSoHk5qLNLJ6QXFD+rw+itCtz4qLFeRDG/Ib5pQjU0FT0+Qy0VgaEHZ8A2M8wKBgQC7jxpfz7EKM0nkVJSj2vbtJA1GNZNnFutrssVrCEtBW5wUpl+s3KDSXdkQ4N9O+Bvsa09v8tVTtHqiU3my6L/mZ9W75WxgC7+1w4AfQDBEwRLG2MT6Ju9O7VS9FKAz4OURxc5WZTBqVs5/bZz4s0gP3XmHq1vE7RPbnVEYuE3FkwKBgQDFFCoovfTj333+Q3Aq6bH6vCYBmU2uPN/GQjsY7v+j6GMlUIMP075B/ey2QZSUJCtUmW/szan6fVDGn0Y24UqqT1aXCbuznm7eUEtJouSSY/fCydX9gPlQYKxskKz/tX/6dF7CqkbH6KXUNl/akB93Iuw3us0yRa8nc6VpPZL/VwKBgEQ8XOkMo6lFXZWvW+B9EibWXen0Jet0gDPPd1loTBC8Jn2wxdAa+HtwXz9vwG53f5k0tVLSMuBgIdmaqwT2/pHxpuXUIuiSfa3AMYWtEaKB57XmOUuVDK1XVOPxdBNLt6sOnvH5oHKfoELl+xzUBNyYw9Ui96Eea4ITquRmcQz3AoGBALPZ0x+bOwE51CFWKeb/ngzT51tOLDX2F8E2b/gxI9rRGKnU78Zh1h8jPAKXlqAa4fAylpHknlqaQj0A3XL35svF25+6ojEpRMRdQlfQ8Acoc9KvnznZmaxgjPoGjdpOKJzH1jKQcke9aJhhhthO7mgq1qeFMf3O2imGwE1qg9vBAoGBAK1b1hZV9FdFPeXQw6z3L7q1RAiSJ2eLrDurIQpKwzGCnD6u6dOjatM5iV7L9+0ST3x4KDtjtcadf5oSjqPbqOOCVCVreTH8UYGrHWx+uF5bAhWq7q34mhZIJkapgTIGiofghZXCpOlGnGgw4b2CLmkf/ovhLSRymdHFYHDWM7kB"
   
    if len(decode_data) == 127:
        hex_fixed = '00' + decode_data.hex()
        decode_data = b16decode(hex_fixed.upper())
    other_private_key = RSA.importKey(b64decode(private_key))
    cipher = Cipher_PKCS1_v1_5.new(other_private_key)
    decrypt_text = cipher.decrypt(decode_data, None).decode()
    return decrypt_text

