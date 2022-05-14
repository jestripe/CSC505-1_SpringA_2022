from os import system, name
from re import sub
import time
import datetime as datetime


def clear():
# if windows
    if name == 'nt':
        _ = system('cls')
    else: # Mac or linux
        _ = system('clear')

class phtrs_citizen(object):
    def __init__(self):
        self = self

    def damage_file():
        clear()
        claim_type = input('Was this a damage, injury or both? ')
        clear()
        date_of_event = input('Which day did this happen on? ')
        clear()
        police_report = input('Was a police report filed?  If yes please provide the case number. ')
        clear()
        description = input('Describe the damage or injury. ')
        clear()
        cost = input('Cost to repair/billed for treatment? ')
        tmp = str(claim_type + ", " + date_of_event  + ", " + police_report + ", " + description + ", " + cost)
        return tmp


    def new_report():
        clear()
        submit_date = str(datetime.date.today())
        fname = input("What is your first name? ")
        clear()
        lname = input("What is your last name? ")
        clear()
        address = input("Please provide your address. ")
        clear()
        phone = input("Please provide a phone number. ")
        clear()
        email = input("Please provide an email address. ")
        clear()
        location = input('Please provide the location of the pothole. ')
        clear()
        size = input('Please provide an approximate size in inches for the pothole.')
        clear()
        damage = input('Is there any property damage or injuries assocaiated with this pothole Y/N? ')
        if (damage == 'y' or damage == 'Y'):
            df = (phtrs_citizen.damage_file()+ "," + submit_date + "," + fname + "," + lname + ';')
            with open('damages.txt', 'a') as f:
                f.write(df)
                f.close()
                exit()
        else:
            pass

        tmp = (submit_date + ", " +fname + "," + lname + "," + address + "," + phone + "," + email + "," + location + "," + size + "," + damage +';')
        
        with open('tmp_database.txt', 'a') as f:
            f.write(tmp)
            f.close()
            exit()

phtrs_citizen.new_report()