import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat App GUI")
        self.setGeometry(300, 300, 400, 300)

        self.client_socket = None
        self.username = ""

        main_layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        main_layout.addWidget(self.chat_display)

        bottom_layout = QHBoxLayout()

        self.input_field = QLineEdit()
        bottom_layout.addWidget(self.input_field)

        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)
        bottom_layout.addWidget(send_button)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        self.start_client()

    def start_client(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 2169))

        self.username = input("Please enter a username for this chat session: ")

        receive_thread = threading.Thread(target=self.receive_message)
        receive_thread.start()

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                self.chat_display.append(message)
            except:
                break

    def send_message(self):
        message = self.input_field.text()
        if message:
            self.chat_display.append(f"You: {message}")
            self.client_socket.sendall(f"{self.username}: {message}".encode())
            self.input_field.clear()

    def closeEvent(self, event):
        if self.client_socket:
            self.client_socket.sendall("quit".encode())
            self.client_socket.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
