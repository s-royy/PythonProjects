import random
import string


def generate_password(length: int, use_digits: bool, use_symbols: bool) -> str:
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

