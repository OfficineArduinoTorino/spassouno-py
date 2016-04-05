import termios
import select
import sys
import tty


class KeyManager(object):
    def __init__(self):
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    def __del__(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def read_key(self):
        if self.__is_data():
            k = sys.stdin.read(1)
            # Exteded key (Up, Down, ...)
            if ord(k) == 27:
                k += sys.stdin.read(2)
            return k
        else:
            return ''

    def __is_data(self):
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

if __name__ == '__main__':
    import time

    km = KeyManager()
    k = ''
    while k <> 'q':
        k = km.read_key()
        print "k = {0}".format(k)
        time.sleep(0.5)



