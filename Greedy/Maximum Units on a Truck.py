class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # Sort the box types with the number of units per box in descending order
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        
        total_units = 0
        for i, unit in boxTypes:
            total_units += min(i, truckSize) * unit
            truckSize -= i
            
            # Check if there is an available space left in truck
            if truckSize > 0: continue
            else: break
                
        return total_units
      
