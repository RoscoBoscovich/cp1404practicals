

number_list = []
for i in range(5):
    number_list = number_list + [int(input("Number:"))]
print("The first number is {}".format(number_list[0]))
print("The last number is {}".format(number_list[4]))
print("The smaller number is {}".format(min(number_list)))
print("The largest number is {}".format(max(number_list)))
print("The average of the numbers is {}".format((1/5)*sum(number_list)))
