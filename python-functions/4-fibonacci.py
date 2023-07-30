def fibonacci_sequence(n):
    sequence = []
    
    if n <= 0:
        return sequence
    
    sequence.append(0)
    
    if n == 1:
        return sequence
    
    sequence.append(1)
    
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence