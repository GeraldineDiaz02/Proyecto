import sys
import PyQt5.QtWidgets as PyQT
from PyQt5.QtCore import Qt
from PyQt5 import uic
from Agregar import Principal

class Help_create(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        uic.loadUi('createuser.ui',self)
        self.show()
        self.perfil.clicked.connect(lambda:self.perfilview())
        self.contact_info.clicked.connect(lambda:self.perfilview())
        self.opciones.clicked.connect(lambda:self.volver())  
    def perfilview(self):
        view=Principal()
        view.show()
    def volver(self):
        viewtwo=Help_create()
        viewtwo.show()
        
class Sett_singup(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initSett()
    def initSett(self):
        uic.loadUi('singup.ui',self)
        self.show()
        self.perfil.clicked.connect(lambda:self.perfilsett())
        self.comentar.clicked.connect(lambda:self.commentsett())
    def perfilsett(self):
        ver=Principal()
        ver.show
    def commentsett(self):
        x=self.coment0.text()
        
        self.comentario.setText(x)




def main():
    app = PyQT.QApplication([])
    window = Sett_singup()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()