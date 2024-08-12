def odd_index_sum(numbers):

    total_sum = 0
 
    for index in range(len(numbers)):
   
        if index % 2 != 0:
           
            total_sum += numbers[index]
    
    return total_sum


print(odd_index_sum([1, 2, 3, 4, 5]))  
print(odd_index_sum([10, 20, 30, 40, 50])) 
print(odd_index_sum([7, 8, 9, 10, 11, 12]))  