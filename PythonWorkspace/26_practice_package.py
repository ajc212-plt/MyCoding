#패키지

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.vietnamPackage()
# trip_to.detail()

# from random import *
from travel import *
# trip_to = vietnam.vietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) #랜덤의 위치가 어디 있는지 확인
print(inspect.getfile(thailand))
