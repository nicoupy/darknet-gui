import sys
#import signal
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class VentanaScripts(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Detección en Visión Artificial")
        self.setGeometry(600, 200, 400, 600)

        # Diccionario para almacenar los procesos de cada script
        self.procesos = {
            "deteccion_basura": None,
            "deteccion_humanos": None,
            "deteccion_pez_leon": None
        }

        # Layout principal vertical
        layout_principal = QVBoxLayout()


        #Titulo
        texto_informativo = QLabel("Detección en Visión Artificial")
        texto_informativo.setWordWrap(True)
        texto_informativo.setAlignment(Qt.AlignCenter)
        texto_informativo.setStyleSheet("""
            font-size: 20px;
            color: #333;
            padding: 10px;
            margin-bottom: 10px;

        """)

        layout_principal.addWidget(texto_informativo)

      


        #Texto segundo paso
        texto_pasodos = QLabel("2. Selecciona la detección que deseas aplicar:")
        texto_pasodos.setWordWrap(True)
        texto_pasodos.setStyleSheet("""
            font-size: 15px;
        """)
        layout_principal.addWidget(texto_pasodos)


        # Scripts
        layout_principal.addLayout(self.crearSeccion("Ejecutar darknet", "/home/cicy2024/detecciones/deteccion_humanos2.sh", "deteccion_humanos2"))
        layout_principal.addLayout(self.crearSeccion("Terminar proceso", "/home/cicy2024/detecciones/kill.sh", "deteccion_humanos"))
        layout_principal.addLayout(self.crearSeccion("Detección de pez león", "/home/cicy2024/detecciones/deteccion_pez_leon.sh", "deteccion_pez_leon"))

        #Texto manuales
        texto_manual = QLabel("Encuentra más información sobre las detecciones a continuación:")
        texto_manual.setWordWrap(True)
        texto_manual.setStyleSheet("""
            font-size: 15px;
        """)
        layout_principal.addWidget(texto_manual)

         # Manuales
        btn_abrir_carpeta = QPushButton("Manuales")
        btn_abrir_carpeta.clicked.connect(self.abrir_carpeta)
        layout_principal.addWidget(btn_abrir_carpeta)


        #Texto webcam
        texto_webcam =  QLabel("Aplicación de las detecciones desde una cámara web")
        texto_webcam.setWordWrap(True)
        texto_webcam.setStyleSheet("""
            font-size: 15px;
        """)
        layout_principal.addWidget(texto_webcam)

        # webcam
        btn_webcam = QPushButton("cámara web")
        btn_webcam.clicked.connect(self.app_webcam)
        layout_principal.addWidget(btn_webcam)

        #Texto salida
        texto_salida =  QLabel("Escriba 'Ctrl C' en la terminal para salir de la función de detección")
        texto_salida.setWordWrap(True)
        texto_salida.setStyleSheet("""
            font-size: 15px;
        """)
        layout_principal.addWidget(texto_salida)



        self.setLayout(layout_principal)
                
    
    def crearSeccion(self, nombre_script, ruta_script, clave):
        layout = QHBoxLayout()

        label = QLabel(nombre_script)
        layout.addWidget(label)

        btn_ejecutar = QPushButton("Ejecutar")
        btn_ejecutar.clicked.connect(lambda: self.ejecutar_script(ruta_script, clave))
        layout.addWidget(btn_ejecutar)

        return layout


    def ejecutar_script(self, ruta, clave):
        if self.procesos[clave] is None:
            try:
                self.procesos[clave] = subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"{ruta}; exec bash"])
                print(f"{clave} iniciado.")
            except Exception as e:
                print(f"Error al ejecutar {clave}: {e}")
        else:
            print(f"{clave} ya está en ejecución.")

    def abrir_vlc(self):
        try:
            subprocess.Popen(["vlc"])
            print("VLC abierto.")
        except Exception as e:
            print("Error al abrir VLC:", e)

    def abrir_carpeta(self):
        carpeta_path = "/home/cicy2024/detecciones/Manuales"

        try:
            subprocess.Popen(["xdg-open", carpeta_path])
            print("Manuales")
        except Exception as e:
            print(f"Error al abrir los manuales: {e}")
    
    def app_webcam(self):
        try:
            subprocess.Popen(["python3", "/home/cicy2024/detecciones/prot_app_webcam.py"])
            print("Script ejecutado")
        except Exception as e:
            print(f"Error al ejecutar el script: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ventana = VentanaScripts()
    ventana.show()
    sys.exit(app.exec_())
