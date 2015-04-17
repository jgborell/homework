def fh_fileopen(text):
    try:
        fh = open(text,'r')
    except IOError:
        print "Error: can't find file or read data"
    else:
        print "File opened successfully"

def no_fh_fileopen(text):
    fh = open(text, 'r')

try:
    no_fh_fileopen("filename.txt")
except IOError:
    print "Can not find file or read data"
else:
    print "File opened successfullY"

fh_fileopen("filename.txt")
