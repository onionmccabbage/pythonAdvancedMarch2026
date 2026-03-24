# working with JSON data
import json # this library is available for working with JSON data
import sys
# NB JSON is plain human readable text
# JSON is NOT JavaScript
# append a new location to sys.path list (this will depend on where you put your JSON file)
sys.path.append('d:\\pythonAdvancedMarch2026\\review2') # python will look in this location for file  access

def createJSON(struct):
    '''convert a Python structure into JSON text'''
    j = json.dumps(struct) # convert the Python structure into plain text JSON
    return j

def makeStruct(text):
    '''convert text which is JSON into a Python structure'''
    s = json.loads(text) # convert the JSON text into a Python structure

def readJSON():
    '''read JSON from a text file'''
    try:
        with (open('todos.json', 'rt')) as fin: # we have a file access object
            f = json.load(fin)
            return f # the text will be automatically converted to a Python structure
    except Exception as err:
        print(err)

if __name__ == '__main__':
    '''exercise this module'''
    results = readJSON()
    print(results, type(results))