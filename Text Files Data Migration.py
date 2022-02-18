# exercise to create a function which takes all inactive members from a register and moves it to
# a register of inactive members only, so that the active register lists all active members only
# and the register of inactive members contains the inactive members only.



# this code section was already provided for generating the text files for the exercise.
# skip below to def of function cleanFiles for developed code.
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)
# end of file generation for text files exercise.





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
