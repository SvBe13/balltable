from vpython import *
import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 30000

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

#Ball on table

redbox=box(pos=vector(0,0,0), angle=0, size=vector(36,-0.25,32), up = vector(0,1,0), color=color.red) #lokales KO
ball=sphere(pos=vector(0,1,0), radius=0.85,color=color.green) #globales KO

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data_unpacked=struct.unpack('6f',data)
    print(data_unpacked)
    ball.pos.x =data_unpacked[2]
    ball.pos.z =data_unpacked[4]
    #redbox = redbox(angle = 0.357, axis = vector(1,0,0), origin = vector(0,0,0), up = vector(0,1,0))
    #redbox(angle = box.pos+box.pos.x, axis = vector(1,0,0), origin = vector(0,0,0), up = vector(0,1,0))

#Rotation of Table
redbox.rotate(angle = 1, axis = vector(1,0,0), origin = vector(0,0,0))

#Transformationsmatrix Tisch KO ins globale KO
#Rotation der Achsen
#PHI = math.radians(15)
#PHI_rot = matrix([[1,0,0],[0,cos(PHI),-sin(PHI)],[0,sin(PHI), cos(PHI)]]) #Rotation um x-Achse
#Theta = math.radians(10)
##Theta_rot = matrix([[cos(Theta),-sin(Theta), 0], [sin(Theta), cos(Theta), 0], [0,0,1]]) #Rotation um z-Achse

#Multiplikation der Matrizen
#trans_m = Theta_rot*PHI_rot

#Transformation ins Globale-KO, Tisch
#tisch_gf = redbox.rotate * trans_m

#Transformation ins Globale-KO, Kugel
#kugel_gf = ball * trans_m

    
    
