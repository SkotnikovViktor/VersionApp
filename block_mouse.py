import pynput
while True:
    mouse_listen = pynput.mouse.Listener(suppress=True)
    mouse_listen.start()
