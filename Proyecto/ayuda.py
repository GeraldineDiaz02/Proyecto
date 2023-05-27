import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class Ayuda(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.show()

        self.testseguridad.clicked.connect(self.informacionseguridad)
        self.recomendaciones.clicked.connect(self.informacionseguridad)
        self.denuncias.clicked.connect(self.informaciondenuncias)
        self.bloquear.clicked.connect(self.informacionbloquear)
        self.volver.clicked.connect(self.regresar)
    
    def load_ui(self):
        ui_file = "ayuda.ui"
        loadUi(ui_file, self)
        self.setWindowTitle(self.windowTitle())

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

    def regresar(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ayuda()
    sys.exit(app.exec_())
