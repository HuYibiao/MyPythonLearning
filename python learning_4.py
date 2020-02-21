'''
python learning
面向对象编程
学习使用类，以及如何定义类
'''

class Student(object):
    '''
      这里的self其实就是对象，它属于Student这一个大类，name和score是它的属性
      尝试添加了第三个可变变量birthplace，这一项变量有无对对象的定义不产生实际影响
    '''
    def __init__(self, name, score, birthplace='unknown_birthplace'):
        self.name = name
        self.score = score
        self.birthplace = birthplace

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 75:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'D'


hyb = Student('hyb', 100)
grade_hyb = hyb.get_grade()
'''调用函数时要指定对象'''

hpx = Student('hpx', 30, 'zhengzhou')
grade_hpx = hpx.get_grade()

print('Student name: %s, Student grade:%s'%(hyb.name, grade_hyb))
print('Student name: %s, Student grade: %s, Birthplace: %s' % (hyb.name, grade_hpx, hpx.birthplace))

