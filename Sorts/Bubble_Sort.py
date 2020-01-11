#############################################################################
# Author: Ryan Cleminson (Ryan.Cleminson@student.uts.edu.au)
# Date: 22/10/19
# Purpose: 
#############################################################################

#############################################################################
#   Get names for an array
#############################################################################

Names = []
Name = ""
j = 1

while Name != "//":
    print('Please Enter Name ' + str(j) + ':')
    j = j + 1
    Name = str(input())
    if Name != "//":
        Names.append(Name)

#############################################################################
#   Swap Definition
#############################################################################

def Swap(Name1, Name2):
    temp = Name1
    Name1 = Name2
    Name2 = temp
    return(Name1, Name2)

#############################################################################
#   Bubble Sort names
#############################################################################

NumNames = int(len(Names))
print(NumNames)
Swapped = True

while Swapped == True:
    Swapped = False
    i = 0
    
    while i+1 < NumNames:
        # print(Names)
        # print(i+1)
        if Names[i] > Names[i+1]:
            Names[i], Names[i+1] = Swap(Names[i], Names[i+1])
            Swapped = True
        i = i + 1
    
    # print(Swapped)

    NumNames = NumNames - 1

print(Names)
#############################################################################
#############################################################################
#############################################################################


        

    