from Crypto.Hash import SHA256
import sys

file = sys.argv[1]
with open(file, 'r') as myfile:
    data=myfile.read().replace('\n', '')

sha = SHA256.new(data).hexdigest()
print sha
