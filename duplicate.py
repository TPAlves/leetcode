input = [1, 2, 3, 1]
result = False
# for i in range(len(input)):
#     for j in range(i + 1, len(input)):
#         if input[i] == input[j]:
#             result = True
#             break

# print(result)  


for n, i in enumerate(input):
    if i in input[n + 1:]:
        result = True
        break
    
print(result)