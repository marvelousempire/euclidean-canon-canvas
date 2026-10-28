def bjorklund(pulses, steps):
    """Björklund's algorithm for Euclidean rhythms.
    Returns a list of 1s and 0s.
    """
    if pulses > steps or pulses < 0:
        raise ValueError("Invalid pulses")
    if pulses == 0:
        return [0] * steps
    if pulses == steps:
        return [1] * steps

    front = [[1] for _ in range(pulses)]
    back = [[0] for _ in range(steps - pulses)]

    while len(back) > 1:
        new_front = []
        while front and back:
            new_front.append(front.pop(0) + back.pop(0))
        back = front + back
        front = new_front

    return [item for group in front + back for item in group]


if __name__ == "__main__":
    print("E(3,8):", bjorklund(3, 8))
    print("E(5,8):", bjorklund(5, 8))
    print("E(5,13):", bjorklund(5, 13))
