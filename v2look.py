def LOOK(arr, head, direction):
    """
    Function to perform the LOOK algorithm

    :param arr: List of disk locations to access
    :param head: Starting position of the disk head
    :param direction: Direction of head movement ('left' or 'right')
    :return: The order of disk accesses
    """
    size = len(arr)
    distance = 0
    seek_sequence = []

    # Appending end values which has to be visited
    # before reversing the direction
    if direction == "left":
        left = [x for x in arr if x <= head]
        right = [x for x in arr if x > head]
        left.sort()
        right.sort()

        # First service the requests on the left side
        for i in range(len(left) - 1, -1, -1):
            cur_track = left[i]
            seek_sequence.append(cur_track)

        # Then move to the right side
        for i in range(len(right)):
            cur_track = right[i]
            seek_sequence.append(cur_track)

    elif direction == "right":
        left = [x for x in arr if x <= head]
        right = [x for x in arr if x > head]
        left.sort()
        right.sort()

        # First service the requests on the right side
        for i in range(len(right)):
            cur_track = right[i]
            seek_sequence.append(cur_track)

        # Then move to the left side
        for i in range(len(left) - 1, -1, -1):
            cur_track = left[i]
            seek_sequence.append(cur_track)

    return seek_sequence

# Example usage
arr = [176, 79, 34, 60, 92, 11, 41, 114]
head = 176
direction = "left"

sequence = LOOK(arr, head, direction)
print("The sequence of movements is:", sequence)