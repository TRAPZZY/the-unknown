```markdown
# The Unknow

The Unknow is a secure communication system developed by Trapzzy. It uses symmetric encryption to ensure that messages sent between a client and a server are encrypted and secure. The system also employs HTTPS to provide a secure channel for communication over the internet.

## Features

- Symmetric encryption using Fernet (AES)
- Secure communication over HTTPS
- Multi-threaded server to handle multiple clients
- User-friendly client interface for entering the server link

## Requirements

- Python 3.6 or higher
- `cryptography` library
- OpenSSL (for generating self-signed SSL certificates)

## Setup

1. **Install the required Python library**:

   ```bash
   pip install cryptography
   ```

2. **Generate a self-signed SSL certificate** (for testing purposes):

   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes
   ```

   This will create `server.crt` and `server.key` files in your current directory.

3. **Run the server**:

   ```bash
   python server.py
   ```

   The server will display a link for secure communication. Note this link for use in the client.

4. **Run the client**:

   In a separate terminal or on a different machine, run:

   ```bash
   python client.py
   ```

   Enter the link displayed by the server when prompted.

## Usage

Once the server and client are running, the client can send encrypted messages to the server. The server will decrypt these messages and display them.

## Security

- The system uses Fernet symmetric encryption, which is built on top of AES. 
- Communication between the client and server is encrypted using HTTPS.
- For production use, obtain a certificate from a trusted certificate authority (CA) instead of using a self-signed certificate.

## Author

- **Trapzzy** - *Initial work* - [Trapzzy](https://github.com/trapzzy)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the Python and cryptography communities for providing the tools and libraries to make secure communication possible.
```


