def summing_the_n_series():
    tc = input()
    while tc > 0:
        num_t = input()
        tc -= 1
        print int((num_t * (1 + ((num_t**2) - ((num_t-1)**2))))/2) % ((10**9) + 7)

summing_the_n_series()