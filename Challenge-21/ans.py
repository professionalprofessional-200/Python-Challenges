def calculate_average():
    numbers=input("Numbers are separated by spaces:")
    number_list=[float(num) for num in numbers.split()]
    
    if len(number_list)==0:
        return 0
        
    total_sum=sum(number_list)
    count=len(number_list)
    
    average=total_sum/count
    
    return average
    
result=calculate_average()

print(f"{result}")
