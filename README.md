# ITNE352-Project-Group-B15
# Multithreaded News Client/Server Information System

## Project Description
This project is a Python-based multithreaded client-server system designed to exchange news data. The server fetches news from the [NewsAPI](https://newsapi.org/) and responds to client requests, enabling users to explore news headlines, sources, and categories interactively.

The project demonstrates core concepts of **network programming**, including:
- Client-server architecture
- Multithreading
- API integration
- TCP socket communication

---

## Table of Contents
1. [Features](#features)
2. [System Requirements](#system-requirements)
3. [Setup Instructions](#setup-instructions)
4. [Usage Guide](#usage-guide)
5. [Design Details](#design-details)
6. [Folder Structure](#folder-structure)
7. [Acknowledgments](#acknowledgments)

---

## Features
### Server:
- Handles multiple simultaneous client connections using threads.
- Fetches news data from NewsAPI and saves responses in JSON format.
- Logs client connections, disconnections, and requests.

### Client:
- User-friendly menu-driven interface.
- Allows users to:
  - Search for news headlines by keyword, category, or country.
  - View available news sources by category, country, or language.
  - Save results in structured JSON files.

---

## System Requirements
- **Python**: 3.10 or higher
- **Libraries**:
  - `requests`
  - `socket`
  - `threading`
  - `json`

To install the required libraries:
```bash
pip install requests
```
## Setup Instructions
1. Clone the Repository
Clone the project folder or manually create the files (server.py and client.py) in a directory.

2. Configure NewsAPI
Sign up for a free API key at NewsAPI.org.
Replace the API_KEY in server.py with your actual API key

3. Run the Server
Open a terminal in the project directory.
Run the server script: `python server.py`

4. Run the Client `python client.py`

## Design Details
### Architecture:
Server:

Runs on 127.0.0.1:12345 and listens for client connections.
Utilizes threads to handle multiple clients simultaneously.
Fetches data from the NewsAPI based on client requests.
Client:
Connects to the server via TCP.
Provides an interactive menu-driven interface for user interaction.
Error Handling:
The server gracefully handles connection errors and API request failures.
The client ensures smooth navigation even with invalid inputs.

## Folder Structure
```bash
MultithreadedNewsSystem/
├── server.py          # Server script
├── client.py          # Client script
├── README.md          # Project documentation
```

## Acknowledgments
NewsAPI for providing an extensive news database.
Python libraries for enabling network communication and API integration. 
