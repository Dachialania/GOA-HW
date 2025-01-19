# def manual_replace(string, old, new):
#     result = "" 
#     for char in string:
#         if char == old:
#             result += new  
#         else:
#             result += char  
#     return result


# input_string = "hello world"
# output_string = manual_replace(input_string, " ", "-")
# print(output_string)  





# def manual_range(*args):
    
    
#     if len(args) == 1:
#         start = 0  
#         end = args[0]
#         step = 1  
#     elif len(args) == 2:
#         start = args[0]
#         end = args[1]
#         step = 1  
#     elif len(args) == 3:
#         start = args[0]
#         end = args[1]
#         step = args[2]
#     else:
#         raise TypeError("manual_range requires 1 to 3 arguments")

#     result = []  
#     while start < end:
#         result.append(start)
#         start += step 
#     return result


# print(manual_range(5))     
# print(manual_range(2, 8))     
# print(manual_range(1, 10, 2)) 





