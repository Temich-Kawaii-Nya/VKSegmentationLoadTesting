import random
import string


def generate_random_string(length = 32):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k = length))