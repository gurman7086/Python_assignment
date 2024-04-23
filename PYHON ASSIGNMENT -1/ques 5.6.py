import statistics

my_list = [2, 4, 6, 8, 10]


mean = statistics.mean(my_list)
print("Mean:", mean)

variance = statistics.variance(my_list)
print("Variance:", variance)


std_dev = statistics.stdev(my_list)
print("Standard Deviation:", std_dev)
