import unittest

def TestValue_results():
    
    #5 Unit tests
    
    objeto = Solution()

    nums1 = [1,3,4,2,2]
    assert objeto.buscaDuplicado(nums1) == 2, "Should be equal to 2"
    
    nums2 = [3,1,3,4,2]
    assert objeto.buscaDuplicado(nums2) == 3, "Should be equal to 3"
    
    nums3 = [1,1]
    assert objeto.buscaDuplicado(nums3) == 1, "Should be equal to 1"
    
    nums4 = [1,1,2]
    assert objeto.buscaDuplicado(nums4) == 1, "Should be equal to 1"
    
    nums5 = [2,1,4,4,3]
    assert objeto.buscaDuplicado(nums5) == 4, "Should be equal to 4"
    
    

class Solution(object):
    
    def buscaDuplicado(self, nums):
        
        if len(nums) > 1:
            x = nums[0]
            y = nums[nums[0]]
            
            while x != y:
                x = nums[x]
                y = nums[nums[y]]
            y = 0
            
            while x != y:
                x = nums[x]
                y = nums[y]
                
            return x
        
        return -1
    

if __name__ == "__main__": 
    
    TestValue_results()
    print("\nAll test cases passed\n")

objeto = Solution()

#Primeros 4 ejemplos son los mismos del ejercicio
nums1 = [1,3,4,2,2]
output1 = objeto.buscaDuplicado(nums1)
print("\nExample 1: \n")
print("Input: ", nums1, "\nOutput: ", output1)

nums2 = [3,1,3,4,2]
output2 = objeto.buscaDuplicado(nums2)
print("\nExample 2: \n")
print("Input: ", nums2, "\nOutput: ", output2)

nums3 = [1,1]
output3 = objeto.buscaDuplicado(nums3)
print("\nExample 3: \n")
print("Input: ", nums3, "\nOutput: ", output3)

nums4 = [1,1,2]
output4 = objeto.buscaDuplicado(nums4)
print("\nExample 4: \n")
print("Input: ", nums4, "\nOutput: ", output4)

#Otro ejemplo
nums5 = [2,1,4,4,3]
output5 = objeto.buscaDuplicado(nums5)
print("\nExample 5: \n")
print("Input: ", nums5, "\nOutput: ", output5)