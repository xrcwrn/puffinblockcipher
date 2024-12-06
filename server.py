import socket
from Puffin import encrypt, decrypt  # Import the PUFFIN cipher module

def server():
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    master_key = 0x0123456789ABCDEF0123456789ABCDEF  # Shared master key

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                try:
                    # Receive encrypted data from client
                    encrypted_data = conn.recv(1024)
                    if not encrypted_data:
                        print("Client disconnected.")
                        break

                    # Decrypt the client message
                    print(f"Received enc message: {encrypted_data}")
                    decrypted_message = decrypt(encrypted_data, master_key).decode()
                    print(f"Client: {decrypted_message}")

                    # Get response from server operator
                    response = input("Server: ")
                    if not response:
                        print("Exiting...")
                        break
                    
                    # Encrypt the response and send back to client
                    encrypted_response = encrypt(response.encode(), master_key)
                    conn.sendall(encrypted_response)
                except Exception as e:
                    print(f"Error: {e}")
                    break

if __name__ == "__main__":
    server()
