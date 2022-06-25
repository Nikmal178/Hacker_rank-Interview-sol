# length of the array
n = int(input())

# input array elements
arr = list(map(int, input().strip().split()))
    

# plusMinus function with argument as an array
def plusMinus(array):
    p_arr = []
    n_arr = []
    z_arr = []

    for ele in array:
        if ele > 0:
            p_arr.append(ele)
        elif ele < 0:
            n_arr.append(ele)
        elif ele == 0:
            z_arr.append(ele)

    p_len = len(p_arr)
    n_len = len(n_arr)
    z_len = len(z_arr)

    p_ratio = float(p_len/n)
    n_ratio = float(n_len/n)
    z_ratio = float(z_len/n)

    print("{:.6f}".format(p_ratio))
    print("{:.6f}".format(n_ratio))
    print("{:.6f}".format(z_ratio))


# calling plusMinus() 
plusMinus(arr)
