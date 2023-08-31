print('                 MIS 303: Business Application Programming')

print()
print('Assignment 1')
name = input('Name: ')

print()
print("This app serves as a checkout system fot the Anaconda's Pit Motel.")
print()
customer = input("Customer's Name: ")
room = input("Enter Room Number: ")
rental_nights = int(input("Number of Nights Staying: "))
cost_per_room=23.59
total_cost = (cost_per_room * rental_nights)

print()
print("Customers Name: " + customer)
print("Room Number: " + room)
print("Number of nights: " + str(rental_nights))
print("Room Cost: " + str(cost_per_room))
print("Total Cost: " + str(total_cost))


