#!/bin/python3
#---- Script creado por Pavel Butzmann
#---- Obtencion de comandos en switch mediante python

import getpass
from datetime import date
from netmiko import ConnectHandler

today = date.today()
target = input("IP address: ") # Se solicita al usuario ingresar la direccion IP
print("SSH Login")
user = input("User: ") # se solicita usuario con el que se puede ingresar al dispositivo
passw = getpass.getpass() #Solicita password para entrar al dispositivo sin mostrar los caracteres


iou1 = {
'device_type': 'cisco_ios',
'ip': target,
'username': user,
'password': passw,
}

device = ConnectHandler(**iou1) # Conexion al dispositivo

output0 = device.send_command("show run | include hostname")
output1 = device.send_command("show running-config")
output2 = device.send_command("show inventory")
output3 = device.send_command("show version")
output4 = device.send_command("show ip interface brief")
output5 = device.send_command("show vlan")
output6 = device.send_command("show interface status")
output7 = device.send_command("show ip route")
output8 = device.send_command("show cdp neighbors")
output9 = device.send_command("show cdp neighbors detail")

save_file = open((output0[9::])+"-backup-"+str(today)+".txt","w")
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *          SHOW RUNNING CONFIG        * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output1)
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *           SHOW INVENTORY            * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output2)
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *             SHOW VERSION            * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output3)
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *        SHOW IP INTERFACE BRIEF      * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output4)
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *              SHOW VLAN              * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output5)
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *         SHOW INTERFACE STATUS       * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output6)
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *            SHOW IP ROUTE            * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output7)
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *          SHOW CDP NEIGHBORS         * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output8)
save_file.write("\n\n\n --------------------------------------- \n")
save_file.write("\n *      SHOW CDP NEIGHBORS DETAIL      * \n")
save_file.write("\n --------------------------------------- \n")
save_file.write(output9)

save_file.close() # Se guarda el documento en la misma ruta donde se ejecuta el programa
device.disconnect() # desconexion del dispositivo