# PROGRAMOS SIFR_AESS.PY KODAS
from Crypto.Cipher import AES
from binascii import unhexlify

def decrypt_aes_eax(ciphertext_hex, key, tag_hex, nonce_hex):
    # Konvertuojame šiuos duomenis iš šešioliktainės į baitų sekas
    ciphertext = unhexlify(ciphertext_hex)
    tag = unhexlify(tag_hex)
    nonce = unhexlify(nonce_hex)

    # Sukuriamas šifravimo objektas su pateiktu raktu ir nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
     
    # Bandoma iššifruoti tekstą ir patikrinti MAC su pateiktu tag'u
    try:
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data.decode('utf-8')
    except ValueError:
        return "Užšifruotas tekstas buvo pažeistas. Iššifravimas nutrauktas."

def main():
    # Pateikti duomenys
    key = b"ThisIsASecretKey_32bytesLongAbCd"
    ciphertext_hex = "a8cfed33a6ca1fd8bc16f5f712544a9c6350f20b5597495d46b4222b81c0cd7c4ead46e9811bcd7040d814348123cbc4718df4e03403106d7dc846e009755cd2943ed6a044761c410e6e88c5f2"
    tag_hex = "1d7fce75962fa02764f15b57769d097a"
    nonce_hex = "6900c5899fa76800ba7bff77e0fe6cb6"

    decrypted_message = decrypt_aes_eax(ciphertext_hex, key, tag_hex, nonce_hex)
    print(f"Iššifruotas tekstas: {decrypted_message}")

if __name__ == '__main__':
    main()
