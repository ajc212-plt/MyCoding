# 모듈 theater_module.py
# import theater_module
# theater_module.price(3) #3명이서 일반 영화 가격
# theater_module.price_morning(4) #4명이서 조조할인
# theater_module.price_soldier(5) #5명이서 군인할인

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_soldier(4)
# price_morning(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7)

from theater_module import price_soldier as price
price(5)