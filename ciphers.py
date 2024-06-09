from itertools import islice, cycle

def get_letter_value(letter: str) -> int:
    return ord(letter) - 65

def get_letter_from_value(value: int) -> str:
    return chr(value + 65)

def caeser_cipher(text: str, shift: int, decrypt: bool) -> str:
    text_lst: list[str] = list(text)
    result: str = ""

    if decrypt:
        shift = -shift

    for letter in text_lst:
        value: int = get_letter_value(letter)
        if not decrypt:
            result += get_letter_from_value(value + shift)

    return result

def vigenère_cipher(text: str, key: str, decrypt: bool) -> str:
    text_lst: list[str] = list(text)
    key_lst: list[str] = list(key)

    if len(key_lst) < len(text_lst):
        key_lst = list(islice(cycle(key_lst), len(text_lst)))
    if len(key_lst) > len(text_lst):
        key_lst = key_lst[:len(key_lst)]

    result: str = ""

    for index, letter in enumerate(text_lst):
        letter_value: int = get_letter_value(letter)
        key_value: int = get_letter_value(key_lst[index])
        new_letter: str = get_letter_from_value((letter_value + key_value) % 26)
        print(letter, letter_value, key_value, new_letter)

    return result
print(vigenère_cipher("DCODE", "KEY", False))