def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def mds(message):
    # Khởi tạo các biến ban đầu
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length = len(message)
    message += b'\x80'  # Ký tự kết thúc
    while (len(message) * 8) % 64 != 56:
        message += b'\x00'  # Padding
    message += original_length.to_bytes(8, 'little')

    # Chia chuỗi thành các block 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        a0, b0, c0, d0 = a, b, c, d

        # Vòng lặp chính của thuật toán MD5
        for j in range(64):
            if j < 16:
                f = (b0 & c0) | ((~b0) & d0)
                g = j
            elif j < 32:
                f = (d0 & b0) | ((~d0) & c0)
                g = (5*j + 1) % 16
            elif j < 48:
                f = b0 ^ c0 ^ d0
                g = (3*j + 5) % 16
            else:
                f = c0 ^ (b0 | (~d0))
                g = (7*j) % 16

            temp = d0
            d0 = c0
            c0 = b0
            b0 = b0 + left_rotate((a0 + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)
            a0 = temp

        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = mds(input_string.encode('utf-8'))
print("Mã băm MDS của chuỗi '{}' là: {}".format(input_string, md5_hash))