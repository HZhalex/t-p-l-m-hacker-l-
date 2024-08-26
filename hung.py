def initialize_sbox(key):
    # Khởi tạo S-box (state box) với các giá trị từ 0 đến 255
    sbox = list(range(256))
    j = 0
    key_length = len(key)

    # Hoán đổi giá trị trong S-box dựa trên khóa
    for i in range(256):
        j = (j + sbox[i] + key[i % key_length]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]

    return sbox

def generate_key_stream(sbox, data_length):
    # Tạo key stream từ S-box
    i = j = 0
    key_stream = []

    for _ in range(data_length):
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]

        # Tính toán giá trị key stream từ S-box
        key_byte = sbox[(sbox[i] + sbox[j]) % 256]
        key_stream.append(key_byte)

    return key_stream

def rc4(key, data):
    # Khởi tạo S-box với khóa
    sbox = initialize_sbox(key)

    # Tạo key stream
    key_stream = generate_key_stream(sbox, len(data))

    # Mã hóa dữ liệu bằng cách XOR với key stream
    encrypted_data = [byte ^ key_stream[i] for i, byte in enumerate(data)]

    return encrypted_data

# Ví dụ sử dụng
key = [0x01, 0x23, 0x45, 0x67, 0x89]  # Đây là một khóa ví dụ 40-bit
iv = [0x12, 0x34, 0x56]  # Đây là một IV ví dụ 24-bit
data_to_encrypt = [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]  # Đây là dữ liệu ví dụ

# Ghép IV vào khóa để tạo khóa WEP
wep_key = key + iv

# Mã hóa dữ liệu sử dụng RC4
encrypted_data = rc4(wep_key, data_to_encrypt)

# In kết quả
print("Dữ liệu ban đầu:", data_to_encrypt)
print("Dữ liệu đã mã hóa:", encrypted_data)
