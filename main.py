driver_name = input("Enter driver name: ")
distance = float(input("Enter your distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

litres_needed = (distance * consumption) / 100
fuel_cost = litres_needed * fuel_price
cost_per_km = fuel_cost / distance

print("=" * 30)
print("         ROAD TRIP SUMMARY")
print("=" * 30)
print("Driver: ",driver_name)
print("Distance: ",distance,"km")
print("Consumption: ",consumption,"L/km")
print("Fuel price: ",fuel_price,"L/km")

print ("-" * 30)
print("Litres: ",litres_needed,"L")
print("Cost: ",fuel_cost,"KZT")
print ("Cost per km: ",cost_per_km,"KZT")
print("=" * 30)

print("Trip longer than 300 km: ",distance> 300)
print ("Fuel cost above 5000 KZT: " , fuel_cost > 5000)
