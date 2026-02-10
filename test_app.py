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

        # VLC
        layout_vlc = QHBoxLayout()
        label_vlc = QLabel("Darknet YOLO")
        layout_vlc.addWidget(label_vlc)
        btn_vlc = QPushButton("Abrir Deteccion")
        btn_vlc.clicked.connect(self.abrir_vlc)
        layout_vlc.addWidget(btn_vlc)
        layout_principal.addLayout(layout_vlc)


  



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
        	subprocess.Popen(["bash", "/home/cicy2024/detecciones/deteccion_humanos2.sh"]
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
    app.setStyle("Windows")
    ventana = VentanaScripts()
    ventana.show()
    sys.exit(app.exec_())
