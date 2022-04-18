from cgitb import reset
from os import system, name
import time

class listapp(object):
    def __init__(self, response):
        self.response = response
    
    # to clear the terminal and make it more readable
    # shamelessly copied from last week's assignment.
    def clear():
        # if windows
        if name == 'nt':
            _ = system('cls')
        else: # Mac or linux
            _ = system('clear')

    # outline the tools to be used in order to build the application
    def tools():
        listapp.clear()
        print('''In order to facilitate this aplication across multiple platforms the following tools will be used.
\n1. Javascript with React js to build the user interface and core application.
\n2. The data itself will be stored locally as a json file eliminating the need for
    a structured local database.
\n3. Server side infrastructure will be hosted on Amazon Web Services
\n4. Syncronization of account across multiple devices still needs consideration.''')
        input('Press enter to return to the menu.')
        listapp.module_interface()

# describe the logic of the log in screen
    def login():
        listapp.clear()
        print('''The pseudo logic for the login screen is as follows:
\non login_button.click()
if login_handshake == True:
    sync.sync_lists()
    Lists.show()
else:
    error_dialogue(bad_credentials)
    exit()''')
        input('Press enter to return to the menu.')
        listapp.module_interface()

# describe the logic of the lists interface
    def Lists_interface():
        listapp.clear()
        print('''The functionality of the list interface is outline below:
\ndef show():
    get list of lists from the server
    if lists match:
        exit()
    elif new_list_on_server:
        download
    else:
        upload new list on device
\ndef select_list():
    on long_click():
        highlight item
    on click():
        retrieve_list_data()
\ndef rearrange_list():
    with select:
    on click_drag():
        set new index based on new position in list
        on click_release():
            exit()
''')
        input('Press enter to return to the menu.')
        listapp.module_interface()

# describe the list functions
    def lists_function():
        listapp.clear()
        print('''The list functionality is outline below:
\ndef open(list):
    with List_interface.select_list(list)
        read.json(list)
        render(list)
\ndef create_new():
    on click()
        input_dialouge(new_list)
        json.create_empty(name_input)
        render(name_input)
        on close()
            upload to server
\ndef delete:
    on click()
        warning_dialouge(delete_yn)
        if delete == yes:
            json.key(list).delete
        else:
            exit''')
        input('Press enter to return to the menu.')
        listapp.module_interface()

#describe the item functions
    def item_functions():
        listapp.clear()
        print('''The item functionallaty is outline below:
\ndef add_item():
    if length list.index() == 0
        set index == 0
        render check_box(false)
        set focus cursor at position 0 index 0
    else:
        get length of list.index == n
            p = n+1
            set index == p
            render check_box(false)
            set focus cursor at position 0 index P
\ndef delete_item
    with item.index(n) selected
        json.delete_element.key(n)
        reset.index()''')
        input('Press enter to return to the menu.')
        listapp.module_interface()

# Sets up the interface for this script
    def module_interface():
        listapp.clear()
        print('''Select an option to learn about this application:
\n1. The tools to be used
\n2. The login funtionallity
\n3. The lists interface
\n4. The list functionallity
\n5. The item functionallity
\n6. I am finished ''')

    #returns the corresponding information while gracefully handling bad options.
        while True:
            response = input(str('Your selection: '))
            if response == '1':
                listapp.tools()
                break
            if response == '2':
                listapp.login()
                break
            if response == '3':
                listapp.Lists_interface()
                break
            if response == '4':
                listapp.lists_function()
                break
            if response == '5':
                listapp.item_functions()
                break
            if response == '6':
                print('Thank you! This program will close in five seconds.')
                time.sleep(5)
                exit()
            print('Please pick a valid response.')

# executes the script.
listapp.module_interface()