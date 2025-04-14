# PROGRAMOS SIFR_AESR.PY KODAS
from Crypto.Cipher import AES

def main():
    # Naudokime pastovų 32 baitų ilgio raktą
    key = b"ThisIsASecretKey_32bytesLongAbCd"
    
    # Inicijuoti AES šifro objektą su EAX režimu
    cipher = AES.new(key, AES.MODE_EAX)
    
    # Teksto užšifravimas
    plaintext = b"Slapta: Kompiuteris yra tavo ir mano geriausias draugas :-)."
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    # Atspausdiname raktą, užšifruotą tekstą, tag ir nonce reikšmes
    print(f"Raktas: {key.decode('utf-8')}")
    print(f"Užšifruotas tekstas: {ciphertext.hex()}")
    print(f"Tag: {tag.hex()}")
    print(f"Nonce: {cipher.nonce.hex()}")  # Atspausdiname nonce reikšmę

    # Teksto iššifravimas
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    decrypted = cipher_dec.decrypt(ciphertext)
    
    # Patikriname, ar iššifruotas tekstas sutampa su pradiniais duomenimis
    try:
        cipher_dec.verify(tag)
        print(f"Pradinis: {decrypted.decode('utf-8')}")
    except ValueError:
        print("Iššifruotasis tekstas yra neteisingas!")

if __name__ == '__main__':
    main()
