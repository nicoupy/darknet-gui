#!/usr/bin/env python3
"""
PyQt5 Control Interface for Human Detection System
Provides GUI controls for starting and stopping Darknet-based human detection
"""

import sys
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QVBoxLayout, QWidget, QLabel, QTextEdit,
                             QHBoxLayout, QFrame)
from PyQt5.QtCore import Qt, QProcess
from PyQt5.QtGui import QFont, QPalette, QColor


class DetectionController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.process = None
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle('Human Detection Control Panel')
        self.setGeometry(100, 100, 600, 500)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Title
        title = QLabel('🎯 Human Detection System')
        title.setFont(QFont('Arial', 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #2c3e50; padding: 10px;")
        main_layout.addWidget(title)
        
        # Separator
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)
        
        # Status label
        self.status_label = QLabel('Status: Ready')
        self.status_label.setFont(QFont('Arial', 12))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
            color: #2c3e50;
        """)
        main_layout.addWidget(self.status_label)
        
        # Buttons layout
        button_layout = QHBoxLayout()
        
        # Start Detection Button
        self.start_btn = QPushButton('▶ Start Detection')
        self.start_btn.setFont(QFont('Arial', 12, QFont.Bold))
        self.start_btn.setMinimumHeight(60)
        self.start_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
            QPushButton:pressed {
                background-color: #1e8449;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        """)
        self.start_btn.clicked.connect(self.start_detection)
        button_layout.addWidget(self.start_btn)
        
        # Stop Detection Button
        self.stop_btn = QPushButton('⏹ Stop Detection')
        self.stop_btn.setFont(QFont('Arial', 12, QFont.Bold))
        self.stop_btn.setMinimumHeight(60)
        self.stop_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        """)
        self.stop_btn.clicked.connect(self.stop_detection)
        self.stop_btn.setEnabled(False)
        button_layout.addWidget(self.stop_btn)
        
        main_layout.addLayout(button_layout)
        
        # Output/Log display
        log_label = QLabel('System Output:')
        log_label.setFont(QFont('Arial', 10, QFont.Bold))
        main_layout.addWidget(log_label)
        
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFont(QFont('Courier', 9))
        self.output_text.setStyleSheet("""
            background-color: #2c3e50;
            color: #ecf0f1;
            border-radius: 5px;
            padding: 5px;
        """)
        main_layout.addWidget(self.output_text)
        
        # Info label
        info = QLabel('ℹ️ Using Darknet YOLO for real-time human detection')
        info.setFont(QFont('Arial', 9))
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("color: #7f8c8d; padding: 5px;")
        main_layout.addWidget(info)
        
        self.log_message("System initialized and ready")
        
    def log_message(self, message):
        """Add a message to the output log"""
        self.output_text.append(f"[INFO] {message}")
        
    def start_detection(self):
        """Start the human detection script"""
        self.log_message("Starting human detection system...")
        self.status_label.setText('Status: Running Detection')
        self.status_label.setStyleSheet("""
            background-color: #2ecc71;
            padding: 10px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        """)
        
        try:
            # Run the detection script
            result = subprocess.Popen(
                ['bash', '/home/cicy2024/detecciones/deteccion_humanos2.sh'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            
            self.log_message(f"Detection process started (PID: {result.pid})")
            self.log_message("Darknet YOLO is now analyzing video feed...")
            
            # Update button states
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            
        except Exception as e:
            self.log_message(f"ERROR: Failed to start detection - {str(e)}")
            self.status_label.setText('Status: Error')
            self.status_label.setStyleSheet("""
                background-color: #e74c3c;
                padding: 10px;
                border-radius: 5px;
                color: white;
                font-weight: bold;
            """)
            
    def stop_detection(self):
        """Stop the human detection script"""
        self.log_message("Stopping detection system...")
        self.status_label.setText('Status: Stopping...')
        self.status_label.setStyleSheet("""
            background-color: #f39c12;
            padding: 10px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        """)
        
        try:
            # Run the kill script
            result = subprocess.run(
                ['bash', '/home/cicy2024/detecciones/kill.sh'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            self.log_message("Detection processes terminated")
            self.log_message("System stopped successfully")
            
            # Update UI
            self.status_label.setText('Status: Ready')
            self.status_label.setStyleSheet("""
                background-color: #ecf0f1;
                padding: 10px;
                border-radius: 5px;
                color: #2c3e50;
            """)
            
            # Update button states
            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)
            
        except Exception as e:
            self.log_message(f"ERROR: Failed to stop detection - {str(e)}")
            self.status_label.setText('Status: Error')
            self.status_label.setStyleSheet("""
                background-color: #e74c3c;
                padding: 10px;
                border-radius: 5px;
                color: white;
                font-weight: bold;
            """)
            

def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show the main window
    window = DetectionController()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
