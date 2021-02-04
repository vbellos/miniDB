import socket
import sys
import compiler

def start_menu():
    ip = input("Enter ip or leave empty for default ip(127.0.0.1):")
    if ip =='' :
        ip = '127.0.0.1'
        
    port = input("Enter port or leave empty for default port(3555):")
    if port == '' :
        port = 3555
    nc = input("Enter number of clients to listen or leave empty for default(5):")
    if nc == '' :
        nc = 5
        
    start_server(ip,int(port),int(nc))

def start_server(ip,port,nc):
    com = compiler
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip,port)
    print(f"starting up on {ip} port: {port}")
    sock.bind(server_address)
    sock.listen(nc)
    while True:
        try:
           
            print (sys.stderr, "waiting for connection")
            client, address = sock.accept()
            print(f"Connection Established - {address[0]}:{address[1]}")
        #Receive
            string = client.recv(1024)
            ui = string.decode("utf-8")
            print(ui)
            ui= ui.split("::")
            db = ui[0]
            query = ui[1]
            answer = com.comp(db,query)	
        #Send		
            client.send(bytes(answer, "utf-8"))
            client.close()
            
        except(KeyboardInterrupt,SystemExit):
            sock.close()
            print("Server Stopped manually")
            break

if __name__ == "__main__":

    while True:
        start_menu()
        a = input("Wanna start a new Server? (Type 'yes' to continue)")
        if a != 'yes':
            break

        print("Thank you for using our software \n Goodbye!!")