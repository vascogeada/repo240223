import hashlib
 
# The string to be hashed
input_string = "ABC"
 
# Create a new SHA-256 hash object
hash_object = hashlib.sha256(input_string.encode())
 
# Get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()
 
# Print the hash
print(hex_dig)
 
print(f"A resposta tem {len(hex_dig)} letras")