#loads the settings from the file settings.txt
#the settings are stored in the ./utils directory
#all the required imports for the load_settings function
import os
import json
import sys
import time
#difines the 2d arrays of the different types of settings
packet_settings = []
target_settings = []
network_settings = []
misc_settings = []
#loads the settings from the file settings.txt in to a 2d array of setting and value 
#for each type of setting: packet settings, target settings, network settings and misc settings
#each section of settings is seperated by a new line with the title of the section proceeded by a ~
#each setting is seperated by a '//' followed by the name and use of the setting
#on the following line is the name of the setting followed by a ':' and the value of the setting
def load_settings():
    global packet_settings
    global target_settings
    global network_settings
    global misc_settings
    #opens the file in read mode and stores the contents in a variable
    try:
        with open(os.path.join(sys.path[0], 'util/settings.txt'), 'r') as f:
            settings_file = f.read()
    except:
        with open(os.path.join(sys.path[0], 'settings.txt'), 'r') as f:
            settings_file = f.read()
    #splits the file into sections of settings
    settings_file = settings_file.split('~')    
    #splits the packet settings section into individual settings
    packet_settings = settings_file[1].split('//')
    target_settings = settings_file[2].split('//')
    network_settings = settings_file[3].split('//')
    misc_settings = settings_file[4].split('//')
    #for each type of setting: packet settings, target settings, network settings and misc settings
    #the data is cycled through the following loop to make it useable
    all_settings = [packet_settings, target_settings, network_settings, misc_settings]
    for i in range(len(all_settings)):
        #all_settings[i] = settings_file[i].split('//')
        all_settings[i].pop(0)
        #formats all the arrays to the useable format
        #removes the text before the first '\n' in each setting and removes the '\n' from the end of each setting
        temp = all_settings[i]
        for j in range(len(temp)):
            try:
                #print(str(j+1)+ ' of ' + str(len(temp)) + ' in settings section ' + str(i+1))
                #print(temp[j])
                temp[j] = temp[j].split('\n')
                #if j == 0:
                temp[j].pop(0)
                temp[j][1] = temp[j][1].rstrip()
                #splits the packet settings section into individual settings
                #moves all the text after the '::' to the the following index of the array
                #removes the '::' from the end of the setting name
                temp[j][0] = temp[j][0].split('::')
                temp[j][0][1] = temp[j][0][1].rstrip()
                #simplifies the array so that for example: [[['target_ip', '8.8.8.8'], ''], [['target_port', '12345'], '']] 
                #becomes ['target_ip', '8.8.8.8'], ['target_port', '12345']
                #this makes it easier to access the settings
                #by removing the extra brackets
                temp[j] = temp[j][0] + temp[j][1:]
                #then removing the last index of each setting that is empty(all settings have a value that is epmty)
                temp[j].pop()
                #print(temp[j])
            except:
                print('error')
                pass
#loads in to ram the settings from the settings.txt file to have a chance to modify them
def set_setting(setting_type, setting_name, setting_value):
    #sets the value of the setting
    #setting_type is the type of setting: packet settings, target settings, network settings and misc settings
    #setting_name is the name of the setting
    #setting_value is the value of the setting
    #the setting is searched for in the 2d array of settings
    #if the setting is found, the value of the setting is changed to the new value
    #if the setting is not found, the function returns 'setting not found'
    if setting_type == 'packet settings':
        for i in range(len(packet_settings)):
            if packet_settings[i][0] == setting_name:
                packet_settings[i][1] = setting_value
                return
    elif setting_type == 'target settings':
        for i in range(len(target_settings)):
            if target_settings[i][0] == setting_name:
                target_settings[i][1] = setting_value
                return
    elif setting_type == 'network settings':
        for i in range(len(network_settings)):
            if network_settings[i][0] == setting_name:
                network_settings[i][1] = setting_value
                return
    elif setting_type == 'misc settings':
        for i in range(len(misc_settings)):
            if misc_settings[i][0] == setting_name:
                misc_settings[i][1] = setting_value
                return
    else:
        print("setting not found")
        return 'setting not found'
    #if the program is in debug mode, print curennt settings
    #print(packet_settings)
    #print(target_settings)
    #print(network_settings)
    #print(misc_settings)
def get_setting(setting_type, setting_name):
    #returns the value of the setting
    #setting_type is the type of setting: packet settings, target settings, network settings and misc settings
    #setting_name is the name of the setting
    #the setting is searched for in the 2d array of settings
    #if the setting is found, the value of the setting is returned
    #if the setting is not found, the function returns 'setting not found'
    if setting_type == 'packet settings':
        for i in range(len(packet_settings)):
            if packet_settings[i][0] == setting_name:
                return packet_settings[i][1]
    elif setting_type == 'target settings':
        for i in range(len(target_settings)):
            if target_settings[i][0] == setting_name:
                return target_settings[i][1]
    elif setting_type == 'network settings':
        for i in range(len(network_settings)):
            if network_settings[i][0] == setting_name:
                return network_settings[i][1]
    elif setting_type == 'misc settings':
        for i in range(len(misc_settings)):
            if misc_settings[i][0] == setting_name:
                return misc_settings[i][1]
    else:
        print("setting not found")
        return 'setting not found'
def get_all_settings():
    #returns all the settings in a 2d array
    #the 2d array is in the format: [[setting_type, setting_name, setting_value], [setting_type, setting_name, setting_value], ...]
    #the setting_type is the type of setting: packet settings, target settings, network settings and misc settings
    #the setting_name is the name of the setting
    #the setting_value is the value of the setting
    all_settings = []
    for i in range(len(packet_settings)):
        all_settings.append(['packet settings', packet_settings[i][0], packet_settings[i][1]])
    for i in range(len(target_settings)):
        all_settings.append(['target settings', target_settings[i][0], target_settings[i][1]])
    for i in range(len(network_settings)):
        all_settings.append(['network settings', network_settings[i][0], network_settings[i][1]])
    for i in range(len(misc_settings)):
        all_settings.append(['misc settings', misc_settings[i][0], misc_settings[i][1]])
    return all_settings
def find_full_string(string, start_substring, end_substring):
    # find the start index of the first occurrence of the start substring
    start_index = string.find(start_substring)
    if start_index == -1:
        return None

    # find the end index of the last occurrence of the end substring
    end_index = string.rfind(end_substring)
    if end_index == -1:
        return None

    # return the full string
    return string[start_index:end_index + len(end_substring)]
def set_setting(setting_type, setting_name, setting_value):
    global packet_settings
    global target_settings
    global network_settings
    global misc_settings
    #sets the value of the setting
    #setting_type is the type of setting: packet settings, target settings, network settings and misc settings
    #setting_name is the name of the setting
    #setting_value is the value of the setting
    #the setting is searched for in the 2d array of settings
    #if the setting is found, the value of the setting is changed to the new value
    #if the setting is not found, the function returns 'setting not found'
    if setting_type == 'packet settings':
        for i in range(len(packet_settings)):
            if packet_settings[i][0] == setting_name:
                packet_settings[i][1] = setting_value
                return
    elif setting_type == 'target settings':
        for i in range(len(target_settings)):
            if target_settings[i][0] == setting_name:
                target_settings[i][1] = setting_value
                return
    elif setting_type == 'network settings':
        for i in range(len(network_settings)):
            if network_settings[i][0] == setting_name:
                network_settings[i][1] = setting_value
                return
    elif setting_type == 'misc settings':
        for i in range(len(misc_settings)):
            if misc_settings[i][0] == setting_name:
                misc_settings[i][1] = setting_value
                return
    else:
        print("setting not found")
        return 'setting not found'
def check_for_changes(settings_file_contents):
    #check if the settings file has the any changes that need to be saved
    #if the settings file has no changes that need to be saved, the function returns
    for i in range(len(packet_settings)):
        if packet_settings[i][0] + '::' + packet_settings[i][1] not in settings_file_contents:
            return True
    for i in range(len(target_settings)):
        if target_settings[i][0] + '::' + target_settings[i][1] not in settings_file_contents:
            return True
    for i in range(len(network_settings)):
        if network_settings[i][0] + '::' + network_settings[i][1] not in settings_file_contents:
            return True
    for i in range(len(misc_settings)):
        if misc_settings[i][0] + '::' + misc_settings[i][1] not in settings_file_contents:
            return True
    return True
def save_settings():
    try:
        with open(os.path.join(sys.path[0], 'util/settings.txt'), 'r') as f:
            settings_file_contents = f.read()
    except:
        with open(os.path.join(sys.path[0], 'settings.txt'), 'r') as f:
            settings_file_contents = f.read()
            print("failed to open settings file in utils folder, trying to open settings file in main folder")
    #saves the settings to the settings file if there are any changes that need to be saved
    if check_for_changes(settings_file_contents):
        #replace in the settings file the old settings with the new settings
        #from packet_settingd[1][0] + '::' till 
        for i in range(len(packet_settings)):
            #finds out what the curent setting is so it can be replaced with the new setting 
            if (packet_settings[i][0] + '::' + packet_settings[i][1] not in settings_file_contents):
                print(packet_settings[i][0] + '::' + packet_settings[i][1] + 'not changed')
            else:
                temp = find_full_string(settings_file_contents, (packet_settings[i][0] + '::'), '\n')
                print(temp)
                if temp != None:
                    settings_file_contents = settings_file_contents.replace(temp, packet_settings[i][0] + '::' + packet_settings[i][1])
        for i in range(len(target_settings)):
            temp = find_full_string(settings_file_contents, (target_settings[i][0] + '::'), '\n')
            print(temp)
            if temp != None and (target_settings[i][0] + '::' + target_settings[i][1] not in settings_file_contents):
                settings_file_contents = settings_file_contents.replace(temp, target_settings[i][0] + '::' + target_settings[i][1])
        for i in range(len(network_settings)):
            settings_file_contents = settings_file_contents.replace(network_settings[i][0] + '::' + network_settings[i][1], network_settings[i][0] + '::' + network_settings[i][1])
        for i in range(len(misc_settings)):
            settings_file_contents = settings_file_contents.replace(misc_settings[i][0] + '::' + misc_settings[i][1], misc_settings[i][0] + '::' + misc_settings[i][1])
        #opens the settings file and writes the new settings to the file
        try:
            with open(os.path.join(sys.path[0], 'util/settings.txt'), 'w') as f:
                f.write(settings_file_contents)
        except:
            with open(os.path.join(sys.path[0], 'settings.txt'), 'w') as f:
                f.write(settings_file_contents)
                print("failed to open settings file in utils folder, trying to open settings file in main folder")
    else:
        print('no changes to save')
    print("not implemented yet")


#end of code any following code is for testing purposes
if __name__ == '__main__':
    load_settings()
    set_setting('target settings','target_ip','1.1.1.1')
    save_settings()
    print(get_setting('target settings', 'target_ip'))