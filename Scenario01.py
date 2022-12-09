#Create List and Dictionary in advance.
Destination = [] 
Dictionary = {}

#Prompt the number of the destinations u desired.
NumberOfDestination = int(input('How many places the cargo needs to be delivered to: '))

#Prompt the name of destinations based on the number of them.
for i in range(0, NumberOfDestination):
    NameOfDestination = str(input('Please enter the name of the destination: '))
    #Append prompted names to the list of Destinations.
    Destination.append(NameOfDestination)

#Create key:value lists from the dictionary    
for a in Destination:
    Dictionary[str(a)] = []

#Prompt the desired amount of goods     
Goods_amount = int(input('Please enter the amount of goods: '))

#Prompt the names and destinations based on the number of goods
for i in range(0, Goods_amount):
    DestinationOfGoods = str(input('Please enter the destination of the cargo: '))
    NameOfGoods = str(input('Please enter the name of the cargo: '))
    #Append names of the goods to the dictionary if the destination in the dictionary and that of the goods are similar.
    for a in Destination:
        if a == DestinationOfGoods:
            Dictionary[a].append(NameOfGoods)
        
print(Dictionary)

    


        
        
        
        

