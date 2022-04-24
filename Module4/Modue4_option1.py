from cgitb import reset
from os import system, name
import time


# to clear the terminal and make it more readable
# shamelessly copied from module 2.

 
class knowledge(object):
    def __init__(self):
        self=self

    def what_is_knowledge():
        good_programer.clear()
        print("The knowledge a good programer has is not limited to the language or architecture they are working with.  They mush also understand the process they are attepmting to model or business they are supporting.")
        input('\nPress enter to return to the menu.')
        good_programer.three_characteristics()

class creative(object):
    def __init__(self):
        self = self
    def what_is_creativity():
        good_programer.clear()
        print("Creativity is finding ways to solve complex problems using efficent and elegant code.  It is also finding new solutions to old problems and being able to find where the existing ones lie.")
        input('\nPress enter to return to the menu.')
        good_programer.three_characteristics()


class intellegence(object):
    def __init__(self):
            self = self

    def what_is_intellegence():
        good_programer.clear()
        print("Intellegence is the ability to apply knowledge to solve a problem.  Intellegence is also indicates how easily a programer can pickup new skills and teach them to others.")
        input('\nPress enter to return to the menu.')
        good_programer.three_characteristics()

class good_programer(knowledge, creative, intellegence):
    def __init__(self, response):
        self.response = response

    def clear():
    # if windows
        if name == 'nt':
            _ = system('cls')
        else: # Mac or linux
            _ = system('clear')

    def quit_app():
        print('Thank you! This program will close in five seconds.')
        time.sleep(5)
        exit()

    def three_characteristics():
        good_programer.clear()
        print('''There are three characteristics I beleve that make good programers.
\n1. Knowledge
\n2. Intellegance
\n3. Creativity
\n4. I am finished
\n
\nWhich one do you want to learn about?''')
        while True:
            response = input(str('Your choice: '))
            if response == '1':
                knowledge.what_is_knowledge()
                break
            if response == '2':
                intellegence.what_is_intellegence()
                break
            if response == '3':
                creative.what_is_creativity()
                break
            if response == '4':
               good_programer.quit_app()
            print('Please pick a valid response.')


    def interface():
        good_programer.clear()
        print('''Do you want to learn what makes a good programer?  Y/N?''')

        response = input('Your selection: ')
        if (response == 'y' or response == 'Y'):
            good_programer.clear()
            good_programer.three_characteristics()
        else:
            good_programer.quit_app()

good_programer.interface()