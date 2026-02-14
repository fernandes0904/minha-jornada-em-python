import math
import random 
ang = random.randint(0,90)
print('O ângulo é {}'.format(ang))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Seno é {0}\nCosseno é {1}\nTangente é {2}'.format(seno,coss,tang))


