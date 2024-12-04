import socket
from puffin_cipher import encrypt, decrypt  # Ensure to save PUFFIN code in a module named puffin_cipher

def server():
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    master_key = 0x0123456789ABCDEF0123456789ABCDEF

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # Receive encrypted data from client
                encrypted_data = conn.recv(1024)
                if not encrypted_data:
                    break

                # Decrypt the data
                decrypted_message = decrypt(encrypted_data, master_key).decode()
                print(f"Client: {decrypted_message}")

                # Send an encrypted response
                response = input("Server: ")
                encrypted_response = encrypt(response.encode(), master_key)
                conn.sendall(encrypted_response)

if __name__ == "__main__":
    server()
