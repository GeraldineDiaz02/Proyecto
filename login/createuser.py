import re     #es muy útil para tareas como la validación de entradas de usuario, el análisis de archivos de texto, la manipulación de cadenas de texto complejas y otras aplicaciones en las que se requiere una manipulación precisa de los patrones de texto
import dicccredentials as dc

def addUser():
    # Solicita el nombre de usuario y contraseña al usuario
    username = input("Enter username:")
    
    while True:
        password = input("Enter password:")
        
        # Verifica que la contraseña cumpla con las condiciones especificadas
        if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])[^\s]{8,16}$', password): #para aplicar una expresión regular a la variable "password" y verificar si cumple con ciertas condiciones de complejidad.
            # Agrega el nuevo usuario al diccionario de credenciales
            #credentials[username] = password
            dc.registro(username,paswword)
            # Imprime un mensaje de confirmación
            print("User added successfully!")

            # Llama a la función main del archivo dicccredentials para ver la lista actualizada de usuarios y contraseñas
            import dicccredentials
            dicccredentials.main()
            break
        else:
            print(f"\t"+"The password must contain at least one uppercase letter\n" +
                f"\t"+"one lowercase letter, one special character, no spaces, and\n" +
                f"\t"+"be between 8 and 16 characters")
