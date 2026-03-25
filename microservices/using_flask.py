# we may use the Flask library for basic web content
# you may need to pip isntall flask
from flask import Flask
from flask import render_template # this lets us work with html template files
import sys
# modify this next line dpending on your file locations
sys.path.append('D:\pythonAdvancedMarch2026')
from using_yield import makeDateTimeStamp

ts = makeDateTimeStamp() # we need an instance of the generator

def main():
    '''declare and run a Flask server (a microservice)'''
    global ts # we now have access to the ts generator
    app = Flask('my_server')
    # we declare routes
    @app.route('/') # this is the root
    def root():
        # we could do any pre-processing to garner the data we then return to the web page
        return 'Welcome to our Flask microservice'
    @app.route('/greet')
    def greet():
        now = ts.__next__()
        return (f'Welcome, the time is {now}')
    # several routes may end up showing the same content
    @app.route('/aluminium')
    @app.route('/aluminum')
    def al():
        return 'it is spelled "aluminium" '
    # we may choose to pass HTML
    @app.route('/data')
    def data():
        ''' we could retrieve some data (db file API etc.)'''
        response = '<h2>Data Goes Here</h2>'
        return response
    @app.route('/demo')
    @app.route('/demo/<person>') # here we might expect an argument
    def demo(person='Ethel'):
        return render_template('demo.html', person=person)

    # we call the flask server into being like this
    app.run()

if __name__ == '__main__':
    ts = makeDateTimeStamp()
    main()