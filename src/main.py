# the main Python program that calls all the other functions
# welcomes the user and asks what they want to do
# Path: src\main.py
import threading
import time
import packets
from util import load_settings as lset

#stores the ip address to send the packets to 
#the ip address is stored in a string variable

def main():
    lset.load_settings()
    print('Welcome to the Network Performance Tester')
    print('1. Test network performance')
    print('2. change target ip address')
    print('3. settings')
    print('4. reload settings (not implemented yet)')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        print('Testing network performance...')
        # create a thread that runs the send_packets function
        ip_address_destination = lset.get_setting('target settings','target_ip')
        destination_port = lset.get_setting('target settings','target_port')
        print(str(ip_address_destination)+ ' on port ' + str(destination_port))
        packets.send_packets(str(ip_address_destination), int(destination_port))
        #t = threading.Thread(target=send_packets, args=(ip_address_destination, destination_port))
        #t.start()
    elif choice == '2':
        temp = input('Enter the new ip address: ')
        #checks if the ip address is valid and if it is then it changes the ip address
        #requires the ip address to be in the format x.x.x.x where x is a number between 0 and 255
        if temp.count('.') == 3:
            if temp.split('.')[0].isdigit() and temp.split('.')[1].isdigit() and temp.split('.')[2].isdigit() and temp.split('.')[3].isdigit():
                if int(temp.split('.')[0]) >= 0 and int(temp.split('.')[0]) <= 255 and int(temp.split('.')[1]) >= 0 and int(temp.split('.')[1]) <= 255 and int(temp.split('.')[2]) >= 0 and int(temp.split('.')[2]) <= 255 and int(temp.split('.')[3]) >= 0 and int(temp.split('.')[3]) <= 255:
                    lset.set_setting('target settings','target_ip',temp)
                    print('ip address changed to ' + temp)
                else:
                    print('Invalid ip address. Please try again.')
                    main()
            else:
                print('Invalid ip address. Please try again.')
                main()
        main()
    elif choice == '3':
        #runs the settings function that modifications to the settings.txt file 
        print('Settings:')
        #prints all the settings
        #removes the brackets from the settings and displays them in a table
        for i in range(len(lset.get_all_settings())):
            temp = lset.get_all_settings()[i]
            print(str(temp[0]) + ' '*(24-len(str(temp[0]))) + str(temp[1]) + ' '*(24-len(str(temp[1]))) + str(temp[2]))
        main()
    elif choice == '4':
        #reloads the settings file
        lset.save_settings()
        print('settings reloaded')
        main()
    elif choice == '5':
        print('Goodbye!')
    else:
        print('Invalid choice. Please try again.')
        main()

if __name__ == '__main__':
    main()