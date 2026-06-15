"""
Merge Sort implementation.

Improvement 1:
Added module documentation.
"""


def merge_sort(values):
    """
    Improvement 2:
    Added function documentation.
    Sorts a list using Merge Sort.
    """

    # Improvement 3:
    # Simplified the termination condition.
    if len(values) <= 1:
        return

    # Improvement 4:
    # Replaced unclear variable names.
    middle = len(values) // 2
    left_half = values[:middle]
    right_half = values[middle:]

    merge_sort(left_half)
    merge_sort(right_half)

    # Improvement 5:
    # More descriptive index names.
    left_index = 0
    right_index = 0
    merged_index = 0

    while left_index < len(left_half) and right_index < len(right_half):

        # Improvement 6:
        # Removed unnecessary ASSIGNMENT() wrapper function
        # and used direct assignment.
        if left_half[left_index] <= right_half[right_index]:
            values[merged_index] = left_half[left_index]
            left_index += 1
        else:
            values[merged_index] = right_half[right_index]
            right_index += 1

        merged_index += 1

    while left_index < len(left_half):
        values[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right_half):
        values[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1


# Improvement 7:
# Added main guard to separate reusable code
# from executable code.
if __name__ == "__main__":

    import matplotlib.pyplot as plt

    # Improvement 8:
    # More descriptive variable name.
    numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    x_values = range(len(numbers))
    plt.plot(x_values, numbers)

    # Improvement 9:
    # Added plot title.
    plt.title("Before Merge Sort")
    plt.show()

    merge_sort(numbers)

    x_values = range(len(numbers))
    plt.plot(x_values, numbers)

    plt.title("After Merge Sort")
    plt.show()
