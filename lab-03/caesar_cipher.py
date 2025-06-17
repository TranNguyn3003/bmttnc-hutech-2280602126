import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow  # Import class từ caesar.py
import requests

# Cấu hình đường dẫn đến thư mục platforms
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "C:/Users/ASUS/AppData/Local/Programs/Python/Python312/Lib/site-packages/PyQt5/Qt5/plugins/platforms"

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        plain = self.ui.textEdit.toPlainText().strip()
        key_str = self.ui.textEdit_2.toPlainText().strip()
        if not plain or not key_str.isdigit():
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập Plain Text và Key là số nguyên!")
            return
        payload = {
            "plain_text": plain,
            "key": key_str
        }
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response content:", response.text)
            if response.status_code == 200:
                data = response.json()
                print("Response data:", data)
                self.ui.textEdit_3.setText(data["encrypt_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error while calling API")
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        cipher = self.ui.textEdit_3.toPlainText().strip()
        key_str = self.ui.textEdit_2.toPlainText().strip()
        if not cipher or not key_str.isdigit():
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập CipherText và Key là số nguyên!")
            return
        payload = {
            "cipher_text": cipher,
            "key": key_str
        }
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response content:", response.text)
            if response.status_code == 200:
                data = response.json()
                print("Response data:", data)
                self.ui.textEdit.setText(data["decrypt_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error while calling API")
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())