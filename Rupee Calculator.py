"""
Name: Rupee Calculator
Author: Charlotte
Date: 28/02/2019
Description:
"""
#Variables
RN = ["1","2","3","4","5","6","7","8","9"]
RT = ["Green ","Blue ","Yellow ","Red ","purple ","Orange ","Silver "]
RS = "You have "
RI = 0
counter = 0
INV = True

#
while INV:
    print("Enter RI between 1 and 999")
    RI = int(input())
    if RI > 999 or RI == 0:
        print("Invalid number.")
    else:
        INV = False

#sr
INV = True
while INV:
    if RI >= 200:
        RI = RI - 200
        counter = counter + 1
    elif RI < 200:
        INV = False

if counter == 1:
    RS = RS + RN[0] + " " + RT[6] + "Rupee"
elif counter == 2:
    RS = RS + RN[1] + " " + RT[6] + "Rupees"
elif counter == 3:
    RS = RS + RN[2] + " " + RT[6] + "Rupees"
elif counter == 4:
    RS = RS + RN[3] + " " + RT[6] + "Rupees"

if RI == 0:
    RS = RS + "."
elif RI > 0 and counter == 0:
    RS = RS
elif RI > 0:
    RS = RS + ", "


#or
counter = 0
INV = True
while INV:
    if RI >= 100:
        RI = RI - 100
        counter = counter + 1
    elif RI < 100:
        INV = False

if counter == 1:
    RS = RS + RN[0] + " " + RT[5] + "Rupee"
elif counter == 2:
    RS = RS + RN[1] + " " + RT[5] + "Rupees"
elif counter == 3:
    RS = RS + RN[2] + " " + RT[5] + "Rupees"
elif counter == 4:
    RS = RS + RN[3] + " " + RT[5] + "Rupees"

if RI == 0:
    RS = RS + "."
elif RI > 0 and counter == 0:
    RS = RS
elif RI > 0:
    RS = RS + ", "

#pr
counter = 0
INV = True
while INV:
    if RI >= 50:
        RI = RI - 50
        counter = counter + 1
    elif RI < 50:
        INV = False

if counter == 1:
    RS = RS + RN[0] + " " + RT[4] + "Rupee"
elif counter == 2:
    RS = RS + RN[1] + " " + RT[4] + "Rupees"
elif counter == 3:
    RS = RS + RN[2] + " " + RT[4] + "Rupees"
elif counter == 4:
    RS = RS + RN[3] + " " + RT[4] + "Rupees"

if RI == 0:
    RS = RS + "."
elif RI > 0 and counter == 0:
    RS = RS
elif RI > 0:
    RS = RS + ", "
    
#rr
counter = 0
INV = True
while INV:
    if RI >= 20:
        RI = RI - 20
        counter = counter + 1
    elif RI < 20:
        INV = False

if counter == 1:
    RS = RS + RN[0] + " " + RT[3] + "Rupee"
elif counter == 2:
    RS = RS + RN[1] + " " + RT[3] + "Rupees"
elif counter == 3:
    RS = RS + RN[2] + " " + RT[3] + "Rupees"
elif counter == 4:
    RS = RS + RN[3] + " " + RT[3] + "Rupees"

if RI == 0:
    RS = RS + "."
elif RI > 0 and counter == 0:
    RS = RS
elif RI > 0:
    RS = RS + ", "
    
#yr
counter = 0
INV = True
while INV:
    if RI >= 10:
        RI = RI - 10
        counter = counter + 1
    elif RI < 10:
        INV = False

if counter == 1:
    RS = RS + RN[0] + " " + RT[2] + "Rupee"
elif counter == 2:
    RS = RS + RN[1] + " " + RT[2] + "Rupees"
elif counter == 3:
    RS = RS + RN[2] + " " + RT[2] + "Rupees"
elif counter == 4:
    RS = RS + RN[3] + " " + RT[2] + "Rupees"

if RI == 0:
    RS = RS + "."
elif RI > 0 and counter == 0:
    RS = RS
elif RI > 0:
    RS = RS + ", "
    
#br
counter = 0
INV = True
while INV:
    if RI >= 5:
        RI = RI - 5
        counter = counter + 1
    elif RI < 5:
        INV = False

if counter == 1:
    RS = RS + RN[0] + " " + RT[1] + "Rupee"
elif counter == 2:
    RS = RS + RN[1] + " " + RT[1] + "Rupees"
elif counter == 3:
    RS = RS + RN[2] + " " + RT[1] + "Rupees"
elif counter == 4:
    RS = RS + RN[3] + " " + RT[1] + "Rupees"

if RI == 0:
    RS = RS + "."
elif RI > 0 and counter == 0:
    RS = RS
elif RI > 0:
    RS = RS + ", "

#gr
counter = 0
INV = True
while INV:
    if RI >= 1:
        RI = RI - 1
        counter = counter + 1
    elif RI < 1:
        INV = False

if counter == 1:
    RS = RS + RN[0] + " " + RT[0] + "Rupee"
elif counter == 2:
    RS = RS + RN[1] + " " + RT[0] + "Rupees"
elif counter == 3:
    RS = RS + RN[2] + " " + RT[0] + "Rupees"
elif counter == 4:
    RS = RS + RN[3] + " " + RT[0] + "Rupees"

if RI == 0:
    RS = RS + "."
elif RI > 0 and counter == 0:
    RS = RS
elif RI > 0:
    RS = RS + ", "

print(RS)

