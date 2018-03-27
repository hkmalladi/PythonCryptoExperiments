from Crypto.Hash import SHA256

with open('buttonPress_3.db', 'r') as myfile:
    data=myfile.read().replace('\n', '')

sha = SHA256.new(data).hexdigest()
print sha
