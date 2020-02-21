
import math
count = -1
for count, line in enumerate(open("muons.txt",'r')):
    pass
count += 1
realCount = count//5

file = open("muons.txt","r")
file2 = open("Calculation Result.txt","w")

for i in range(0,realCount):
    a= file.readline()
    c= file.readline()
    str1 = file.readline()
    str2=file.readline()
    b= file.readline()

    string1 = str1.split()
    string2 = str2.split()

    def invariantMass(a, b):
        pt1 = float(a[2])
        eta1 = float(a[3])
        phi1 = float(a[4])
        m1 = float(a[5])
        pt2 = float(b[2])
        eta2 = float(b[3])
        phi2 = float(b[4])
        m2 = float(b[5])
        result = math.sqrt(2 * pt1 * pt2 * (math.cosh(eta1-eta2)-math.cos(phi1-phi2)))
        return result

    mFinal = invariantMass(string1, string2)

    finalFantasy = str(mFinal)
    file2.write(a) 
    file2.write(c)
    file2.write("Invariant Mass: "+finalFantasy)
    file2.write("\n\n")

file.close()
file2.close()

# Professor, I didn't what you mean by the "loop" on your demands list, so I just did what is expected. 
