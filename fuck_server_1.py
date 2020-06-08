# first of all import the socket library 
import socket                
import threading
import time

# function definition, function is the target
def do_something():
    print ('Sleeping 1 second. . .')
    time.sleep(1)
    print ('Done Sleeping')

# next create a socket object 
s = socket.socket()          
print ('Socket successfully created')
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345 
print ('PORT 12345 is reserved for newly created socket')

server_address =('',port)
s.bind(server_address)
print ('Socket successfully bound to 12345') 

s.listen(5)
print ('Socket at port 12345 is listening') 

while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print ('Got connection from', addr) 

   # execute processes
   start = time.perf_counter()
    
   t1 = threading.Thread(target=do_something)
   t2 = threading.Thread(target=do_something)

   t1.start()
   t2.start()

   t1.join()
   t2.join()
    
   finish = time.perf_counter()
   spent_time = finish-start
   
   print(spent_time)
   f = round(spent_time)
   print(f)
   #send a thank you message to the client.  
   
   c.send (str.encode(str(f)))
   
   
   # Close the connection with the client 
   c.close()
   print('Connection terminated')
   print('Press Ctrl + C to close the server') 