from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# save private key to file
with open('private.pem', 'wb') as f:
    f.write(private_key)

# save public key to file
with open('public.pem', 'wb') as f:
    f.write(public_key)

print('Private key saved to private.pem')
print('Public key saved to public.pem')
print('Done')
print(private_key)