import threading
from pynput import keyboard
from pynput.keyboard import Key, KeyCode


class tester(threading.Thread):
    def __init__(self):
        super(tester, self).__init__()

    def function_x(self):
        print('hiii')

    def on_press(self, key):
        # handle pressed keys
        pass

    def on_release(self, key):
        # handle released keys
        if key == Key.enter or key == KeyCode.from_char('a'):
            self.function_x()
        if key == Key.esc:
            return False

    def run(self):
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()


if __name__ == "__main__":
    listenr = tester()
    listenr.start()
