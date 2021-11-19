myData=['apel', 'rambutan', 'jeruk ']
def sortStringByChar(myData):
    Data= sorted(myData, reverse=True, key = len)
    return Data

print('myData=', sortStringByChar(myData))

