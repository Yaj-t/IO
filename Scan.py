import matplotlib.pyplot as plt
import random

def SCAN(arr, head, direction):
    """
    Function to perform SCAN on Disk

    Parameters:
    arr (list): Array of disk locations to service
    head (int): Starting position of disk head
    direction (str): Direction to move ('left' or 'right')

    Returns:
    list: Order of serviced requests
    """
    
    distance = 0
    seek_sequence = []

    # Appending end values which has to be visited before reversing the direction
    if direction == 'left':
        arr.append(0)
    elif direction == 'right':
        arr.append(200)
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

# Example usage
# arr = [random.randint(0, 199) for _ in range(20)]
arr = [176, 79, 34, 60, 92, 11, 41, 114]
head = arr[0]
direction = "right"

print(f"array: {arr} head: {head} direction: {direction}")
sequence = SCAN(arr, head, direction)
print("The sequence of movements is:", sequence)

# Plotting the seek sequence with labels
plt.figure(figsize=(10, 5))
plt.plot(range(len(sequence)), sequence, marker='o', linestyle='-')
plt.xlabel("Index")
plt.ylabel("Size")
plt.title("LOOK Algorithm Seek Sequence")

# Adding labels to each data point
for i, size in enumerate(sequence):
    plt.annotate(f"{size}", (i, size), textcoords="offset points", xytext=(0, 10), ha='center')

plt.grid(True)
plt.show()