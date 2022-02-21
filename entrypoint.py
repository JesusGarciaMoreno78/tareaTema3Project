from app import create_app

if __name__ == '__main__':
    app = create_app() #instancio la clase create_app() definida en app>_init_.py
    app.run()
