def caeser_cipher(plaintext: str, shift: int, decrypt: bool) -> str:
    text_lst: list[str] = list(plaintext)
    result: str = ""

    for letter in text_lst:
        value: int = ord(letter)
        if not decrypt:
            result += chr(value + shift)
        else:
            result += chr(value - shift)
    return result