# -*- coding: utf-8 -*-

#廖雪峰python教学
#编写函数得到方程ax^2+bx+c=0的解

import math

def quadratic(a, b, c):
    if not isinstance(a,(int,float)) :
        print('Error input!')
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('no x satisify the formula!')
        elif delta > 0 :
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            return x1,x2
            
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
    
    
    
    
    
