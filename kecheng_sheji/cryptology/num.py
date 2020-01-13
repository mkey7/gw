import math
sm2_P = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF', 16)
s = int(math.sqrt(sm2_P))
a = []
aa = []
for i in range(2,s):
    for ii in range(s,sm2_P):
        if i*ii%sm2_P==1:
            aa.append(i)
            aa.append(ii)

print(aa)
