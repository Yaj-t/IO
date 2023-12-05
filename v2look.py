import matplotlib.pyplot as plt

def look_scheduling(requests, head, direction='left'):
    if not requests:
        return []

    requests.sort()
    path = [head]
    index = 0

    # Find the first request in the direction of head movement
    for i in range(len(requests)):
        if requests[i] >= head:
            index = i
            break

    # Service requests in the initial direction
    if direction == 'left':
        for i in range(index-1, -1, -1):
            path.append(requests[i])
        for i in range(index, len(requests)):
            path.append(requests[i])
    else:
        for i in range(index, len(requests)):
            path.append(requests[i])
        for i in range(index-1, -1, -1):
            path.append(requests[i])

    return path



# Example usage
requests = [176, 79, 34, 60, 92, 11, 41, 114]
initial_head_position = 176
direction = 'right'

servicing_order = look_scheduling(requests, initial_head_position, direction)
print("Order in which requests are serviced:", servicing_order)
