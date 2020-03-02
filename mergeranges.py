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

# need to organize meetings in ascending order based on start time

# return result

# test cases:
# merge_ranges([(1, 3), (2, 4)])


def merge_ranges(meetings):
    """Merging overlapping timeframes!"""

    time_ranges = []
    # sort meetings in ascending order based on first ele
    # if first ele same = sort based on second ele
    meetings.sort()

    # range of first meeting. account for end bc end is exclusive!
    curr_range = range(meetings[0][0], meetings[0][1] + 1)

    for meeting in meetings:
        start = meeting[0]
        end = meeting[1]

        if start in curr_range and end not in curr_range:
            curr_range = range(curr_range[0], end + 1)
        elif start not in curr_range:
            time_ranges.append((curr_range[0], curr_range[-1]))
            curr_range = range(start, end + 1)

    # need to append the very last range into time ranges!
    time_ranges.append((curr_range[0], curr_range[-1]))

    return time_ranges

        	