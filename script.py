def ground_shipping(weight):
 
 if(weight <= 2):
   cost = 1.50
  
 elif(weight <= 6):
   cost = 3.00
   
 elif(weight <= 10):
   cost = 4.00
   
 else:
   cost = 4.75
 return 20 + (cost * weight)

#print(ground_shipping(8.4))

premium_shipping = 125.00

def drone_shipping(weight):
  if(weight <= 2):
    cost = 4.50
  elif(weight <= 6):
    cost = 9.00
  elif(weight <= 10):
    cost = 12.00
  else:
    cost = 14.25
  return (cost * weight)
#print(drone_shipping(1.5))

def cheap_shipping(weight):

  ground = ground_shipping(weight)
  premium = premium_shipping
  drone = drone_shipping(weight)

  if ground < premium and ground < drone: 
    method = "Standard Ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "Premium Ground"
    cost = premium
  else:
    method = "Drone"
    cost = drone
  print("The cheapest option available is $%.2f with %s shipping."
    % (cost, method)
    )

print(cheap_shipping(4.8))
print(cheap_shipping(41.5))
