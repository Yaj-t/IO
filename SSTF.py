import matplotlib.pyplot as plt
import random

def SSTF(requests, head):
    """
    Function to perform SSTF on Disk

    Parameters:
    requests (list): Array of disk locations to service
    head (int): Starting position of disk head

    Returns:
    list: Order of serviced requests
    """
    seek_sequence = []
    while requests:
        # Calculate distance from head to each request
        distance = {abs(head - r): r for r in requests}
        
        # Find the closest request
        closest_request = distance[min(distance)]
        
        # Add the closest request to the seek sequence and remove it from the requests list
        seek_sequence.append(closest_request)
        requests.remove(closest_request)
        
        # Move the head to the closest request
        head = closest_request

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
    plt.suptitle("SSTF Algorithm Seek Sequence")
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

print(f"array: {arr} head: {head}")

sequence = SSTF(arr, head)
print("The sequence of movements is:", sequence)

totalSeekTime =TotalSeekTime(sequence)
print(totalSeekTime)

Plot(sequence, totalSeekTime)