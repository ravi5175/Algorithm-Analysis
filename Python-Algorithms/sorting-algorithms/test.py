import random
import datetime

from bubbleSort import BubbleSort

class Test:
    #res=['name','length','order' : rand,sort,reversed, time_taken, passes] 
    sample_data = []
    passes = 0
    available_sort=['bubble_sort']

    def __init__(self, length=100, sample_range=None, sorted=False,reverse=False):
        if sample_range is None:
            self.sample_data = random.sample(range(100,1000),length)
            if sorted == True and reverse == True:
                self.sample_data.sort(reverse=True)
            if sorted == True and reverse == False:
                self.sample_data.sort()
            self.call_test()
        else:
            self.sample_data = random.sample(range(sample_range),length)
            if sorted == True and reverse == True:
                self.sample_data.sort(reverse=True)
            if sorted == True and reverse == False:
                self.sample_data.sort()
            self.call_test()
                
    def call_test(self):
        res = BubbleSort(self.sample_data)
        self.export_metrics(res.passes)



    def export_metrics(self,res):
        pass