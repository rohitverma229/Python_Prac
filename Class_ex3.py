class OldClass():
    def __init__(self):
        print('I am an old class')

class NewClass(object):
    def __init__(self):
        print('I am a jazzy new class')

old = OldClass()
# Output: I am an old class

new = NewClass()
# Output: I am a jazzy new class
