import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import consultarbase as cb
import login

class Creperfil(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        uic.loadUi('createuser.ui', self)
        self.show()

        self.registrar.clicked.connect(cb.registrar)

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
    app = QApplication([])
    window = Creperfil()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()