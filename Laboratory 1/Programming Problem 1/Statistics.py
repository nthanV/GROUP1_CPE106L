"""Laboratory 1"""
def calculatemedian(lst):
    sortedlist = sorted(lst)
    mid = len(sortedlist) // 2
    return (sortedlist[mid] + sorted_list[~mid]) / 2

def calculate_mode(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)

def calculate_mean(lst):
    return sum(lst) / len(lst)

def get_user_input():
    numbers = input("Enter numbers separated by spaces: ").strip().split()
    return [float(num) for num in numbers]

def main():
    num_list = get_user_input()
    print("Results:")
    print(f"Median: {calculate_median(num_list):.3f}")
    print(f"Mode:   {calculate_mode(num_list):.3f}")
    print(f"Mean:   {calculate_mean(num_list):.3f}")

if __name == "__main":
    main()
