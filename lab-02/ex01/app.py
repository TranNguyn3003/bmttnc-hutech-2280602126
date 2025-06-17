from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

# Route cho trang chính
@app.route('/')
def home():
    return render_template('index.html')

# Route cho trang Caesar Cipher
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

# Route cho trang Rail Fence Cipher
@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

# Route cho trang Vigenere Cipher
@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

# Route cho trang Playfair Cipher
@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

# Route để mã hóa (encrypt)
@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    referer = request.headers.get('Referer', '')
    if 'caesar' in referer:
        cipher = CaesarCipher()
        key = int(key)
        result = cipher.encrypt_text(text, key)
    elif 'railfence' in referer:
        cipher = RailFenceCipher()
        key = int(key)
        result = cipher.rail_fence_encrypt(text, key)
    elif 'vigenere' in referer:
        cipher = VigenereCipher()
        result = cipher.vigenere_encrypt(text, key)
    elif 'playfair' in referer:
        cipher = PlayfairCipher()
        matrix = cipher.create_playfair_matrix(key)
        result = cipher.playfair_encrypt(text, matrix)
    else:
        return "Invalid cipher type"
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {result}"

# Route để giải mã (decrypt)
@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    referer = request.headers.get('Referer', '')
    if 'caesar' in referer:
        cipher = CaesarCipher()
        key = int(key)
        result = cipher.decrypt_text(text, key)
    elif 'railfence' in referer:
        cipher = RailFenceCipher()
        key = int(key)
        result = cipher.rail_fence_decrypt(text, key)
    elif 'vigenere' in referer:
        cipher = VigenereCipher()
        result = cipher.vigenere_decrypt(text, key)
    elif 'playfair' in referer:
        cipher = PlayfairCipher()
        matrix = cipher.create_playfair_matrix(key)
        result = cipher.playfair_decrypt(text, matrix)
    else:
        return "Invalid cipher type"
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {result}"

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)