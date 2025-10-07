import unicodedata
import string
from math import gcd

DEFAULT_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
SPACE_MARKER = "XMEZERAX"


def remove_diacritics(text):
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join([c for c in nfkd if not unicodedata.combining(c)])


def filter_input(text, alphabet=DEFAULT_ALPHABET):
    text = remove_diacritics(text)
    result = ""
    for c in text.upper():
        if c == " ":
            result += SPACE_MARKER
        elif c in alphabet:
            result += c
    return result


def restore_spaces(text):
    return text.replace(SPACE_MARKER, " ")


def format_five(text):
    return " ".join([text[i : i + 5] for i in range(0, len(text), 5)])


def modinv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Inverse does not exist for a={a}, m={m} (must be coprime)")


def check_key_a(a, alphabet):
    return gcd(a, len(alphabet)) == 1


def encrypt(plain_text, a, b, alphabet=DEFAULT_ALPHABET):
    filtered = filter_input(plain_text, alphabet)
    cipher = ""
    i = 0
    while i < len(filtered):
        if filtered[i : i + len(SPACE_MARKER)] == SPACE_MARKER:
            cipher += SPACE_MARKER
            i += len(SPACE_MARKER)
            continue
        char = filtered[i]
        idx = alphabet.find(char)
        if idx == -1:
            i += 1
            continue
        c_idx = (a * idx + b) % len(alphabet)
        cipher += alphabet[c_idx]
        i += 1
    return format_five(cipher)


def decrypt(cipher_text, a, b, alphabet=DEFAULT_ALPHABET):
    inv_a = modinv(a, len(alphabet))
    cipher_text = cipher_text.replace(" ", "")
    plain = ""
    i = 0
    while i < len(cipher_text):
        if cipher_text[i : i + len(SPACE_MARKER)] == SPACE_MARKER:
            plain += SPACE_MARKER
            i += len(SPACE_MARKER)
            continue
        char = cipher_text[i]
        idx = alphabet.find(char)
        if idx == -1:
            i += 1
            continue
        p_idx = (inv_a * (idx - b)) % len(alphabet)
        plain += alphabet[p_idx]
        i += 1
    return restore_spaces(plain)


def get_filtered_input(plain_text, alphabet=DEFAULT_ALPHABET):
    return filter_input(plain_text, alphabet)


def get_cipher_alphabet(a, b, alphabet=DEFAULT_ALPHABET):
    return "".join(
        [alphabet[(a * i + b) % len(alphabet)] for i in range(len(alphabet))]
    )
