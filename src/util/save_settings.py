#loads the settings from the file settings.txt
#the settings are stored in the ./utils directory
#all the required imports for the load_settings function
import os
import json
import sys
import time
import load_settings as lset
#difines the 2d arrays of the different types of settings
packet_settings = []
target_settings = []
network_settings = []
misc_settings = []
def load_settings():
    lset.load_settings()
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
    return False
def save_settings():
    settings_file = open('settings.txt', 'r')
    #read the settings file
    settings_file_contents = settings_file.read()
    #close the settings file
    settings_file.close()
    #saves the settings to the settings file if there are any changes that need to be saved
    if check_for_changes(settings_file_contents):
        #replace in the settings file the old settings with the new settings
        #from packet_settingd[1][0] + '::' ti
        for i in range(len(packet_settings)):
            settings_file_contents = settings_file_contents.replace(packet_settings[i][0] + '::' + packet_settings[i][1], packet_settings[i][0] + '::' + packet_settings[i][1])
        for i in range(len(target_settings)):
            settings_file_contents = settings_file_contents.replace(target_settings[i][0] + '::' + target_settings[i][1], target_settings[i][0] + '::' + target_settings[i][1])
        for i in range(len(network_settings)):
            settings_file_contents = settings_file_contents.replace(network_settings[i][0] + '::' + network_settings[i][1], network_settings[i][0] + '::' + network_settings[i][1])
        for i in range(len(misc_settings)):
            settings_file_contents = settings_file_contents.replace(misc_settings[i][0] + '::' + misc_settings[i][1], misc_settings[i][0] + '::' + misc_settings[i][1])
        #open the settings file
        settings_file = open('settings.txt', 'w')
        #write the new settings to the settings file
        settings_file.write(settings_file_contents)
        #close the settings file
        settings_file.close()
    else:
        print('no changes to save')
    print("not implemented yet")
print(target_settings)