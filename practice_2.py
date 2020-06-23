my_list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
output: [27, 82, 9, 27, 99, 63, 42]


# divisible by 3 with no remainder
# loop through array -> 
# use module % to find numbers with no remainder
# if module = 0 then put into results array

# class Practice(object):
#     def divisibleByThree(self, nums):

#         results = []

#         for num in my_list:
#             if num % 3 == 0:
#                 results.append(num)
#                 return(results)                
#         print(list(results))

# result = list(filter(lambda x: (x % 3 == 0), my_list))

# # display the result
# print("Numbers divisible by 3 are", result)


results = []

for num in my_list:
    if num % 3 == 0:
        results.append(num)           
print(list(results))
