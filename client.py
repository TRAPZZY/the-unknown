import socket
import ssl
from cryptography.fernet import Fernet

# Load the encryption key
with open("encryption_key.txt", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Get the server's link from the user
link = input("Enter the link for secure communication: ")
server_ip, server_port = link.replace("https://", "").split(":")

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_context = ssl.create_default_context()
ssl_socket = ssl_context.wrap_socket(client_socket, server_hostname=server_ip)
ssl_socket.connect((server_ip, int(server_port)))

# Encrypt and send a message
message = "Hello, secure world!"
encrypted_message = cipher_suite.encrypt(message.encode("utf-8"))
ssl_socket.send(encrypted_message)
print(f"Sent encrypted message: {encrypted_message}")

# Clean up
ssl_socket.close()
client_socket.close()
