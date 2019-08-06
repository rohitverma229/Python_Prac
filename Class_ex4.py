class GetTest(object):
    def __init__(self):
        print('Greetings!!')
    def another_method(self):
        print('I am another method which is not'
              ' automatically called')

a = GetTest()
# Output: Greetings!!

a.another_method()
# Output: I am another method which is not automatically
# called
