import random
def main():
    sorted_numbers = get_sorted_array()
    item = int(input("Number we are trying to find: "))
    print("Found in position: ", binary_search(item, sorted_numbers))

def binary_search(item, array):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = int((low + high) / 2)
        guess = array[mid]
        print("Guess: ", guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None


def get_sorted_array():
    low = int(input("Lowest value = "))
    high = int(input("Highest value = "))
    maximum_items = int(input("Number of items in the list = "))
    numbers = []

    for index in range(maximum_items):
        numbers.append(random.randint(low, high))
    numbers.sort()
    print(numbers)
    return numbers
    
if __name__ == "__main__":
    main()