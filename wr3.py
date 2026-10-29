# Import the socket module
import socket

# Resolve the hostname into an IP address
hostname = "localhost"
ip_address = socket.gethostbyname(hostname)

# Print the result
print(f"Hi, {hostname} resolves to {ip_address}.")
