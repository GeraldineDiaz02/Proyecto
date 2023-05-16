from dicccredentials import credentials

def verifyCredentials(user, password, credentials):
    # Verifica si el usuario y contraseña ingresados coinciden con los datos almacenados en un diccionario.
    # Retorna True si la autenticación fue exitosa, False en caso contrario.
    if user in credentials and credentials[user] == password:
        return True
    else:
        return False

# Ejemplo de uso
authenticated = False
while not authenticated:
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    if verifyCredentials(user, password, credentials):
        print("Authentication successful!")
        authenticated = True
    else:
        print("Authentication failed. Please try again.")

