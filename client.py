import socket
from puffin_cipher import encrypt, decrypt  # Ensure to save PUFFIN code in a module named puffin_cipher

def client():
    host = '127.0.0.1'  # Server address
    port = 65432        # Server port

    master_key = 0x0123456789ABCDEF0123456789ABCDEF

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to the server.")
        while True:
            # Send an encrypted message
            message = input("Client: ")
            encrypted_message = encrypt(message.encode(), master_key)
            s.sendall(encrypted_message)

            # Receive encrypted response from server
            encrypted_response = s.recv(1024)
            if not encrypted_response:
                break

            # Decrypt the response
            decrypted_response = decrypt(encrypted_response, master_key).decode()
            print(f"Server: {decrypted_response}")

if __name__ == "__main__":
    client()
