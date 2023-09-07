MyHexEncrypted = ['0x11', '0x03', '0x10', '0x17', '0x12']
XOR_KEY = "PASSW"

Encrypted_Decimal_Values = []

for i in MyHexEncrypted:
	Encrypted_Decimal_Values.append(int(i, 16))
print(Encrypted_Decimal_Values)


decrypted_values = []

for position, value in enumerate(Encrypted_Decimal_Values):
	decrypted_value = value ^ ord(XOR_KEY[position])
	decrypted_values.append(decrypted_value)

print("Decrypted Values Decimal:", decrypted_values)

print()
print("Plaintext String")
for i in decrypted_values:
	print(chr(i), end='')
