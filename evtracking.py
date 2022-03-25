import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt 

filedata = pd.read_excel('v2.xlsx')

names = filedata['current'].values.tolist() # array creation from excel
count = 0 # used to iterate loop
moddata = [] # data after removing zeros
isZero = 0 #counts 8 zeros in a row
zeroRows = 0 # Counts how many isZero is there

# print (int(names))

while(count < len(names)):
    if (names[count]) == 0:
        print(count) # iterate number printing to debug problems
        isZero = isZero + 1
        if isZero > 8: # assuming it takes 8 zeros to stop while de-accelerating
            zeroRows = zeroRows + 1
            isZero = 0
            if (names[count+1]) == 0:
                isZero = 0  #reset zero count 0
                continue
    else:
        moddata.append((names[count]))
    count = count + 1

print("okay first loop done")
print(moddata)

length = len(moddata)
onSeconds = int(length*2)
zerothSeconds = zeroRows*8*2

onSeconds = onSeconds + zerothSeconds

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)
    

print("Total on time: ", convert(onSeconds))

# assuming speed = 19 kilometers per hour

speed = 19 # kilometers per hour

dist = (onSeconds/(speed*3600))

print("Average distance covered: ", dist) # accilaration negotiated | to be found out using current values
print("number of 8 zero stacks are", zeroRows)

# plotting graph of speed with help of current's values

# y = np.array(names)
# plt.title("Plotting 1-D array")
# plt.ylabel("Y axis")
# plt.plot(y, color = "red", marker = "o", label = "Array elements")
# plt.legend()
# plt.show()
