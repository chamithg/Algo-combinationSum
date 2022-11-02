class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output =[]
        def run(i, temp, total):
            if(target == total):
                print(temp)
                output.append(temp.copy())
                temp=[]
                return
            if i >= len(candidates) or total > target:
                return
            
            temp.append(candidates[i])
            run(i,temp,total+ candidates[i])
            temp.pop()
            run(i+1,temp,total)
    
        
        run(0,[],0)
        print(output)
        return output
        
candidates = [2,3,5]
target = 8

obj = Solution()

obj.combinationSum(candidates,target)