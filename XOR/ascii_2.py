plaintext = "ABCDE"
XOR_KEY = "PASSW"

Encrypted_Values = []

for Position, PlainTextCharacter in enumerate(plaintext):
	print(Position, PlainTextCharacter)
	print(Position, XOR_KEY[Position])
	print("Xoring the two above values together and saving the result to a list!")
	encrypted_byte = ord(PlainTextCharacter) ^ ord(XOR_KEY[Position])
	
	Encrypted_Values.append(encrypted_byte)

print("The encrypted decimal values when XORing the each of these letters together is:")
print(Encrypted_Values)

print("Here are the hex values:")
for i in Encrypted_Values:
	print(hex(i), " ", end='')
print()

print("Here are the hex values with a space between them instead of 0x")
for i in Encrypted_Values:
	print(format(i, 'x'), " ", end='')
