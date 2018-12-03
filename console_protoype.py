import time
from Controller import Controller

clear = "\n" * 100


class App:
    state = 'splash_screen'
    run = True
    controller = Controller()

    def __init__(self):
        while self.run:
            if self.state == 'splash_screen':
                self.splash_screen()

            elif self.state == 'main_menu':
                self.main_menu()

            elif self.state == 'game':
                self.game()

    def splash_screen(self):
        print(clear)
        print('Welcome to Board Royale!')
        time.sleep(3)
        print(clear)
        self.state = 'main_menu'

    def main_menu(self):
        run = True

        while run:
            print(clear)

            print('> main menu')
            if len(self.controller.get_players()) > 0:
                print('Current players:')

                for idx, player in enumerate(self.controller.get_players()):
                    print(idx, ' ', player.get_name())

            else:
                print('No players added yet.')

            user_input = input('Type an action')

            if user_input == 'quit':
                run = False
                self.run = False

            elif user_input == 'help':
                print('Commands allowed: start, quit, add player.')
                input('Press enter to continue...')

            elif user_input == 'add player':
                if len(self.controller.get_players()) < 8:
                    name = input('Type the name of the player')

                    self.controller.add_player(name)
                else:
                    print('Maximum players reached.')
                    input('Press enter to continue...')

            elif user_input == 'start':

                if len(self.controller.get_players()) >= 2:
                    self.state = 'game'
                    run = False

                else:
                    print('Please add a minimum of two players.')
                    input('Press enter to continue...')

            else:
                print('Invalid input. Use "help" to show allowed inputs.')
                input('Press enter to continue...')

    def game(self):
        run = True

        while run:
            print(clear)
            print('> game')
            print('')
            print('Current round: ', self.controller.get_round())
            print('------------------------------')
            print('Players:')
            for idx, player in enumerate(self.controller.get_players()):
                print('- ', player.get_name(), ' | HP: ', player.get_hp(), ' | Armor: ', player.get_armor(),)

            user_input = input('Type an action')


if __name__ == '__main__':
    app = App()
