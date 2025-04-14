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
    ciphertext_hex = "47b3ec03eacbe4aaddb22192c685f69da5c0fab86d5b7c0fb56e9c00f1035ef59eb1146cbd44138d9e9fa69e7b3b8957a65ff9a3464a3eebb5762b9172e64844cfe380807c2baf7c4b11a23af2e25969a52e7275e2e1591dfd3cd0392c18c7db1c6397b69800"
    tag_hex = "692a8142327e1fd3de00bd76a1833931"
    nonce_hex = "3150360edd204dbcb610883b168b5958"

    decrypted_message = decrypt_aes_eax(ciphertext_hex, key, tag_hex, nonce_hex)
    print(f"Iššifruotas tekstas: {decrypted_message}")

if __name__ == '__main__':
    main()
