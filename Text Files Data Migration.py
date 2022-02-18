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
    
    with open(currentMem,'r+') as members_register: 
            with open(exMem,'a+') as inactive_mem_register:

                # get the data
                members_register.seek(0)

                lines = members_register.readlines()

                #removes header
                header = lines[0]
                lines.pop(0)


                # get list of inactive members
                inactive = [line for line in lines if ('no' in line)]


                # go to the beginning of the members register
                members_register.seek(0) 
                
                # write-in header again
                members_register.write(header)

                # write active members to members_register and inactive members to inactive_mem_register
                for line in lines:
                    if (line in inactive):
                        inactive_mem_register.write(line)
                    else:
                        members_register.write(line)      
                members_register.truncate()   


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