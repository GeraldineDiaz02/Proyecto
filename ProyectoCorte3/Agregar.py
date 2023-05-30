#Mostrar los datos del perfil, agregar perfiles o amigos y busqueda de esos perfiles o amigos para agregarlos.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import QPoint, QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
import help_create as hc
import sqlite3




class MostrarPerfil(QMainWindow):
    def __init__(self): 
        super(MostrarPerfil, self).__init__()
        loadUi('interfaz_dinamica.ui',self)

        self.conexion = sqlite3.connect('BSEUSUARIOS.s3db')

        self.ultimo_perfil = ""
        
        self.show()

        # Barra de titulo
        self.click_posicion = QPoint()
        #self.bt_perfil.clicked.connect(self.abrir_pestaña_superior)
        

        ## Botones
        #self.bt_actualizar.clicked.connect(self.refrescar)
        #self.bt_agregar.clicked.connect(self.agregar_amigos)
        self.bt_actualizar.clicked.connect(self.mostrar_datos)
        self.bt_search.clicked.connect(self.buscar_perfiles)
        self.bt_inicio.clicked.connect(self.mostrar_ultimo_perfil)
        self.bt_settings.clicked.connect(self.configuracion)
        self.bt_help.clicked.connect(self.openhelp)
    

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
        
    


        
    def configuracion(self):
        view = hc.hola()
        view.show()  
      

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
            
    def get_ultimo_perfil(self):
        return self.ultimo_perfil

    def mostrar_ultimo_perfil(self):
        self.mostrar_datos(self.ultimo_perfil)
        self.ultimo_perfil = ""

    def mostrar_datos(self, nombre):
        self.stackedWidget.setCurrentWidget(self.page_perfil)
        n=nombre
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM Registros WHERE Nombre = '{}'".format(n))
        perfil = cursor.fetchall()
        cursor.close()

        if perfil:
            self.nombre.setText(f'{perfil[0][1]}')
            self.profesion.setText(f'{perfil[0][6]}')
            self.resena.setText(f'{perfil[0][5]}')
            self.birthdate.setText(f'{perfil[0][2]}')
            self.gender.setText(f'{perfil[0][3]}')
            self.interests.setText(f'{perfil[0][4]}')
            self.workarea.setText(f'{perfil[0][7]}')

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
        cursor.execute("SELECT Nombre, profesion FROM Registros WHERE profesion = '{}'".format(termino_busqueda))
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
        cursor.execute("SELECT Nombre, profesion FROM Registros WHERE nombre = '{}'".format(n))
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
    def openhelp(self):
        self.ayuda = Ayuda()
        self.ayuda.show()

class Ayuda(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()

        self.testseguridad.clicked.connect(self.informacionseguridad)
        self.recomendaciones.clicked.connect(self.informacionrecomendaciones)
        self.denuncias.clicked.connect(self.informaciondenuncias)
        self.bloquear.clicked.connect(self.informacionbloquear)
        #self.volver.clicked.connect(self.regresar)
    
    def load_ui(self):
        ui_file = "ayuda.ui"
        loadUi(ui_file, self)
        self.showNormal()

    def informacionseguridad(self):
        informacion = "Seguridad:\n\n" \
                      "Consejos para mantener la cuenta segura:\n\n\n" \
                      "  - Utiliza contraseñas seguras: Crea contraseñas fuertes que contengan una combinación de letras mayúsculas y minúsculas, números y símbolos. Evita usar contraseñas obvias o información personal fácilmente deducible.\n" \
                      "  - No compartas información personal: Evita compartir información personal sensible, como tu dirección, número de teléfono o datos bancarios, en tu perfil o en publicaciones públicas. Mantén tu información personal protegida y solo compártela con personas de confianza.\n" \
                      "  - Configura adecuadamente la privacidad de tu cuenta: Revisa y ajusta la configuración de privacidad de tu cuenta de acuerdo con tus preferencias. Limita quién puede ver tus publicaciones y qué información personal está disponible para otros usuarios.\n" \
                      "  - Sé cauteloso al hacer clic en enlaces o descargar archivos: No hagas clic en enlaces sospechosos o desconocidos, y evita descargar archivos adjuntos de fuentes no confiables. Podrían contener malware o ser utilizados para obtener acceso no autorizado a tu cuenta.\n" \
                      "  - Mantén el software actualizado: Asegúrate de tener instaladas las últimas actualizaciones de seguridad tanto para tu sistema operativo como para la aplicación de la red social. Las actualizaciones suelen incluir parches de seguridad que protegen contra vulnerabilidades conocidas.\n" \
                      "  - Ten cuidado con las solicitudes de amistad o mensajes de desconocidos: No aceptes solicitudes de amistad o interactúes con perfiles sospechosos o desconocidos. Algunos usuarios malintencionados pueden intentar obtener acceso a tu cuenta o información personal a través de engaños o estafas.\n" \
                      "  - Aprende a reconocer y reportar contenido inapropiado: Familiarízate con las políticas de la red social y aprende a reconocer contenido inapropiado, como acoso, discriminación o violencia. Si encuentras contenido o comportamientos que violen las normas de la plataforma, repórtalos adecuadamente para ayudar a mantener un entorno seguro.\n" \
                      "\n\n\n" \
                      "Explicación sobre las opciones de privacidad y cómo ajustarlas según las preferencias del usuario:\n\n\n" \
                      "- Configuración de privacidad del perfil: Esta opción te permite controlar quién puede ver la información de tu perfil, como tu foto de perfil, nombre, biografía y lista de amigos. Puedes elegir entre opciones como 'Público' (visible para todos), 'Amigos' (visible solo para tus amigos) o 'Solo yo' (visible solo para ti). Ajusta esta configuración según tu nivel de comodidad y la cantidad de información que deseas compartir.\n" \
                      "- Privacidad de las publicaciones: Puedes controlar quién puede ver tus publicaciones en la red social. Puedes configurarlas para que sean visibles para todos, solo tus amigos o incluso personalizar la visibilidad para grupos específicos. También puedes limitar quién puede comentar en tus publicaciones o quién puede etiquetarte en fotos. Asegúrate de revisar y ajustar estas configuraciones de privacidad según tus preferencias.\n" \
                      "- Privacidad de las fotos y álbumes: Las redes sociales suelen ofrecer opciones para controlar la privacidad de tus fotos y álbumes. Puedes decidir quién puede ver tus fotos, ya sea público, solo amigos o un grupo selecto de personas. También puedes configurar la opción de aprobación de etiquetas, lo que significa que debes aprobar manualmente las etiquetas antes de que aparezcan en tu perfil. Ajusta estas opciones para proteger tu privacidad y controlar quién puede acceder a tus imágenes.\n" \
                      "- Control de la visibilidad de tu actividad: Algunas redes sociales permiten controlar la visibilidad de tu actividad, como los comentarios que realizas, las páginas que te gustan o los eventos a los que asistes. Puedes elegir si deseas que esta actividad sea visible para todos, solo amigos o mantenerla privada. Asegúrate de revisar estas configuraciones y ajustarlas según tus preferencias de privacidad.\n"

        QMessageBox.information(self, "Información de seguridad", informacion)

    def informacionrecomendaciones(self):
        informacion = "Recomendaciones: \n\n" \
                      "-Protege tu información personal: Evita compartir información personal sensible, como tu dirección, número de teléfono o datos bancarios, en tu perfil o en publicaciones públicas. Mantén tu información personal protegida y solo compártela con personas de confianza. \n" \
                      "-Utiliza contraseñas seguras: Crea contraseñas fuertes que contengan una combinación de letras mayúsculas y minúsculas, números y símbolos. Evita usar contraseñas obvias o información personal fácilmente deducible. Además, asegúrate de utilizar contraseñas diferentes para cada una de tus cuentas en redes sociales. \n " \
                      "-Configura adecuadamente la privacidad de tu cuenta: Revisa y ajusta la configuración de privacidad de tu cuenta de acuerdo con tus preferencias. Limita quién puede ver tus publicaciones y qué información personal está disponible para otros usuarios. Utiliza las opciones de privacidad proporcionadas por la red social para controlar quién puede acceder a tu perfil y contenido. \n" \
                      "-Sé selectivo con las amistades: No aceptes solicitudes de amistad o interactúes con perfiles sospechosos o desconocidos. Algunos usuarios malintencionados pueden intentar obtener acceso a tu cuenta o información personal a través de engaños o estafas. Asegúrate de conocer a las personas con las que interactúas en línea y de que sean de confianza.\n" \
                      "-Aprende a reconocer contenido inapropiado: Familiarízate con las políticas de la red social y aprende a reconocer contenido inapropiado, como acoso, discriminación o violencia. Si encuentras contenido o comportamientos que violen las normas de la plataforma, repórtalos adecuadamente para ayudar a mantener un entorno seguro. \n" \
                      "-Sé consciente de tu reputación en línea: Recuerda que lo que compartes en las redes sociales puede tener un impacto en tu vida personal y profesional. Piensa antes de publicar y considera cómo tus publicaciones pueden afectar tu reputación. Evita compartir información comprometedora o irresponsable que pueda perjudicarte a largo plazo. \n" \
                      "-Interactúa de manera respetuosa: Trata a los demás usuarios con cortesía y respeto. Evita el acoso, los comentarios ofensivos o discriminatorios, y las discusiones agresivas. Promueve un ambiente positivo y constructivo en tus interacciones en línea. \n" \
                      "-Controla tus ajustes de notificación: Configura tus notificaciones de manera que se adapten a tus preferencias y necesidades. Recibir demasiadas notificaciones puede ser abrumador y distraerte. Ajusta tus preferencias de notificación para que te mantengas informado sin que afecte negativamente tu productividad o bienestar. \n" 
        QMessageBox.information(self, "Recomendaciones", informacion)

    def informaciondenuncias(self):
        informacion = "Denuncias \n\n"\
                    "En nuestra red social, nos comprometemos a mantener un entorno seguro y respetuoso para todos nuestros usuarios. Si encuentras contenido o comportamientos que violen nuestras normas comunitarias, te alentamos a utilizar nuestra función de denuncia para informarnos sobre ello. Las denuncias nos ayudan a tomar medidas adecuadas y garantizar que nuestra plataforma sea un lugar seguro para todos. \n\n\n" \
                    "¿Qué se puede denunciar? \n\n" \
                    "-Puedes denunciar diferentes tipos de contenido o comportamientos que consideres inapropiados o que violen nuestras políticas. Algunos ejemplos comunes de lo que se puede denunciar incluyen: \n" \
                    "-Contenido ofensivo: Esto puede incluir publicaciones, comentarios, mensajes privados o perfiles que contengan lenguaje abusivo, discriminación, acoso, contenido violento o cualquier forma de contenido inapropiado. \n" \
                    "-Comportamiento de acoso: Si estás experimentando acoso por parte de otro usuario, ya sea a través de mensajes, comentarios o cualquier otra forma de interacción en nuestra plataforma, te alentamos a denunciarlo para que podamos tomar las medidas necesarias. \n" \
                    "-Spam o contenido no deseado: Si encuentras contenido no deseado, como publicaciones o mensajes que promocionen productos o servicios de manera no autorizada, puedes denunciarlo para ayudarnos a mantener nuestra red libre de spam. \n" \
                    "-Cuentas falsas o de suplantación de identidad: Si sospechas que una cuenta está utilizando información falsa o está suplantando la identidad de otra persona, puedes denunciarla para que podamos investigar y tomar las medidas necesarias. \n\n\n" \
                    "¿Cómo hacer una denuncia? \n\n" \
                    "Para realizar una denuncia, sigue estos pasos: \n" \
                    "-Encuentra el contenido o perfil que deseas denunciar. \n" \
                    "-Haz clic en el botón de denuncia que generalmente se encuentra junto al contenido o en el perfil del usuario. \n" \
                    "-Selecciona el motivo de la denuncia en función de las opciones proporcionadas. Si no encuentras una opción específica, puedes seleccionar ""Otro"" y proporcionar detalles adicionales. \n" \
                    "-Proporciona cualquier información adicional relevante que pueda ayudarnos a comprender mejor la situación, como capturas de pantalla o descripciones detalladas. \n" \
                    "-Envía la denuncia y nuestro equipo de moderación la revisará lo antes posible. \n" 
        
        QMessageBox.information(self, "Denuncias", informacion)

    def informacionbloquear(self):
        informacion = "Bloqueo y reporte \n\n\n"\
                    "En nuestra red social, nos preocupamos por tu seguridad y bienestar. Entendemos que en ocasiones puedes encontrarte con contenido o usuarios que consideres inapropiados o que violen nuestras políticas. Por eso, te ofrecemos las opciones de bloquear y reportar para que puedas tomar medidas y mantener un entorno positivo en nuestra plataforma. \n\n\n" \
                    "Bloquear a un usuario: \n\n" \
                    "-Si encuentras a un usuario que te resulta molesto, ofensivo o no deseas interactuar con él, puedes utilizar la función de bloqueo. Cuando bloqueas a un usuario, se eliminará su capacidad para comunicarse contigo y ver tu perfil. Los pasos para bloquear a un usuario son los siguientes: \n" \
                    "-Accede al perfil del usuario que deseas bloquear. \n" \
                    "-Busca la opción ""Bloquear"" o un icono similar. \n" \
                    "-Confirma tu decisión de bloquear al usuario. \n" \
                    "-Una vez bloqueado, el usuario no podrá enviarte mensajes, realizar comentarios en tus publicaciones ni ver tus actualizaciones. \n\n\n" \
                    "Reportar contenido inapropiado: \n\n" \
                    "-Si encuentras contenido que consideras inapropiado, ofensivo, acosador o que viola nuestras políticas, te animamos a que lo denuncies para que podamos revisarlo y tomar las medidas correspondientes. El proceso de reporte es sencillo: \n" \
                    "-Encuentra el contenido ofensivo que deseas reportar. \n" \
                    "-Busca la opción ""Reportar"" o un icono similar. \n" \
                    "-Selecciona el motivo de tu reporte en función de las opciones proporcionadas. Si no encuentras una opción adecuada, elige ""Otro"" y proporciona detalles adicionales. \n" \
                    "-Proporciona cualquier información adicional relevante que pueda ayudarnos a entender la situación. \n" \
                    "-Envía el reporte y nuestro equipo de moderación lo revisará en breve. \n\n\n" \
                    "Recuerda que tomamos en serio cada reporte y tratamos la información de manera confidencial. Tu contribución es esencial para mantener nuestra comunidad segura y libre de contenido inapropiado.\n" \
                    "Te agradecemos por tu colaboración y por ayudarnos a mantener un entorno positivo y respetuoso en nuestra red social.\n"
        QMessageBox.information(self, "Bloqueo y reporte", informacion)



def main():
    app = QApplication(sys.argv)
    my_app = MostrarPerfil()
    my_app.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()