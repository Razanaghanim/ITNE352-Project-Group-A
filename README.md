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
