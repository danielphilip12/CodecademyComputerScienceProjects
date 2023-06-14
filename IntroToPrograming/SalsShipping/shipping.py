weight = 41.5

# Ground Shipping
if weight <= 2:
    cost = (weight * 1.50) + 20
elif weight > 2 and weight <= 6:
    cost = (weight * 3) + 20
elif weight > 6 and weight <= 10:
    cost = (weight * 4) + 20
else:
    cost = (weight * 4.75) + 20

print("Ground shiping cost is $" + str(cost))

ground_shipping_premium_cost = 125
print("The ground shipping premium cost is: $" + str(ground_shipping_premium_cost))


#Drone Shipping
if weight <= 2:
    cost = 4.5 * weight
elif weight > 2 and weight <= 6:
    cost = weight * 9
elif weight > 6 and weight <= 10:
    cost = weight * 12
else:
    cost = weight * 14.25

print("Cost of drone shipping: $" + str(cost))
