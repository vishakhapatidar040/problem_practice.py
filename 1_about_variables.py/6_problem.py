#temperature analyzer
#7 days ke temperatures input lena hai
temperatures = []
for i in range(7):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    temperatures.append(temp) 

#calculations
total= sum(temperatures)
average = total / len(temperatures)
highest = max(temperatures)
lowest = min(temperatures)

#results
print("\nTemperature Analysis")
print("Average Temperature:", average)
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)        
