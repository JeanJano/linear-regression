def main():
    print("hello linear regression")

    theta0 = 0.0
    theta1 = 0.0
    data = ""
    learningRate = 0.01
    m = -1
    mileages = []
    prices = []

    with open("data.csv", "r") as f:
        data = f.read()
        
    data_split = data.split("\n")
    for elem in data_split:
        if elem == "km,price":
            continue
        elem_split = elem.split(",")
        if (len(elem_split) > 1):
            mileages.append(int(elem_split[0]))
            prices.append(int(elem_split[1]))

    m = len(mileages)

    print(mileages)
    print(prices)
    print(m)
    # print(data_split)
    # print(data)

if __name__ == "__main__":
    main()