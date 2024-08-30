import hashlib
import hmac
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, utils
from cryptography.hazmat.backends import default_backend

def generate_rsa_keypair():
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return key

def sign_message(private_key, message, algorithm):
    if algorithm == "rsa":
        signer = private_key.signer(
            padding.PSS(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        signer.update(message.encode())
        signature = signer.finalize()
        return signature
    elif algorithm == "hmac":
        signature = hmac.new(private_key, message.encode(), hashlib.sha256).digest()
        return signature
    else:
        raise ValueError("Invalid signature algorithm")

def verify_signature(public_key, message, signature, algorithm):
    if algorithm == "rsa":
        verifier = public_key.verifier(
            signature,
            padding.PSS(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        verifier.update(message.encode())
        verifier.verify()
        return True
    elif algorithm == "hmac":
        expected_signature = hmac.new(public_key, message.encode(), hashlib.sha256).digest()
        return hmac.compare_digest(signature, expected_signature)
    else:
        raise ValueError("Invalid signature algorithm")

# Example usage:
private_key = generate_rsa_keypair()
public_key = private_key.public_key()
message = "Hello, universe!"
signature = sign_message(private_key, message, "rsa")
print("RSA signature:", signature)

verified = verify_signature(public_key, message, signature, "rsa")
print("Verification result:", verified)
