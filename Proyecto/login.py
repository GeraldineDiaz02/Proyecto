import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import consultarbase as cb
import singup

class Principal(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.initGui()
    
    def initGui(self):
        uic.loadUi("loginInterfaz.ui",self)
        self.show()

        self.entrar.clicked.connect(self.entrando)
        self.llevarsingup.clicked.connect(self.crearse)

    def crearse(self):
        singup.Creperfil()
        

    def entrando(self):
        usuario = self.usuario_log.text()
        contrasena= self.contrasena_log.text() 
        res, contrasenaveri = cb.validar(usuario)
        if res and contrasena == contrasenaveri:
            QMessageBox.information(self, "Inicio de sesión", "Inicio de sesión exitoso")
        else:
            QMessageBox.warning(self, "Inicio de sesión", "Nombre de usuario o contraseña incorrectos")



class Creusuario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        uic.loadUi('singup.ui', self)
        self.show()

        self.crear.clicked.connect(cb.crearusu)

    def creacion(self):
        email=self.inemail.text()
        contrasena=self.incontrasena.text()
        numcel=self.innumcel.text()

def main():
    app = QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()