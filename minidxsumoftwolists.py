"""leetcode challenge: 599. Minimum Index Sum of Two Lists

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).


Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.

"""

# thoughts
# input: two lists
# output: list w/item found in both lists and least list idx sum - ex: (0 + 1)

# empty list var
# sum idx var = None

# i = idx list 1
# k = idx list 2
# while loop -> idx can loop through both
# if item in list 1 == item in list 2
# add i and k 
# if sum == None or sum == i + k 
# sum = i + k 
# append item
# else if i + k < sum, 
# reset list - list = []
# append current item 

# outside of loop
# return list

def findRestaurant(self, list1, list2):
	"""
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    same_fave = []
    sum_idx = None
    
    # idx of list1       
    i = 0
    
    while i < len(list1):
        if list1[i] in list2:
            #TODO: get idx of item in list[2]
            # idx of item in list2
            k = list2.index(list1[i])
            a_sum = i + k
            if sum_idx == None or sum_idx == a_sum:
                sum_idx = a_sum
                same_fave.append(list1[i])
            elif a_sum < sum_idx:
                sum_idx = a_sum
                same_fave = []
                same_fave.append(list1[i])
        i+=1
    return same_fave
