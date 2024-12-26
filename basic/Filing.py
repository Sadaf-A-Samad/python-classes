x = input('Enter your text for File: ')

try:
    f = open('myfile2.txt', 'a')
    print(f.read())
except:
    print('File does not exist. Please create file first.')
