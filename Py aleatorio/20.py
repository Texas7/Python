N = int(input())

hrs = ((N / 60)/60)
min = ((N / 60)% 60)

mn = (N / 60)
seg = (N % 60)

print("{}:{}:{}".format(int(hrs),int(min),int(seg)))
