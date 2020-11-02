import time

class BubbleSort:
    
    time_elapsed=0
    passes = 0

    def __init__(self,data,reverse=False):
        self.bubbleSort(data,reverse)

    def swap(self,a,b):
        a,b = b, a
        return a,b

    def bubbleSort(self,data,reverse):
        while(True):
            swap_count=0
            start = time.time()
            for x in range(len(data)-1):
                if reverse == False:
                    if data[x]>data[x+1]:
                        data[x],data[x+1] = self.swap(data[x],data[x+1])
                        swap_count += 1
                else:
                    if data[x]>data[x+1]:
                        data[x],data[x+1] = self.swap(data[x],data[x+1])
                        swap_count += 1
            self.passes += 1


            if swap_count == 0:
                self.time_elapsed=time.time()-start
                break

        return data

if __name__=='__main__':
    data=[2,6,3,1,5,8,9]
    passes=BubbleSort(data)
    print(passes.passes)
    print(passes.time_elapsed)

    
            



        
