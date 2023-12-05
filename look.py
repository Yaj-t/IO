import matplotlib.pyplot as plt
import random
def LOOK(arr, head, direction):
    """
    Function to perform the LOOK algorithm

    :param arr: List of disk locations to access
    :param head: Starting position of the disk head
    :param direction: Direction of head movement ('left' or 'right')
    :return: The order of disk accesses
    """
    seek_sequence = []
        
    size = len(arr)
    arr.sort()

    # Find the position to start the servicing
    index = arr.index(head)

    # Move to the end in the specified direction and then reverse
    if direction == 'left':
        for i in range(index, -1, -1):
            seek_sequence.append(arr[i])
        
        for i in range(index + 1, size):
            seek_sequence.append(arr[i])

    elif direction == 'right':
        for i in range(index, size):
            seek_sequence.append(arr[i])
        
        for i in range(index - 1, -1, -1):
            seek_sequence.append(arr[i])

    return seek_sequence

def TotalSeekTime(seek_sequence):
    seek_time = 0

    for i in range(len(seek_sequence)-1):
        seek_time += abs(seek_sequence[i] - seek_sequence[i+1])
    
    return seek_time

def Plot(sequence, totalSeekTime):
    # Plotting the seek sequence with labels
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(sequence)), sequence, marker='o', linestyle='-')
    plt.xlabel("Index")
    plt.ylabel("Size")
    plt.suptitle("LOOK Algorithm Seek Sequence")
    plt.title(f'Total Seek Time: {totalSeekTime}')


    # Adding labels to each data point
    for i, size in enumerate(sequence):
        plt.annotate(f"{size}", (i, size), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.grid(True)
    plt.show()
    
# Example usage
# arr = [random.randint(0, 199) for _ in range(20)]
arr = [176, 79, 34, 60, 92, 11, 41, 114]
head = arr[0]
direction = "right"
print(f"array: {arr} head: {head} direction: {direction}")

sequence = LOOK(arr, head, direction)
print("The sequence of movements is:", sequence)

totalSeekTime =TotalSeekTime(sequence)
print(totalSeekTime)

Plot(sequence, totalSeekTime)