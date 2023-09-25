import hashlib

def descifrar_mensaje(mensaje, n):
    mensaje_descifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            nueva_letra = chr(((ord(letra) - ord('a') - n) % 26) + ord('a'))
            mensaje_descifrado += nueva_letra
        else:
            mensaje_descifrado += letra
    return mensaje_descifrado

def verificar_integridad(mensaje_descifrado, hash_original):
    hash_calculado = hashlib.sha256(mensaje_descifrado.encode()).hexdigest()
    print("calculado",hash_calculado)
    return hash_calculado == hash_original

with open("mensajeseguro.txt", "r") as archivo_seguro:
    mensaje_cifrado = archivo_seguro.readline().strip()
    hash_original = archivo_seguro.readline().strip()

n = 3
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, n)

if verificar_integridad(mensaje_descifrado, hash_original):
    print("original",hash_original)
    print("El mensaje es válido y no ha sido modificado.")
    print("Mensaje original:",mensaje_descifrado)
else:
    print("El mensaje ha sido modificado o es inválido.")
