class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        box=0
        for size,val in boxTypes:
            if truckSize >=size:
                box+=size*val
                truckSize-=size
            else:
                box+=truckSize*val
                break
        return box

         



        