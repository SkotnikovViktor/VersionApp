import pynput
a = open('block_board.txt', 'w')
ab = a.read()
a.close()
while a=='0':
    keyboard_listen = pynput.keyboard.Listener(suppress=False)
    keyboard_listen.stop()