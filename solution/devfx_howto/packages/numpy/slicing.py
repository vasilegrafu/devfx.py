import numpy as np

print("----------------------------------------------------------------")
print("Creating array")
print("----------------------------------------------------------------")

x = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
print("x ->", x)
print("x.shape ->", x.shape)


print("----------------------------------------------------------------")
print("Array indexing and slicing")
print("----------------------------------------------------------------")

"""
Index from front:       0   1   2   3   4   5
Index from rear:       -6  -5  -4  -3  -2  -1
                        +---+---+---+---+---+---+
                        | P | y | t | h | o | n |
                        +---+---+---+---+---+---+
Slice from front:   n:  0   1   2   3   4   5   6  :n
Slice from rear:    n: -6  -5  -4  -3  -2  -1      :n

Index:
      0   1   2   3   4
    +---+---+---+---+---+
    | a | b | c | d | e |
    +---+---+---+---+---+
     -5  -4  -3  -2  -1

Slice:
       <----------------|
    |---------------->
    :                   :
    0   1   2   3   4   5
    +---+---+---+---+---+
    | a | b | c | d | e |
    +---+---+---+---+---+
   -5  -4  -3  -2  -1
    :                   :
    |---------------->
       <----------------|
"""

""" [a:b:c]
    len = length of string, tuple or list
    c -> Default is +1 (forward with step size +1).
         Sign of c indicates forward or backward.
         Absolute value of c indicates steps.
         Positive means forward, negative means backward.
    a => When c is positive or blank, default is 0.
         When c is negative, default is -1.
    b => When c is positive or blank, default is +len.
         When c is negative, default is -(len+1).
"""

""" seq[:]                # [seq[0],   seq[1],          ..., seq[-1]    ]
    seq[low:]             # [seq[low], seq[low+1],      ..., seq[-1]    ]
    seq[:high]            # [seq[0],   seq[1],          ..., seq[high-1]]
    seq[low:high]         # [seq[low], seq[low+1],      ..., seq[high-1]]
    seq[::stride]         # [seq[0],   seq[stride],     ..., seq[-1]    ]
    seq[low::stride]      # [seq[low], seq[low+stride], ..., seq[-1]    ]
    seq[:high:stride]     # [seq[0],   seq[stride],     ..., seq[high-1]]
    seq[low:high:stride]  # [seq[low], seq[low+stride], ..., seq[high-1]]
"""

""" a[start:end] # items start through end-1
    a[start:]    # items start through the rest of the array
    a[:end]      # items from the beginning through end-1
    a[:]         # a copy of the whole array
    a[start:end:step] # start through not past end, by step

    a[-1]    # last item in the array
    a[-1:]   # last item in the array
    a[-2]    # last second item in the array
    a[-2:]   # last two items in the array
    a[:-1]   # everything except the last item
    a[:-2]   # everything except the last two items
"""

x = np.arange(0, 7 + 1)
print("x[0:5] ->", x[0:5])
print("x[0:x.size] ->", x[0:x.size])
print("x[:x.size] ->", x[:x.size])
print("x[0:] ->", x[0:])
print("x[7::-1] ->", x[7::-1])
print("x[:7+1:+1] ->", x[:7 + 1:+1])

print("x[-1] ->", x[-1])
print("x[-1:] ->", x[-1:])
print("x[:-1] ->", x[:-1])

print("x[-2] ->", x[-2])
print("x[-2:] ->", x[-2:])
print("x[:-2] ->", x[:-2])

print("x[::+1] ->", x[::+1])
print("x[::-1] ->", x[::-1])

print("----------------------------------------------------------------")

x = np.arange(1, 64 + 1)
print(x)
print(x.shape)

print(x[-4:])

print("----------------------------------------------------------------")

x = np.array(np.split(x, 8))
print(x)
print(x.shape)

print(x[0, :])
print(x[:, 0])

print("----------------------------------------------------------------")

x = [1]
print(x[-1:])

