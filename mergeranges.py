# thoughts
# input: list of tuples
# output: list of tuples

# want to merge tuples that have overlapping ranges
# want to list through whole list bc meeting times could be out of order!

# make a results list
# loop through.. the list
# if the next tuple(start) is within the range (start, end) and end is exclusive! 
# change the range to include current tuple's end 
# else append the new range tuple into the result list

# return result

# test cases:
# merge_ranges([(1, 3), (2, 4)])


def merge_ranges(meetings):
    """Merging overlapping timeframes!"""

    time_ranges = []
    curr_meeting = meetings[0]
    curr_start = curr_meeting[0]
    # account for ranges being exclusive 
    curr_end = curr_meeting[1] + 1
    print('curr_start', curr_start)
    print('curr_end', curr_end)
    
    for meeting in meetings:
        print(meeting)
        start = meeting[0]
        end = meeting[1]
        
        if meeting == curr_meeting:
        	continue
        elif start in range(curr_start, curr_end):
            print('in the if part')
            curr_meeting = (curr_start, end)
            curr_end = end + 1
            time_ranges.append(curr_meeting)
            print('curr_meeting', curr_meeting)
            print('curr_end', curr_end)
        else:
            print('in the else part')
            print(curr_meeting)
            time_ranges.append(curr_meeting)
            curr_meeting = meeting

    return time_ranges

        	