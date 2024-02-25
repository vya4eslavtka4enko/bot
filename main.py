import sys
from backend import Chatbot
from PyQt6.QtWidgets import QGridLayout,QMainWindow,QTextEdit,QLineEdit,QPushButton,QApplication

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()
        self.setMinimumSize(700,500)

        #Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)

        #Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 30)

        #Add the button
        self.button = QPushButton("Send",self)
        self.button.setGeometry(10, 370, 480, 60)
        self.button.clicked.connect(self.send_message)
        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me:{user_input}")

        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f'Bot:{response}')

app=QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())