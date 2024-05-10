def mean(data):
    if not data:
        return 0
    return sum(data) / len(data)

def mode(data):
    if not data:
        return 0
    d = {}
    for i in data:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for w in sorted(d, key=d.get, reverse=True):
        return w

def median(data):
    if not data:
        return 0
    data.sort()
    index = len(data) // 2
    if len(data) % 2 == 0:
        return data[index]
    else:
        return (data[index - 1] + data[index]) / 2

def main():
    data_str = input("Enter a list of numbers separated by spaces: ")
    data = [int(x) for x in data_str.split()]
    
    print("The list is:")
    print(data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))

if __name__ == "__main__":
    main()
