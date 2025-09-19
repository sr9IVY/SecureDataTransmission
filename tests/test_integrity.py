from utils import hashing

def test_hash_integrity():
    data = "Test message"
    hash1 = hashing.sha256_hash(data)
    hash2 = hashing.sha256_hash(data)
    assert hash1 == hash2, "Hashes should match"

if __name__ == "__main__":
    test_hash_integrity()
    print("✅ Hash integrity test passed.")
