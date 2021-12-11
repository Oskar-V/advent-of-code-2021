arr, least_fuel = [], 'start'
with open('input.txt') as f:
    for i in f:
        arr = [int(e) for e in i.strip().split(',')]


def calculateFuelCost(array, to):
    fuel_cost = 0
    for i in array:
        fuel_cost += sum(e for e in range(abs(i-to)+1))
    return fuel_cost


for i in arr:
    print(f"Calculating for {i}")
    fuel_to_this_pos = calculateFuelCost(arr, i)
    if least_fuel == 'start' or fuel_to_this_pos < int(least_fuel):
        least_fuel = fuel_to_this_pos

print(least_fuel)
