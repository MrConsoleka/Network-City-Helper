from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode
import os
import asyncio
from source.misc import get_keys


async def decryption(password):
    try:
        env_data = get_keys().SECRET_KEY

        security_key = env_data.encode('utf-8')

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=security_key,
            iterations=480000,
            backend=default_backend()
        )

        # Генерируем ключ
        key = urlsafe_b64encode(kdf.derive(security_key))

        # Создаем объект шифрования
        cipher_suite = Fernet(key)

        # Пытаемся расшифровать сообщение
        decrypted_message = cipher_suite.decrypt(password)

        return decrypted_message.decode('utf-8')

    except InvalidToken:
        print("Ошибка: недействительный токен. Проверьте правильность введенного токена.")
        return "Token"

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False
