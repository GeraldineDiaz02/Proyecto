from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import consultarbase as cb
import sys

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("loginInterfaz.ui", self)
        self.show()

        self.ui.entrar.clicked.connect(self.entrando)
        self.ui.llevarsingup.clicked.connect(self.open_singup_ui)

    def entrando(self):
        usuario = self.ui.usuario_log.text()
        contrasena = self.ui.contrasena_log.text()
        res, contrasenaveri = cb.validar(usuario)
        if res and contrasena == contrasenaveri:
            QMessageBox.information(self, "Inicio de sesión", "Inicio de sesión exitoso")
        else:
            QMessageBox.warning(self, "Inicio de sesión", "Nombre de usuario o contraseña incorrectos")

    def open_singup_ui(self):
        self.hide()  # Ocultar la ventana de loginInterfaz.ui
        singup_window = SingUpWindow()
        singup_window.show()

class SingUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("singup.ui", self)
        self.show()

        self.ui.registrar.clicked.connect(self.registro_exitoso)

    def registro_exitoso(self):
        email = self.ui.inemail.text()
        contrasena = self.ui.incontrasena.text()
        numcel = self.ui.innumcel.text()

        if cb.verificar_datos_existente(email, numcel):
            QMessageBox.warning(self, "Registro", "El correo electrónico o número de celular ya está registrado.")
        else:
            resultado = cb.crearusu(email, contrasena, numcel)
            QMessageBox.information(self, "Registro", "Registro exitoso.")
            self.hide()  # Ocultar la ventana de singup.ui
            create_user_window = CreateUserWindow(email)
            create_user_window.show()

class CreateUserWindow(QMainWindow):
    def __init__(self, email):
        super().__init__()
        self.ui = loadUi("createuser.ui", self)
        self.show()

        self.email = email

        self.ui.crear.clicked.connect(self.registro)

    def registro(self):
        nombre = self.ui.innombre.text()
        fechana = self.ui.innacimiento.text()

        if self.ui.women.isChecked():
            genero = 'f'
        else:
            genero = 'm'

        intereses = self.ui.inintereses.text()
        descripcion = self.ui.indescripcion.text()
        profesion = self.ui.inprofesiones.text()
        areadetrab = self.ui.inworkarea.text()

        result = cb.registrar(self.email, nombre, fechana, genero, intereses, descripcion, profesion, areadetrab)
        if result == "1":
            QMessageBox.information(self, "Registro", "Usuario creado exitosamente")
            self.hide()  # Ocultar la ventana de createuser.ui
            login_window = Principal()  # Crear una instancia de la clase Principal
            login_window.show()  # Mostrar la ventana de loginInterfaz.ui
        else:
            QMessageBox.warning(self, "Registro", "Error al crear el usuario")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    sys.exit(app.exec_())
