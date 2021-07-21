from os import error
import sys
try:
    FILE_ = open(sys.argv[1],"r").readlines()
except:
    FILE_ = open("main.ccs","r").readlines()
VA = 0
VB = 0
VC = 0
debug = False
FILE = []
for line in FILE_:
    FILE.append(line.replace("\n",""))
if debug:
    print(FILE)
if FILE[0] == "LP MAN":
    loop = 1
elif FILE[0] == "LP INF":
    loop = 0
    if FILE[1][0] == "-":
        print(FILE[1][1:])
        del FILE[1]
else:
    raise error("No loop defined!")
del FILE[0]
while True:
    for line in FILE:
        STRIP = line[0:3]
        if STRIP == "STA":
            VA = float(line[4:])
        elif STRIP == "STB":
            VB = float(line[4:])
        elif STRIP == "STC":
            VC = float(line[4:])
        elif STRIP == "ISA":
            VA = float(input("A=>"))
        elif STRIP == "ISB":
            VB = float(input("B=>"))
        elif STRIP == "ISC":
            VC = float(input("C=>"))
        elif STRIP == "A++":
            VA += 1
        elif STRIP == "B++":
            VB += 1
        elif STRIP == "C++":
            VC += 1
        elif STRIP == "A--":
            VA -= 1
        elif STRIP == "B--":
            VB -= 1
        elif STRIP == "C--":
            VC -= 1   
        elif STRIP == "A+B":
            VA += VB
        elif STRIP == "A+C":
            VA += VC
        elif STRIP == "A-B":
            VA -= VB
        elif STRIP == "A-C":
            VA -= VC
        elif STRIP == "B+A":
            VB += VA
        elif STRIP == "B+C":
            VB += VC
        elif STRIP == "B-A":
            VB -= VA
        elif STRIP == "B-C":
            VB -= VC
        elif STRIP == "C+A":
            VC += VA
        elif STRIP == "C+B":
            VC += VB
        elif STRIP == "C-A":
            VC -= VA
        elif STRIP == "C-B":
            VC -= VB
        elif STRIP == "A*B":
            VA *= VB
        elif STRIP == "A*C":
            VA *= VC
        elif STRIP == "A/B":
            VA /= VB
        elif STRIP == "A/C":
            VA /= VC
        elif STRIP == "B*A":
            VB *= VA
        elif STRIP == "B*C":
            VB *= VC
        elif STRIP == "B/A":
            VB /= VA
        elif STRIP == "B/C":
            VB /= VC
        elif STRIP == "C*A":
            VC *= VA
        elif STRIP == "C*B":
            VC *= VB
        elif STRIP == "C/A":
            VC /= VA
        elif STRIP == "C/B":
            VC /= VB
        elif STRIP == "A^B":
            VA **= VB
        elif STRIP == "A^C":
            VA **= VC
        elif STRIP == "ASQ":
            VA **= (1/2)
        elif STRIP == "B^A":
            VB **= VA
        elif STRIP == "B^C":
            VB **= VC
        elif STRIP == "BSQ":
            VB **= (1/2)
        elif STRIP == "C^A":
            VC **= VA
        elif STRIP == "C^B":
            VC **= VC
        elif STRIP == "CSQ":
            VC **= (1/2)
        elif STRIP == "MIN":
            exec("%s= min(%s,%s)" % (line[4:6],line[4:6],line[7:9]))
        elif STRIP == "MAX":
            exec("%s= max(%s,%s)" % (line[4:6],line[4:6],line[7:9]))
        elif STRIP == "MEN":
            exec("%s = (%s+%s)/2" % (line[4:6],line[4:6],line[7:9]))
        elif STRIP == "CLR":
            try:
                import os
                os.system("cls")
            except:
                try:
                    import os
                    os.system("clear")
                except:
                    pass
        elif STRIP == "END":
            I = input("[E] -> {Enter} to end: ").lower()
            if I == "e":
                loop = 1
                break
        else:
            print(line.replace(">A",str(float(VA))).replace(">B",str(float(VB))).replace(">C",str(float(VC))))
    if loop == 1: break
