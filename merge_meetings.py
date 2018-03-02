# # Write a function merge_ranges() that takes a list of
# # multiple meeting time ranges and returns a list of
# # condensed ranges.


# def merge_two(range1, range2):
#   merged = (range1[0], range2[1])
#   return merged


# def merge_ranges(meeting_time_ranges):
#   condensed_ranges = []
#   for index, outer_meeting_time_range in enumerate(meeting_time_range):
#     for inner_meeting_time_range in meeting_time_ranges[index + 1:]:
#       if outer_meeting_time_range[1] >= inner_meeting_time_range[0]:
#         condensed_ranges.append(merge_two(inner_meeting_time_range, outer_meeting_time_range))
#   return condensed_ranges




def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)
    
    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        
        # If the current meeting overlaps with the last merged meeting, use
        # the later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
            
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))
            
    return merged_meetings

google_meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print merge_ranges(google_meetings)