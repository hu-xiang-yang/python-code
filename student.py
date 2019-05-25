#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
 
#object 表示由哪个类继承下来的  也是所有类最终都会继承的类
class Student(object):                                #Student类名通常是大写开头的单词
 
 
     def __init__(self, name, score):    #__init__方法的第一个属性永远是self表示创建实例的本身    
         self.name = name 
         self.score = score 
 
 
     def print_score(self):                 #类中定义的函数第一个参数必须是实例变量self
         print('%s: %s' % (self.name, self.score)) 
 
 
     def get_grade(self): 
         if self.score >= 90: 
             return 'A' 
         elif self.score >= 60: 
             return 'B' 
         else: 
             return 'C' 
 
 
bart = Student('Bart Simpson', 59)            #创建类的实例bart
lisa = Student('Lisa Simpson', 87) 
 
 
print('bart.name =', bart.name) 
print('bart.score =', bart.score) 
bart.print_score() 
 
 
print('grade of Bart:', bart.get_grade()) 
print('grade of Lisa:', lisa.get_grade()) 
