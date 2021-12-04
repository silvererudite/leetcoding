# def reverseString(word):
#     i = 0
#     j = len(word)-1
#     word = list(word)
#     while(i<j):
#         swap(word,i,j)
#         i +=1
#         j -=1
#     return str(word)
# nums = [16,1,0,9,100]
# def swap(word, i, j):
#     temp = word[i]
#     word[i]=word[j]
#     word[j]=temp

def sortArray(nums):
    nums_new = [0]*len(nums)
    i = 0 
    j = len(nums)-1
    counter = len(nums)-1
    while i <=j:
        leftSq = nums[i]**2
        rightSq = nums[j]**2
        if leftSq > rightSq:
            nums_new[counter] = leftSq
            i +=1
        else:
            nums_new[counter] = rightSq
            j -=1
        counter -=1
    return nums_new

