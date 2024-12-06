import socket
from Puffin import encrypt, decrypt  # Import the PUFFIN cipher module

def client():
    host = '127.0.0.1'  # Server address
    port = 65432        # Server port

    master_key = 0x0123456789ABCDEF0123456789ABCDEF  # Shared master key

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to the server.")
        while True:
            try:
                # Get input from the client
                message = input("Client: ")
                if not message:
                    print("Exiting...")
                    break
                
                # Encrypt the message and send to server
                encrypted_message = encrypt(message.encode(), master_key)
                print(f"Sending enc message {encrypted_message}")
                s.sendall(encrypted_message)

                # Receive encrypted response from server
                encrypted_response = s.recv(1024)
                if not encrypted_response:
                    print("Disconnected from server.")
                    break

                # Decrypt the server response
                decrypted_response = decrypt(encrypted_response, master_key).decode()
                print(f"Server: {decrypted_response}")
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    client()
