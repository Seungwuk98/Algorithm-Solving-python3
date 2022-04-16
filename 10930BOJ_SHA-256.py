import hashlib

string = input()
data = string.encode()

hash_object = hashlib.sha256(data).hexdigest()
print(hash_object)
