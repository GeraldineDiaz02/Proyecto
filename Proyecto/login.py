import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import  uic
import consultarbase as cb

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
        res = cb.validar(texto1)
        print(res)
    

# class Creperfil(PyQT.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initGui()

#     def initGui(self):
#         uic.loadUi('createuser.ui', self)
#         self.show()

#         self.registrar.clicked.connect(cb.registrar)

#     def registro(self):
#         nombre = self.innombre.text()
#         fechana = self.innacimiento.text()
        
#         if self.woman.isChecked():
#             self.genero.setText(str('f'))
#         else:
#             self.genero.setText(str('m'))
        
#         intereses = self.inintereses.text()
#         descripcion = self.indescripcion.text()
#         profesion = self.inprofesiones.text()
#         inworkarea = self.indescripcion.text()

# class Creusuario(PyQT.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initGui()

#     def initGui(self):
#         uic.loadUi('singup.ui', self)
#         self.show()

#         self.crear.clicked.connect(cb.crearusu)

#     def creacion(self):
#         email=self.inemail.text()
#         contrasena=self.incontrasena.text()
#         numcel=self.innumcel.text()

def main():
    app=PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
#select nombre,edad from usuarios where nombre=juan and edad=27
