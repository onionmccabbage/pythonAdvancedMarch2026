# Python can access remote API over http(s)
# you may need to pip install requests
import requests

class APIAccess():
    '''This class will expose methods to access remote API data'''
    def __init__(self):
        pass
    def getAllData(self):
        apiURL = 'https://jsonplaceholder.typicode.com'
        try:
            # request all the photos as JSON
            # NB this is asynchronous, but the requsts library will wait
            # this is an example of I/O bound code
            response = requests.get(f'{apiURL}/photos')
            # grab the data from the response object
            data = response.json() # or .raw() etc.
            # NB by default Python will .......
            return data
        except Exception as err:
            print(err)
    def getOneData(self):
        pass


if __name__ == '__main__':
    # make instances of our class and use them to grab API data
    a = APIAccess()
    d = a.getAllData()
    print(d, type(d))