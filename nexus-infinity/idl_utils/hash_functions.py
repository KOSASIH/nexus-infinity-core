import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def sha512(data):
    return hashlib.sha512(data.encode()).hexdigest()

def blake2b(data):
    return hashlib.blake2b(data.encode()).hexdigest()

def keccak256(data):
    return hashlib.sha3_256(data.encode()).hexdigest()

def ripemd160(data):
    return hashlib.new('ripemd160', data.encode()).hexdigest()

def whirlpool(data):
    return hashlib.new('whirlpool', data.encode()).hexdigest()

def hash_function_selector(algorithm, data):
    if algorithm == "sha256":
        return sha256(data)
    elif algorithm == "sha512":
        return sha512(data)
    elif algorithm == "blake2b":
        return blake2b(data)
    elif algorithm == "keccak256":
        return keccak256(data)
    elif algorithm == "ripemd160":
        return ripemd160(data)
    elif algorithm == "whirlpool":
        return whirlpool(data)
    else:
        raise ValueError("Invalid hash algorithm")

# Example usage:
data = "Hello, universe!"
hash_value = hash_function_selector("sha256", data)
print("SHA-256 hash:", hash_value)
