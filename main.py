def clamp(value, low, high):
    if value<=low:
        return low
    if value>=high:
        return high
    else:
        return value
print(clamp(-1, 0, 1))     # 0
print(clamp(0.5, 0, 1))    # 0.5
print(clamp(2, 0, 1))      # 1
print(clamp(10, 20, 100))  # 20
print(clamp(50, 20, 100))  # 50
print(clamp(150, 20, 100)) # 100