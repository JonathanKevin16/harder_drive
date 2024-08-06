import base64

class Encryptor:
    def encrypt(self, content):
        return base64.b64encode(content)

    def decrypt(self, encrypted_content):
        return base64.b64decode(encrypted_content)