from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generuojame RSA privatųji ir viešąjį raktą
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Eksportuojame viešąjį raktą PEM formatu
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("Viešasis raktas:")
print(public_pem.decode("utf-8"))

# Eksportuojame privatųjį raktą PEM formatu
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

print("Privatusis raktas:")
print(private_pem.decode("utf-8"))

# Užšifruojame žinutę su viešuoju raktu
original_message = b"Andrej Gorbatniov"
ciphertext = public_key.encrypt(
    original_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Užšifruota žinutė:", ciphertext)

# Iššifruojame žinutę su privačiuoju raktu
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Iššifruota žinutė:", decrypted_message.decode("utf-8"))
