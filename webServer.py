#import socket module
from socket import *

#in order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #prepare a server socket
    serverSocket.bind(("", port))


    #Fill in start

    serverSocket.listen()
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #fill in
        print(f"Connected by {addr}")
        
        try:
            message = connectionSocket.recv(4096).decode('utf-8') #client is sending you a message    
            #print(message.value)
            filename = message.split()[1]
            print(f"filename: {filename}")
            
            #opens the client requested file
            #how should you read a file if you plan on sending it through a socket?
            f = open(filename[1:])

         
            #f.close()

            outputdata = b"Content-Type:text/html;charset = UTF-8\r\n"

            #Fill in start-This variable can store your headers you want to send for any valid or invalid request
            #content type above is an example on how to send a header as bytes

            #fill in end

            #send an HTTP header line into a socket for a valid request. What header should be sent for a response that is ok

            #fill in start

            header = 'HTTP/1.1 200 OK\n\n'

            #fill in end

            #send the content of the requested file to the client

            final_response = header

            for i in f: #for line in file
                
                #fill in start- send your html file contents
                
                response = i

                final_response += response
                
                # fill in end
            
            #print(final_response)
            connectionSocket.send(final_response.encode('utf-8'))
            connectionSocket.close() #closing the connection socket

        except Exception as e:
            #Send response message for invalid request due to the file not being found
            #fill in start
            print("Exception occurred!")
            header = 'HTTP/1.1 404 Not Found\n\n'

            response = """<html>
                          <body>
                            <center>
                             <h3>Error 404: File not found</h3>
                            </center>
                          </body>
                        </html>""".encode('utf-8')

            final_response = header.encode('utf-8') + response
            print(final_response)

            connectionSocket.send(final_response)


            #fill in end

            #close client socket
            #fill in start

            connectionSocket.close() 


            #fill in end

    serverSocket.close()
    sys.exit()   #Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
