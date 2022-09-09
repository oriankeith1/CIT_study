
symbol = '@'
def emailcollector(datafile):
    with open(datafile,'r') as m:
        for line in m.readlines():
            if symbol in line:
                email = line.strip()
    return email

emailcollector('myfile.txt') # extracting email in text
                
                