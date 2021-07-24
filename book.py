# book = "The Hitchiker's Guide to the Galaxy"
# booklist = list(book)
# print(booklist)
# print(''.join(booklist[-6:]))

# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)
#
# new_list = (''.join(plist[1:3]))
# new_list = new_list + ''.join([plist[5], plist[4], plist[7], plist[6]])
#
# print(new_list)

import platform
import socket

myIP = socket.gethostbyname(socket.gethostname())
myIP_list = list(myIP)
for n in myIP_list:
    if myIP_list[0] != '.':
        myIP_list.pop(0)
for n in myIP_list:
    if myIP_list[-1] != '.':
        myIP_list.pop()
routIP = "10."+''.join(myIP_list[1:-1])+".1"
prIP = ''.join(myIP_list[1:-1])

pc_name = platform.node()
pc_list = list(pc_name)
for i in range(3):
    pc_list.pop()
num = ''.join(pc_list[2:])
pIP = ''.join(pc_list[2:4]) + "." + ''.join(pc_list[4:6])
ipRouter = "10." + ''.join(pc_list[2:4]) + "." + ''.join(pc_list[4:6]) + ".1"

print ("Получаем из HostName - " + pc_name)
print("номер магазина-" + num)
print("переменная %IP - " + pIP)
print("IP адрес роутера - " + ipRouter)
print()
print("Получаем из IP адреса - " + myIP)
print("IP адрес роутера - " + routIP)
print("переменная %IP - "  + prIP)
# for i in pc_list:
    # print('\t', i)
