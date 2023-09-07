import base64

plainText = "A"
password = "B"

ascii_decimal = ord(plainText) ^ ord(password)

ascii_hex = hex(ascii_decimal)

print(ascii_hex)


ascii_decrypted = int(ascii_hex, 16) ^ ord(password)

print(ascii_decrypted)

print(chr(ascii_decrypted))
