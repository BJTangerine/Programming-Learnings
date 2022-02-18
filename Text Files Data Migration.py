# exercise to create a function which takes all inactive members from a register and moves it to
# a register of inactive members only, so that the active register lists all active members only
# and the register of inactive members contains the inactive members only.

def cleanFiles(currentMem,exMem):
    '''
    currentMem: File containing list of current members
    exMem: File containing list of old members
    
    Removes all rows from currentMem containing 'no' and appends them to exMem
    '''
    
    with open(currentMem,'r+') as writeFile: 
            with open(exMem,'a+') as appendFile:
                # get the data
                writeFile.seek(0)
                members = writeFile.readlines()
                #removes header
                header = members[0]
                members.pop(0)

                # get list of inactive members
                inactive = [member for member in members if ('no' in member)]

                # go to the beginning of the write file
                writeFile.seek(0) 
                # write-in header again
                writeFile.write(header)

                # write active members to writeFile and inactive members to appendFile
                for member in members:
                    if (member in inactive):
                        appendFile.write(member)
                    else:
                        writeFile.write(member)      
                writeFile.truncate()   


# code for viewing results
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())