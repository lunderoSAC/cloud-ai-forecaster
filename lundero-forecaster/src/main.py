import sys
from base64 import b64decode as decoder

from tornado.ioloop import IOLoop

from urls import App

if __name__ == '__main__':
    print(f'Python: {sys.version}')
    with open('lundero', 'r') as f:
        print(decoder(f.readline()).decode('utf8'),
              end='\n')
    print('\n Iniciando IA-Forecaster')

    app = App()
    app.listen(8000, '0.0.0.0')
    IOLoop.current().start()
