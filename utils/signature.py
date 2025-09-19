from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def sign_message(message_hash: str, private_key) -> bytes:
    return private_key.sign(
        message_hash.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

def verify_signature(message_hash: str, signature_bytes: bytes, public_key) -> bool:
    try:
        public_key.verify(
            signature_bytes,
            message_hash.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False
