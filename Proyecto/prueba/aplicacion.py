import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import  uic

class Principal(PyQT.QMainWindow):
    def __init__(self): 
        super().__init__()
        self.initGui()
    
    def initGui(self):
        uic.loadUi("loginInterfaz.ui",self)
        self.show()

        self.entrar.clicked.connect(self.calcular)

    def calcular(self):
        texto1=self.usuario_log.text()
        print(texto1) 


def main():
    app=PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
