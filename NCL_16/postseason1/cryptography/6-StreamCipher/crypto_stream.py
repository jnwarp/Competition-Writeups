
# for stream cipher
d = { chr(c+64) : c for c in range(1,27) }

def encrypt_one(let, key):
	new_let = d[let] + d[key]
	if new_let > 26:
		new_let -= 26
	return chr(new_let+64), let

def decrypt_one(let, key):
	new_let = d[let] + 26-d[key]
	if new_let > 26:
		new_let -= 26
	return chr(new_let+64)

def encrypt(plain, key):
	cipher = ""
	for c in plain:
		new_let, key = encrypt_one(c, key)
		cipher += new_let
	return cipher

def decrypt(cipher, key):
	plain = ""
	for c in cipher:
		new_let = decrypt_one(c, key)
		key = new_let
		plain += new_let
	return plain
