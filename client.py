#Client
import socket

def send_query(ip,port,query):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    sock.send(bytes(query,"utf-8"))
    buffer = sock.recv(1024)
    buffer = buffer.decode("utf-8")
    print(f"Server: {buffer}")
    sock.close()

def connection():
    ip = input("Enter ip or leave empty for default ip:")
    if ip =='' :
        ip = '127.0.0.1'  
    port = input("Enter port or leave empty for default port:")
    if port == '' :
        port = 3555
    db =  input("Enter db name or leave empty for default db:")
    if db == '' :
        db = 'vsmdb'
    query = ''
    while query != 'exit':
        query = input("Enter Query or type 'exit' to exit: \n")
        if query != 'exit':
            query = (f"{db}::{query}")
            send_query(ip,int(port),query)

if __name__ == "__main__":
    
    while True:
        connection()
        a = input("wanna start a new connection? (Type 'yes' to continue)")
        if a != 'yes':
            break
            
    print("Thank you for using our software \n Goodbye!!")
