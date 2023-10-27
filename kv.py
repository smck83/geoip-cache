import dbm
#import semidbm as dbm
import random

dbName = "data/geoipcache"
valid_chars = "0123456789abcdefghijklmnopqrstuvwxyz"

def initialize():
    with dbm.open(dbName, 'c') as db:
        if "init" in db:
            "initialized"

def keyExists(key):
    with dbm.open(dbName, 'r') as db:
        if key in db:
            return True
        else:
            return False


def keyGen(length:int=5):
    random_letters = ""
    for i in range(length):
        random_letter = random.choice(valid_chars)
        random_letters += random_letter
    return random_letters

def genUniqueKey(length:int=5):
    key = keyGen(length)
    print(key)
    while keyExists(key) == True:     
        key = keyGen(length)
        print(key)
    return key
        
def addKey(key,url):
    with dbm.open(dbName, 'w') as db:
        db[key] = url 
        print(getValue(key))

def getValue(key):
    with dbm.open(dbName, 'r') as db:
        if keyExists(key) == True: 
            return str(db[key],encoding='utf-8')

def addValue(url,customkey:str=False,length:int=5):
    if customkey == False:
        key = genUniqueKey(length)
    else:
        key = customkey
    if keyExists(url) == False:  
        addKey(key,url)
        addKey(url,key)
        return(key)
    else:
        output = getValue(url)
        return(output)


            
            

#keyExists("test")
#addKey("test","sendgrid.net")
#print(getURL("test"))
#print(keyExists("test"))