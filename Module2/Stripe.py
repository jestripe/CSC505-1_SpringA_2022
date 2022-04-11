from os import system, name
import time

class stripe(object):
    def __init__(self, response):
        self.response = response

    # to clear the terminal and make it more readable
    def clear():
        # if windows
        if name == 'nt':
            _ = system('cls')
        else: # Mac or linux
            _ = system('clear')

    def communication():
        stripe.clear()
        print('The Communication Phase \n \nIn the Stripe Model the tracking function is moved \nto the communication tier of the diagram to promote more \nfrequent customer interaction and feedback.')

    def development():
        stripe.clear()
        print('The Development Phase \n \nThe Modling and Construction phases are combined \nto facilitate faster development life cycles. \n  \nAn explicit design review is included to provide feedback and \ninput from stakeholders.')

    def stripe_model():
        stripe.communication()
        input('\nPress enter to continue...')
        stripe.development()
        input('\nPress enter to continue...')
        stripe.clear()
        print('This program will close in five seconds, thank you and good bye!')
        time.sleep(5)
        exit()

    def question():
        stripe.clear()
        response = input('Do you want to learn about the Stripe Model Y/N?: ')

        if (response == 'Y' or response == 'y'):
            stripe.stripe_model()
        else:
            print('Awe shucks, have a good day.')
            exit()

stripe.question()
