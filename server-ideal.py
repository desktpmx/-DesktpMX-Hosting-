import http.server
import socketserver
import threading

# Устанавливаем порт, на котором будет работать сервер
PORT = 8000

# Каталог, в котором находятся файлы вашего сайта
WEB_DIR = "/"

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Замените 'index.html' на имя вашего файла главной страницы
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Запуск сервера в отдельном потоке
def run_server():
    with socketserver.ThreadingTCPServer(("192.168.1.71", PORT), MyHttpRequestHandler) as httpd:
        print("Сервер запущен и прослушивает порт:", PORT)
        httpd.serve_forever()

# Запуск сервера в отдельном потоке
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Ваш сервер теперь работает в отдельном потоке
# Вы можете продолжать выполнять другие задачи
# Например, обработка других запросов

...

# Когда закончите работу, вы можете остановить сервер
# server_thread.stop()