L1 = [500,800,600,200,900]
START = 1
SUM = 0
for C in range(START,4):
    SUM = SUM + L1[C]
    print(C,":",SUM)
    SUM = SUM + L1[0]*10
    print(SUM)