from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# ── Generate RSA keys ────────────────────────────────────────
key        = RSA.generate(2048)
public_key  = key.publickey()

print("RSA keys generated!")
print(f"Public key:\n{public_key.export_key().decode()}\n")

# ── Encrypt a message ────────────────────────────────────────
message   = input("Enter message to encrypt: ").encode()
cipher    = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(message)

print(f"\n Encrypted: {encrypted.hex()}")

# ── Decrypt the message ──────────────────────────────────────
cipher2   = PKCS1_OAEP.new(key)
decrypted = cipher2.decrypt(encrypted)

print(f"Decrypted: {decrypted.decode()}")
