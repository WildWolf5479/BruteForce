import sys


ciphertext = sys.argv[1]
ciphertext_bytes = bytes.fromhex(ciphertext)


with open(sys.argv[2], 'r') as file:
	for line in file:
		key = line.strip().encode()
		decrypted = bytearray()

		for i in range(len(ciphertext_bytes)):
			decrypted.append(ciphertext_bytes[i] ^ key[i % len(key)])
		
		if all(32 <= byte <= 126 for byte in decrypted):
			print("Trying", line)
			print("Decrypted (ASCII):", decrypted.decode())

