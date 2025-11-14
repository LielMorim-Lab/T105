text = "the price of the chair is 28 ILS"

#replace ils to $
text.replace('ILS','$')


text_price_update = "the price of the table is 28$"
#add 2$ to the price
index = text_price_update.index('28$')
new_price = text.replace('index','index+2')


nums = [2,5,6]
#print for each number the value of the number *2
for num in nums:
    total = num * 2
    print(total)


print ("how to work with loop")
for i in range (1,11):
    print (i)
    print ("hi good morning")
# you can write the loop like this as well
#for i in range (11):
    #print (i)
    #print ("hi good morning")


print(" ")