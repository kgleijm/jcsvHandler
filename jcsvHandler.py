import csv
import json
import os
import urllib.request
import pandas as pd

# print json
def printJson(inp_json):
    for e in inp_json:
        print(e)

# get json from web method
def getJsonFromAdress(adress):
    if 'http:' in adress:
        with urllib.request.urlopen(adress) as url:
            return json.loads(url.read().decode())
    else:
        with open(adress) as inp_json:
            data = json.load(inp_json)
            return data

# save json at path method
def saveJsonAtPath(path, filename, outputJson):
    with open(path + '\\' + filename + '.json', 'w') as outfile:
        json.dump(outputJson, outfile)

# get csv from web or path method
def getCsvAsList(adress, delimiter):
    output = list()
    print('\n')
    if 'http:' in adress:
        print('try to get csv from webadress: ' + adress)
        response = pd.read_csv(adress)
        for e in response:
            x = e.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace('\'', '')
            x = x.replace(')', '').replace('(', '').replace(':', '').replace(']', '').replace('[', '')
            x = x.replace('"', '').replace('\'', '')
            print(x)
            output.append(x)
    else:
        print('try to get csv from local path: ' + adress)
        f = open(adress, 'r')
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            print('found row:' + str(row))
            thisRow = list()
            for e in row:
                thisRow.append(e)
            output.append(thisRow)
        f.close()
    print('\n')
    return output

# save csv at path method
def saveAsCsvAtPath(adress, filename, iterable):

    outpath = adress + '\\' + filename + '.csv'
    print('\n jcsvHandler will try to save at' + outpath)

    try:
        os.mkdir(adress)
        print('made directory ' + adress)
    except FileExistsError:
        print('directory does already exist, will write to existing file')

    try:
        f = open(outpath, 'w')
        writer = csv.writer(f)
        writer.writerows([iterable])
        f.close()
        return outpath
    except PermissionError:
        print("cant write to file, might already be open somewhere\n")

def saveTextAtPath(path, filename, string):
    try:
        os.mkdir(path)
        print('directory created')
    except:
        pass
    with open(path + '\\' + filename + '.txt', 'w') as outfile:
        outfile.write(string)

def loadTextFromPath(path):
    with open(path) as f:
        return f.readlines()

