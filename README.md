# Chat App GUI

This is a simple chat application with a graphical user interface (GUI) built using Python's PyQt5 library. The application allows multiple clients to connect to a server and exchange messages in real-time. This project demonstrates basic socket programming, threading, and GUI development.

## Features-**Real-time Chat**: Multiple clients can send and receive messages in real-time.
-**Simple GUI**: The chat interface is built using PyQt5, providing a user-friendly environment.
-**Multi-threading**: The server can handle multiple clients simultaneously using threads.
-**Cross-Platform**: Runs on Windows, macOS, and Linux.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- The following Python packages:
  -`PyQt5`

You can install PyQt5 using pip:
## Installation
1. Clone the repository:

    ```
    git clone https://github.com/your-username/chat-app-gui.git
    cd chat-app-gui
    ```
2. Modify the client:

    Before running the client, ensure that you modify the code to include the correct public IP address of the server you want to connect to. Open `client.py` and locate the line where the server IP is defined. Replace it with the server's public IP address.
    ```python
    # Example: Modify this line in client.py
    server_ip = 'your.server.ip.address'
    ```
3. Run the server:

    The server code is included in this repository. You can start the server by running the following command:
    ```
    python server.py
    ```
4. Run the client:

    After starting the server, you can run the chat client:
    ```
    python client.py
    ```
    This will launch the chat application's GUI.
## Usage- When the client application starts, it will prompt the user to enter a username.
- After entering the username, the user can type messages in the input field at the bottom of the window and press the "Send" button to send messages.
- The chat history is displayed in the main area of the window.
- To close the chat application, simply close the window. The client will automatically send a "quit" message to the server and close the connection.

## Known Issues- The application currently uses unencrypted socket communication, which may expose chat messages to network eavesdropping if used over a public network.
- There is no user authentication, so any client can connect to the server if they know the IP address and port.

## Future Enhancements- Implement SSL/TLS encryption for secure communication.
- Add user authentication to ensure that only authorized users can connect.
- Improve the GUI with additional features such as user lists, private messaging, and message timestamps.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Python Socket Programming](https://docs.python.org/3/howto/sockets.html)
- [Python Threading](https://docs.python.org/3/library/threading.html)

