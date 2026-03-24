# Python can access remote API over http(s)
# you may need to pip install requests
import requests

class APIAccess():
    '''This class will expose methods to access remote API data'''
    def __init__(self):
        # make properties available throughout the class
        self.apiURL = 'https://jsonplaceholder.typicode.com'
    def getAllData(self):
        try:
            # request all the photos as JSON
            # NB this is asynchronous, but the requsts library will wait
            # this is an example of I/O bound code
            response = requests.post(f'{self.apiURL}/photos')
            # grab the data from the response object
            data = response.json() # or .raw() etc.
            # NB by default Python will convert plain JSON to a structure (list, dict etc)
            return data
        except Exception as err:
            print(err)
    def getOneData(self, n=1): # provide a sensible default
        try:
            response = requests.get(f'{self.apiURL}/photos/{n}')
            photo = response.json()
            return photo
        except Exception as err:
            print(err)

if __name__ == '__main__':
    # make instances of our class and use them to grab API data
    a = APIAccess()
    d = a.getAllData()
    print(d, type(d))
    print(d[3], type(d[3]))
    # grab one photo
    p = a.getOneData(34)
    print(p, type(p))