# Импорт библиотеки для считывания названия процкессора и так далее
import platform

# Функция по узнаванию имя процессора
def name_processor():
    name = platform.processor()
    return name

# Узнаём название нашеё ОП системы
def name_os():
    name_os = platform.system()
    return name_os

def name_pc():
    name_user_os = platform.node()
    return name_user_os

name_os()

