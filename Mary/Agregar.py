#Mostrar los datos del perfil, agregar perfiles o amigos y busqueda de esos perfiles o amigos para agregarlos.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QPoint, QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
import sqlite3


class Principal(QMainWindow):
    def __init__(self): 
        super(Principal, self).__init__()
        loadUi('interfaz_dinamica.ui',self)

        self.conexion = sqlite3.connect('BSEUSUARIOS.s3db')
        
        self.show()

        # Barra de titulo
        self.click_posicion = QPoint()
        #self.bt_perfil.clicked.connect(self.abrir_pestaña_superior)
        #self.bt_inicio.clicked.connect(self.volver_al_inicio)

        ## Botones
        #self.bt_actualizar.clicked.connect(self.refrescar)
        #self.bt_agregar.clicked.connect(self.agregar_amigos)
        self.bt_actualizar.clicked.connect(self.mostrar_datos)
        self.bt_search.clicked.connect(self.buscar_perfiles)

        ## Coneccion botones para acceder a las paginas
        self.bt_mas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))
        self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_perfil))
       
        # Mover el menu lateral izquiedo
        self.bt_menu.clicked.connect(self.mover_menu)
        self.frame_superior.mouseMoveEvent = self.mover_menu

        # Mover el menu lateral derecho
        self.bt_perfil.clicked.connect(self.mover_perfil)
        self.frame_superior.mouseMoveEvent = self.mover_perfil

        ## Crear widgets
        self.result_layout = QVBoxLayout()
        self.agregar_layout = QVBoxLayout()

        ## Crear el layout principal y el widget contenedor
        self.main_layout = QVBoxLayout()

        # Asignar un layout al frame_menu
        self.frame_menu.setLayout(QVBoxLayout())

        #Lista amigos
        self.perfiles_agregados = []

    def mover_menu(self):
        if True:
            width = self.frame_menu.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_menu, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def mover_perfil(self):
         if True:
            width = self.frame_perfiles.width()
            normal = 0
            if width == 0:
                alargar = 120
            else:
                alargar = normal
            self.animacion = QPropertyAnimation(self.frame_perfiles, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(alargar)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()


    def mostrar_datos(self, nombre):
        self.stackedWidget.setCurrentWidget(self.page_perfil)
        n=nombre
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM Perfiles WHERE nombre = '{}'".format(n))
        perfil = cursor.fetchall()
        cursor.close()
        if perfil:
            self.nombre.setText(f'{perfil[0][0]}')
            self.profesion.setText(f'{perfil[0][5]}')
            self.resena.setText(f'{perfil[0][4]}')
            self.birthdate.setText(f'{perfil[0][1]}')
            self.gender.setText(f'{perfil[0][2]}')
            self.interests.setText(f'{perfil[0][3]}')
            self.workarea.setText(f'{perfil[0][6]}')

            # Limpiar el layout actual de frame_agregar
            self.clear_agregar_layout()

            # Crear y mostrar el botón "Agregar" en el frame_agregar
            agregar_button = QPushButton("Agregar")
            agregar_button.clicked.connect(lambda _, n=nombre: self.agregar_amigos(n))
            self.agregar_layout.addWidget(agregar_button)

            # Asignar el layout al frame_agregar
            self.frame_agregar.setLayout(self.agregar_layout)

        else:
            self.nombre.setText(f'none')
            self.resena.setText(f'None')
            self.birthdate.setText(f'None')
            self.gender.setText(f'None')
            self.interests.setText(f'None')
            self.workarea.setText(f'None')
            
    def buscar_perfiles(self):
        termino_busqueda = self.line_busqueda.text()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, profesion FROM Perfiles WHERE profesion = '{}'".format(termino_busqueda))
        perfiles = cursor.fetchall()
        cursor.close()
    
        self.clear_results()  # Limpiar resultados anteriores
    
        if perfiles:
            self.result_layout = QVBoxLayout()  # Crear un nuevo QVBoxLayout
    
            for perfil in perfiles:
                nombre = perfil[0]
                profesion = perfil[1]

                perfil_button = QPushButton(f"{nombre} / {profesion}")
                perfil_button.clicked.connect(lambda _, n=nombre: self.mostrar_datos(n))  # Conectar la señal clicked al método mostrar_datos
                perfil_button.clicked.connect(lambda _, n1=nombre: self.agregar_amigos(n1))  # Conectar la señal clicked al método mostrar_datos
                self.result_layout.addWidget(perfil_button)

        else:
            perfil_label = QLabel(f"No results found")
            perfil_label.setText("No results found")
            self.result_layout.addWidget(perfil_label)
            
        self.main_layout.addLayout(self.result_layout)  # Agregar el layout de resultados al layout principal
        self.perfiles.setLayout(self.main_layout)  # Establecer el layout principal en el QFrame    

    def clear_results(self):
    # Limpiar los resultados anteriores del layout
        while self.result_layout.count():
            item = self.result_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def agregar_amigos(self, nombre):
        n = nombre

        self.clear_agregar_layout()

        # Crear el botón "AGREGAR(+)"
        amigo_button = QPushButton("AGREGAR(+)")
        amigo_button.clicked.connect(lambda _, n2=n: self.amigo_button(n2))
        self.agregar_layout.addWidget(amigo_button)

        # Asignar el layout al frame_agregar
        self.frame_agregar.setLayout(self.agregar_layout)

    def amigo_button(self, nombre):
        n = nombre

        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, profesion FROM Perfiles WHERE nombre = '{}'".format(n))
        amigo = cursor.fetchall()
        cursor.close()

        if n not in self.perfiles_agregados:
            self.perfiles_agregados.append(n)

            self.clear_agregar_layout()

            for agregando in amigo:
                nombre = agregando[0]
                profesion = agregando[1]

                # Crear el botón del perfil para agregar al frame_menu
                perfil_button = QPushButton(f"{nombre} \n {profesion}")
                perfil_button.clicked.connect(lambda _, n=nombre: self.mostrar_datos(n))
                self.agregar_layout.addWidget(perfil_button)

                # Agregar el botón de amigo al layout de frame_menu
                self.frame_menu.layout().addWidget(perfil_button)

    def clear_agregar_layout(self):
        # Limpiar los widgets anteriores del layout de agregar
        while self.agregar_layout.count():
            item = self.agregar_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

def main():
    app = QApplication(sys.argv)
    my_app = Principal()
    my_app.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()