#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Shane McLeod, 2022-Nov-13, apapted file for dictionaries
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
dicTbl = [] # replace list of lists with list of dicts
dicRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Loading existing data
        dicTbl = []
        dicRow = []
        objFile = open(strFileName, 'r')
        for row in objFile:
            objRow = row.strip().split(',')
            dicRow = {'id': objRow[0], 'title': objRow[1], 'artist': objRow[2]}
            dicTbl.append(dicRow)
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add datax
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': strID, 'title': strTitle, 'artist': strArtist}
        dicTbl.append(dicRow)
        print()
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in dicTbl:
            print(*row.values(), sep = ', ')
        print()
    elif strChoice == 'd':
        rowDel = int(input('Row # you would like to delete: '))
        rowDelPython = rowDel-1
        try:
            del dicTbl[rowDelPython]
            for row in dicTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
            print()
        except:
            print('The row # you entered does not exist.')
            print()
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'r+')
        objFile.truncate(0)
        for row in dicTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

