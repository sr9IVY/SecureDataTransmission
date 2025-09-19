#Main.py the program that launches the project
from utils import hashing, encryption, signature, auth
from config import keys

def get_user_input():
    print("Enter your personal information:")
    fields = [
        "First Name", "Middle Initial", "Last Name",
        "Street Address", "Apartment",
        "City", "State", "Zip Code",
        "Email", "Phone (+1 format)"
    ]
    data = "\n".join([f"{field}: {input(f'{field}: ')}" for field in fields])
    return data

def main():
    user = auth.login()
    if not user:
        print("Access denied.")
        return

    message = get_user_input()
    original_hash = hashing.sha256_hash(message)

    key, iv = keys.generate_symmetric_key()
    encrypted = encryption.encrypt_message(message, key, iv)
    decrypted = encryption.decrypt_message(encrypted, key, iv)

    new_hash = hashing.sha256_hash(decrypted)
    integrity = "✅ Verified" if original_hash == new_hash else "❌ Tampered"

    print(f"\nOriginal Hash: {original_hash}")
    print(f"Decrypted Hash: {new_hash}")
    print(f"Integrity Check: {integrity}")

    priv_key, pub_key = keys.generate_rsa_keys()
    signature_bytes = signature.sign_message(original_hash, priv_key)
    verified = signature.verify_signature(original_hash, signature_bytes, pub_key)

    print(f"Digital Signature Verified: {'✅' if verified else '❌'}")

if __name__ == "__main__":
    main()
