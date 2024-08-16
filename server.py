import socket
import threading

clients = []

def handleClient(c, addr):
    print("Got connection from", addr)
    clients.append(c)
    try:
        while True:
            data = c.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            broadcast(data, c)
    except Exception as e:
        print(f"Error in handleClient for {addr}: {e}")
    finally:
        print(f"Connection with {addr} closed.")
        clients.remove(c)
        c.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.sendall(message)
            except Exception as e:
                print(f"Error broadcasting to {client.getpeername()}: {e}")
                clients.remove(client)

def monitorInput(server_running):
    while server_running[0]:
        user_input = input()
        if user_input.strip().lower() == "quit":
            server_running[0] = False
            print("Server is shutting down.")
            broadcast(b"Server is shutting down...", None)

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(f"Socket creation failed: {e}")
        return
    
    try:
        port = 2169
        s.bind(('0.0.0.0', port))
        print(f"Socket is now bound to port {port}")
    except Exception as e:
        print(f"Socket binding failed: {e}")
        return
    
    s.listen(5)
    print("Socket is now listening.")

    server_running = [True]
    input_thread = threading.Thread(target=monitorInput, args=(server_running,))
    input_thread.start()

    while server_running[0]:
        try:
            s.settimeout(1.0)
            c, addr = s.accept()
            client_thread = threading.Thread(target=handleClient, args=(c, addr))
            client_thread.start()
        except socket.timeout:
            continue
        except Exception as e:
            print(f"Error occurred during accept: {e}")
            break
    
    s.close()
    print("Server has been shut down.")

if __name__ == "__main__":
    main()
