import numpy as np
import time


def pi(precision):
    answer = 0
    factor = 1.0
    sign = True
    percent = precision / 100
    percentage = 1
    for i in range(1,precision + 1):
        odd = np.float64(i) * 2.0 - 1.0
        change = 1.0 / odd * factor
        if sign:
            answer += change #* factor
        else:
            answer -= change #* factor
        sign = not sign
    return(4*answer)

start = time.time()
pi_n = pi(4000000000)
print( "{:.100f}".format(pi_n))
end = time.time()
print(end - start)

def pi2(precision):
    #answer = 0
    #factor = 1000000000
    #sign = 1.0
    #percent = precision / 100
    #percentage = 1

    sign = np.asarray([ [1.0,-1.0] for i in range(int(precision/2))]).ravel().astype(np.float64)
    
    factor = np.arange(1,2*precision+1,2, dtype=np.float64)
    #sign = sign[0:len(factor)]
    
    #print(sign*1.0/factor)
    
    return np.float64(4.0) * np.sum((sign*np.float64(1.0)/factor))

start = time.time()
pi_n2 = pi2(4000000000)
print( "{:.100f}".format(pi_n2))
end = time.time()
print(end - start)

print('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281')