#!/usr/bin/python
# File: main.py
import os
import pygubu

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


class App:
    def __init__(self):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file(os.path.join(CURRENT_DIR, 'main.ui'))

        # 3: Create the toplevel widget.
        self.main_window = builder.get_object('main_window')

        self.builder.connect_callbacks(self)

    def add_player(self):
        print('add player')

    def quit(self, event=None):
        self.main_window.quit()

    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
