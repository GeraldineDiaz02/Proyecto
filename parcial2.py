def resist_serie(r1,r2,r3):
    serie = r1 + r2 + r3
    return serie

def resist_paralelo(r1,r2,r3,r4):
    paralelo = 1/((1/r1)+(1/r2)+(1/r3)+(1/r4))
    return paralelo

def resist_complicada(r1,r2,r3,r4,r5):
       paso_1 = (r5*r4)/(r5+r4)
       paso_2 = r2+paso_1
       paso_3 = 1/((1/r1)+(1/paso_2)+(1/r3))
       return paso_3
