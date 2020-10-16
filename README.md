# information_collection_system

##Настройка сервера
1)Клонирование репозитория
```
git clone https://github.com/Borutia/information_collection_system.git
```
2)Создание и активация виртуальной среды
```
sudo apt install -y python3-venv
python3 -m venv env
source env/bin/activate
```
3)Установка пакетов:
```
pip install -r requirements.txt
```
4)Запуск сервера flask
```
1. Если порт дефолт (5000)
flask run

2. Если нужно на определенном порте 
flask run -p 8001
```
5)Открыть front/index.html
```
Если порт не 8001, зайти в front/js/config.js и поменять на нужный порт 
```

##Настройка клиент-демона
1)Перейти в каталог information_collection_system
2)Запустить клиент-демон
```
1. Если порт дефолт 8001
python client.py

2. Если нужно на определенном порте 
python client.py 5000
```
3)Остановка клиент-демона
```
start-stop-daemon -Kvx pid_file.pid
```