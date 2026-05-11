from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# ── Generate random key ──────────────────────────────────────
key = get_random_bytes(16)      # 16 bytes = 128 bit key

# ── Encrypt ──────────────────────────────────────────────────
message   = input("Enter message to encrypt: ").encode()
cipher    = AES.new(key, AES.MODE_EAX)
encrypted, tag = cipher.encrypt_and_digest(message)

print(f"\n Encrypted: {base64.b64encode(encrypted).decode()}")

# ── Decrypt ──────────────────────────────────────────────────
cipher2   = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher2.decrypt(encrypted)

print(f" Decrypted: {decrypted.decode()}")
