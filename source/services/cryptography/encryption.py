from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode
import os
import asyncio
from source.misc import get_keys


async def encryption(password: str):
    try:
        password = password.encode('utf-8')

        env_data = get_keys().SECRET_KEY

        security_key = env_data.encode('utf-8')

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=security_key,
            iterations=480000,
            backend=default_backend()
        )

        key = urlsafe_b64encode(kdf.derive(security_key))

        cipher_suite = Fernet(key)

        encrypted_password = cipher_suite.encrypt(password)

        key = encrypted_password.decode('utf-8')

        return key

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False
