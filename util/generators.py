import random

def generate_email():
    name ='mikhail_chubarov'
    cog = '21_FS'
    random_num = str(random.randint(100, 999))
    return f'{name}_{cog}_{random_num}@yandex.ru'

def generate_password(length=6):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(chars) for _ in range(length))