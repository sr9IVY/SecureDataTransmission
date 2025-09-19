# keys.py handles key generation, which is essential for your encryption and digital signature modules.
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

def generate_symmetric_key():
    """
    Generates a 256-bit AES key and a 128-bit IV using secure randomness.
    """
    key = os.urandom(32)  # AES-256
    iv = os.urandom(16)   # AES block size
    return key, iv

def generate_rsa_keys():
    """
    Generates a 2048-bit RSA key pair for digital signatures.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key
