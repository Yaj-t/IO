import matplotlib.pyplot as plt

def LOOK(arr, head, direction):
    size = len(arr)
    distance = 0
    seek_sequence = []

    # Append end values which may not have been included
    if direction == 'left':
        left = [0]
        right = []
    elif direction == 'right':
        left = []
        right = [199]  # assuming disk size of 200

    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    left.sort()
    right.sort()

    run = 2
    while run:
        if direction == 'left':
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]

                # Appending current track to seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance += abs(cur_track - head)

                # Update current head
                head = cur_track

            # Reversing the direction
            direction = 'right'
                
        elif direction == 'right':
            for i in range(len(right)):
                cur_track = right[i]

                # Appending current track to seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance += abs(cur_track - head)

                # Update current head
                head = cur_track

            # Reversing the direction
            direction = 'left'
                
        run -= 1

    return distance, seek_sequence

# Example Usage
arr = [176, 79, 34, 60, 92, 11, 41, 114]
head = 200
direction = 'left'

distance, seek_sequence = LOOK(arr, head, direction)

print("Total number of seek operations =", distance)
print("Seek Sequence is", seek_sequence)

# Plotting the Graph with numbers on points
plt.figure(figsize=(10, 5))
plt.plot(seek_sequence, marker='o')
plt.title("Disk Arm Movement - LOOK Algorithm")
plt.xlabel("Seek Sequence")
plt.ylabel("Disk Track Number")
plt.ylim(0, 200)  # Set the y-axis limit to 0-200
plt.grid(linestyle='--')

# Adding numbers to each point
for i, track_number in enumerate(seek_sequence):
    plt.text(i, track_number, str(track_number), ha='right', va='bottom')

plt.show()
