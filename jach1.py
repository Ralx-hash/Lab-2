import hashlib


def cifrar_mensaje(mensaje, n):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            nueva_letra = chr(((ord(letra) - ord('a') + n) % 26) + ord('a'))
            mensaje_cifrado += nueva_letra
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

def generar_hash(mensaje):
    hash_obj = hashlib.sha256()
    hash_obj.update(mensaje.encode())
    return hash_obj.hexdigest()

with open("mensajedeentrada.txt", "r") as archivo_entrada:
    mensaje_original = archivo_entrada.read().lower()

n = 3
mensaje_cifrado = cifrar_mensaje(mensaje_original, n)

hash_original = generar_hash(mensaje_original)

with open("mensajeseguro.txt", "w") as archivo_seguro:
    archivo_seguro.write(mensaje_cifrado)
    archivo_seguro.write("\n")
    archivo_seguro.write(hash_original)
