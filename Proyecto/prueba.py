import sys
import PyQt5.QtWidgets as PyQT
from PyQt5.QtCore import Qt
from PyQt5 import uic
import consultarbase as cb

class Logearse(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        uic.loadUi('loginInterfaz.ui', self)
        self.show()

        self.entrar.clicked.connect(cb.validar)

class Creusuario(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        uic.loadUi('createuser.ui', self)
        self.show()

        self.registrar.clicked.connect(self.registro)

    def registro(self):
        nombre = self.innombre.text()
        fechana = self.innacimiento.text()
        
        if self.woman.isChecked():
            self.genero.setText(str('f'))
        else:
            self.genero.setText(str('m'))
        
        intereses = self.inintereses.text()
        descripcion = self.indescripcion.text()
        profesion = self.inprofesiones.text()
        inworkarea = self.indescripcion.text()

def main():
    app = PyQT.QApplication([])
    window = Logearse()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()