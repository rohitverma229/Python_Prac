class GetTest(object):
    def __init__(self):
        self.info = {'name':'Rohit','country':'India','number':12345812}

    def __getitem__(self,i):
        return self.info[i]

foo = GetTest()

foo['name']
# Output: 'Rohit'
foo['country']
#foo['number']
# Output: 12345812
