import socket
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

def display_message_and_get_input(sock):
    server_message = sock.recv(1024).decode('utf-8')
    print(server_message)
    if "Goodbye!" in server_message:
        return None

    user_input = input("Enter your choice: ")
    sock.send(user_input.encode('utf-8'))
    return True

def main():
    # Establish connection with the server
    print("Connecting to the server...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            print(f"Connected to the server at {SERVER_HOST}:{SERVER_PORT}\n")
            while True:
                if not display_message_and_get_input(client_socket):
                    break

    except ConnectionError as e:
        print(f"Error connecting to the server: {e}")
    except KeyboardInterrupt:
        print("\nConnection closed by the user.")
    finally:
        print("Exiting the client application.")

if __name__ == "__main__":
    main()
