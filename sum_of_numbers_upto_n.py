


def sum_of_numbers_upto_n(num):
    output = 0
    for i in range(1, num+1):
        output += i

    return output


if __name__ == "__main__":
    print("hi")
    for i in range(1, 11):
        print(f"sum of numbers up to {i} = {sum_of_numbers_upto_n(i)}")


print("HelloWorld")
