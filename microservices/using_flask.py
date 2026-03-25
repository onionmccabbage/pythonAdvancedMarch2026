# we may use the Flask library for basic web content
# you may need to pip isntall flask
from flask import Flask


def main():
    '''declare and run a Flask server (a microservice)'''
    app = Flask('my_server')
    # we declare routes
    @app.route('/') # this is the root
    def root():
        return 'Welcome to our Flsk microservice'

    # we call the flask server into being like this
    app.run()

if __name__ == '__main__':
    main()