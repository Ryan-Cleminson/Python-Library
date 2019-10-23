#############################################################################
# Author: Ryan Cleminson (Ryan.Cleminson@student.uts.edu.au)
# Date: 6/10/19
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
    Name = str(raw_input())
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
#   Selection Sort names
#############################################################################

NumOfUnsortedNames = len(Names)
while NumOfUnsortedNames > 0:
    i = 0
    Maximum = Names[i]
    MaximumPos = i
    while i < NumOfUnsortedNames:
    
        print(Names)
        print(Maximum)
        print(MaximumPos)
        print(i)

        if Names[i] > Maximum:
            Maximum = Names[i]
            MaximumPos = i

        i = i + 1        
    Swap(Names[MaximumPos], Names[NumOfUnsortedNames-1])
    NumOfUnsortedNames = NumOfUnsortedNames - 1