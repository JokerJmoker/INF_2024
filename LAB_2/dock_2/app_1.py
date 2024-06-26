from flask import Flask # импорт фрейворка FLASK (т.е класс из библиотеки flask)

app = Flask(__name__) # создаем экземпляр на основе класса FLASK , в которм содержится имя текущего модуля 

@app.route('/') # связываем функцию с url адресом . Т.е она ( funct ) вызывается когда отправляется запрос по url адресу (открываем старницу например ) 
def funct():
    return 'Слоняра ... '

"""
# вообще эта строка имеет смылс с точки зрения ИБ. В нашем случае, ее можно опустить , однако в более сложных задачах она уместна 
if __name__ == '__main__': # здесь мы проверяем, является ли текущий модуль основным, т.е запущен ли он напрямую ( python app_1.py  (выполняется как самостоятельное приложение )) или посредством импорта в другой модуль и т.д)

    app.run(debug=True, host='0.0.0.0', port=5000) # Обеспечение возможности слушать все интерфейсы и запросы на порту 5000
"""
app.run(debug=True, host='0.0.0.0', port=5000) # Применяем метод app.run() запускаем сервер Flask в режиме отладки (debug=True), что позволяет  автоматичеаски презапускать сервер , host с прееданными пармаетрыми позволяет слушать все сетевые интерфейсы(зайти с телефона например) , порт 5000 - порт, на котором вы запускаем веб-сервер 