import socket
import threading
import requests
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
API_KEY = '392f07995d1647219aba47100df38789'

def fetch_news_data(request_type, filters=None):
    base_url = "https://newsapi.org/v2/"
    endpoints = {
        "headlines": "top-headlines",
        "sources": "sources"
    }
    params = {"apiKey": API_KEY}

    if filters:
        params.update(filters)

    try:
        response = requests.get(base_url + endpoints[request_type], params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        return {"error": str(error)}

def handle_client_connection(client_socket, client_address):
    print(f"[INFO] New connection established with {client_address}")
    client_socket.send("Welcome! Please enter your name: ".encode('utf-8'))
    client_name = client_socket.recv(1024).decode('utf-8').strip()
    print(f"[INFO] Client identified as: {client_name}")

    while True:
        main_menu = """
        Main Menu:
        1. Search Headlines
        2. View Sources
        3. Exit
        Choose an option: """
        client_socket.send(main_menu.encode('utf-8'))
        client_choice = client_socket.recv(1024).decode('utf-8').strip()

        if client_choice == "1":
            headlines_menu = """
            Headlines Menu:
            1. Search by Keyword
            2. Search by Category
            3. Search by Country
            4. List All Headlines
            5. Back to Main Menu
            Enter your choice: """
            client_socket.send(headlines_menu.encode('utf-8'))
            sub_choice = client_socket.recv(1024).decode('utf-8').strip()
            
            filters = {}
            if sub_choice in ["1", "2", "3"]:
                client_socket.send("Enter the value: ".encode('utf-8'))
                filter_value = client_socket.recv(1024).decode('utf-8').strip()
                filters = {
                    "1": {"q": filter_value},
                    "2": {"category": filter_value},
                    "3": {"country": filter_value}
                }.get(sub_choice, {})
            results = fetch_news_data("headlines", filters)
            file_name = f"{client_name}_headlines.json"
            with open(file_name, "w") as file:
                json.dump(results, file)
            client_socket.send(f"Headlines saved to {file_name}\n".encode('utf-8'))

        elif client_choice == "2":
            sources_menu = """
            Sources Menu:
            1. Filter by Category
            2. Filter by Country
            3. Filter by Language
            4. View All Sources
            5. Back to Main Menu
            Enter your choice: """
            client_socket.send(sources_menu.encode('utf-8'))
            sub_choice = client_socket.recv(1024).decode('utf-8').strip()
            
            filters = {}
            if sub_choice in ["1", "2", "3"]:
                client_socket.send("Enter the value: ".encode('utf-8'))
                filter_value = client_socket.recv(1024).decode('utf-8').strip()
                filters = {
                    "1": {"category": filter_value},
                    "2": {"country": filter_value},
                    "3": {"language": filter_value}
                }.get(sub_choice, {})
            
            # Fetch sources and save results
            results = fetch_news_data("sources", filters)
            file_name = f"{client_name}_sources.json"
            with open(file_name, "w") as file:
                json.dump(results, file)
            client_socket.send(f"Sources saved to {file_name}\n".encode('utf-8'))

        elif client_choice == "3":
            client_socket.send("Goodbye!\n".encode('utf-8'))
            print(f"[INFO] Client {client_name} has disconnected.")
            break
        else:
            client_socket.send("Invalid choice. Please try again.\n".encode('utf-8'))

    client_socket.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(5)
        print(f"[INFO] Server is running on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, client_address))
            client_thread.start()

if __name__ == "__main__":
    start_server()
