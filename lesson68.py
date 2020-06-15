#import lesson_package.utils

#r = lesson_package.utils.say_twice('hello')

#print(r)

from lesson_package import utils
r = utils.say_twice('hello')
print(r)

from lesson_package.talk import human
print(human.sing())
print(human.cry())