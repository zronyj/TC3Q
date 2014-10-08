K = [7.5E-3, 6.2E-8, 4.8E-13]
f = open("diagrama.csv","w")
for i in xrange(0,141,5):
    ctrl = [0]*4
    for j in xrange(len(K) + 1):
        if j > 1:
            ctrl[j] = K[j-1]*ctrl[j-1]/(K[j-1] + 10**(i*-0.1))
            ctrl[j-1] -= ctrl[j]
        elif j == 1:
            ctrl[j] = K[j-1]/(K[j-1] + 10**(i*-0.1))
            ctrl[j-1] -= ctrl[j]
        else:
            ctrl[j] = 1
    result = str(i*0.1)
    for k in ctrl:
        result += " " + str(k)
    f.write(result + "\n")
f.close()
