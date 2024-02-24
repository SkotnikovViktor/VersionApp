#import pynput
#
#while True:
#    keyboard_listen = pynput.keyboard.Listener(suppress=True)
#    keyboard_listen.start()

# Создаём список со всеми возможными клавишими
key = ['q','w','e','r','t','y','u','i','o','p',
       'a','s','d','f','g','f','h','j','k','l',
       'z','x','c','v','b','n','m'
       ,'0','1','2','3','4','5','6','7','8','9','shift','ctrl','alt','windows','esc','backspace','-','+','*','/','[',']','{','}','enter','tab','~'
       ,'|','capslock','(',')','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','delete']

# Импорт пакета для блока нужных клавиш
import keyboard

# Запускаем вечный цикл для того, чтобы for всегда проходил по списку и клавиши блокались
while True:
    # Ложу в переменную i все значения по порядку из списка key
    for i in key:
        # Блокирую, все клавиши, которые перибераются в цикле for выше!
        keyboard.block_key(i)







