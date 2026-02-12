import sys
#import signal
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QStyle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class VentanaScripts(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Detección en Visión Artificial")
        self.setGeometry(200, 200, 400, 200)

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

        #Texto primer paso
        texto_pasouno = QLabel("Aplicacion de prueba para ejecutar darknet yolo cuda cudnn opencv dnn gpu")
        texto_pasouno.setWordWrap(True)
        #texto_pasouno.setAlignment(Qt.AlignCenter)
        texto_pasouno.setStyleSheet("""
            font-size: 15px;
        """)
        layout_principal.addWidget(texto_pasouno)

        # darknet1
        layout_darknet1 = QHBoxLayout()
        label_darknet1 = QLabel("Darknet YOLO")
        layout_darknet1.addWidget(label_darknet1)
        btn_darknet1 = QPushButton("Abrir Deteccion")
        btn_darknet1.clicked.connect(self.deteccion_personas)
        layout_darknet1.addWidget(btn_darknet1)
        layout_principal.addLayout(layout_darknet1)

        # kill darknet
        layout_kill = QHBoxLayout()
        label_kill = QLabel("Cerrar Detección")
        layout_kill.addWidget(label_kill)
        btn_kill = QPushButton("Kill Darknet")
        btn_kill.clicked.connect(self.terminar_proceso)
        layout_kill.addWidget(btn_kill)
        layout_principal.addLayout(layout_kill)

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

    def deteccion_personas(self):
        try:
            subprocess.Popen(["bash", "/home/cicy2024/detecciones/deteccion_humanos2.sh"])
        except Exception as e:
            print("Error al abrir Darknet:", e)
    def terminar_proceso(self):
        try:
            subprocess.Popen(["bash", "/home/cicy2024/detecciones/kill.sh"])
        except Exception as e:
            print("Error al terminar proceso:", e)

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
    app.setStyle("Windows")
    ventana = VentanaScripts()
    ventana.show()
    sys.exit(app.exec_())