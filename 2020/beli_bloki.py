# Emina Merlak Susman
# 27151132
# Praktična matematika


# Returns index of x in arr if present, else -1
def binary_search(li, low, high, x):
    '''Binary search'''


    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if li[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif li[mid] > x:
            return binary_search(li, low, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binary_search(li, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# reading input

w, h, k = map(int, input().split())

black_dots = []
for _ in range(k):
    coords = tuple(map(int, input().split()))
    black_dots.append(coords)

# add black edges
for j in range(w + 2):
    black_dots.append((j, 0)) # top

for i in range(1, h + 2):
    black_dots.append((0, i)) # left

for l in range(1, w + 2):
    black_dots.append((l, h + 1)) # bottom

for d in range(1, h + 1):
    black_dots.append((w + 1, d)) # right


x_coords = sorted(black_dots, key=lambda k: [k[0], k[1]])
y_coords = sorted(black_dots, key=lambda k: [k[1], k[0]])

block_count = 0

# checking differences
for i in range(len(x_coords) - 1):
    first = x_coords[i]
    second = x_coords[i + 1]

    if first[0] == second[0]:
        diff = second[1] - first[1]
        if diff > 2:
            block_count += 1

        elif diff == 2:  # a block of length one only counts if it's surrounded by black dots on all four sides
            this_field = (second[0], second[1]- 1)  # coordinates of this white block
            # we need to find out whether the fields
            # left and right of this white block are black
            left_field = (this_field[0] - 1, this_field[1])
            right_field = (this_field[0] + 1, this_field[1])

            # finding left and right in x_coords with binary search
            # (faster than finding it in black_dots list, bc x_coords is sorted)
            low = 0
            high = len(black_dots)


            lft_check = binary_search(x_coords, low, high, left_field)
            rgt_check = binary_search(x_coords, low, high, right_field)

            if -1 not in [lft_check, rgt_check]:
                block_count += 1  # we only have to count these square blocks once


for i in range(len(y_coords) - 1):
    first = y_coords[i]
    second = y_coords[i + 1]
    if first[1] == second[1]:
        diff = second[0] - first[0]
        if diff > 2:
            block_count += 1


print(block_count)


