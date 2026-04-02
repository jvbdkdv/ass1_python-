driver_name = input("Enter driver name: ")
destination = input("Enter destination: ")
distance = float(input("Enter your distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
price = float(input("Enter fuel price (KZT/L): "))

fuel_cost = (distance/100) * consumption

if distance < 100:
    category = "Short trip"
elif distance < 500:
    category = "Medium trip"
else:
    category = "Long trip"

print("=" * 30)
print("Driver: ", driver_name)
print("Destination: ", destination.upper())
print("Distance: ", distance,"km")
print("Fuel cost: ", fuel_cost,"KZT")
print("Category: ", category)
print("=" * 30)

print("\n Cost breakdown: ")

for km in range(100,int(distance) + 1,100):
    fuel_cost = (km / 100) * consumption * price
    print(km,"km ->",fuel_cost,"KZT")

print("\nDestination uppercase: ", destination.upper())
print("Destination lowercase: ", destination.lower())
print("Length :",len(destination))

count_a = destination.lower().count('a')
print("Letter 'a' count :", count_a)


