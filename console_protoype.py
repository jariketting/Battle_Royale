import time
from Controller import Controller

clear = "\n" * 100


class App:
    _run = True
    _state = 'main_menu'
    _controller = Controller()

    def __init__(self):
        self.splash_screen()

        while self._run:
            print(clear)
            self.show_actions()
            user_input = input()

            if self._state == 'main_menu':
                if user_input == 'start':
                    if len(self._controller.get_players()) > 2:
                        print(clear)
                        print('Game started')
                        time.sleep(3)
                    else:
                        print(clear)
                        print('Please add a minimum of two players.')
                        time.sleep(3)
                elif user_input == 'add_player':
                    self.add_player()

            if user_input == 'quit':
                self._run = False

    def splash_screen(self):
        print(clear)
        print('Welcome to Board Royale!')
        time.sleep(3)

    def show_actions(self):
        print('Please use any of the following actions:')

        if self._state == 'main_menu':
            print('add_player, start, quit')

    def add_player(self):
        print(clear)
        print('Enter name of player')

        name = input()

        self._controller.add_player(name)
        print('Added ' + name)


if __name__ == '__main__':
    app = App()
