def main():
    print("hello linear regression")

    theta0 = 0.0
    theta1 = 0.0
    data = ""

    with open("data.csv", "r") as f:
        data = f.read()
    
    
    print(data)

if __name__ == "__main__":
    main()