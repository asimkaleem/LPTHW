def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d count of cracker boxes" % boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket. \n"


print "we can just give the function numbers directly:"
cheese_and_crackers(30, 45)

print "OR we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 35

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print "We can even do Math Inside:"
cheese_and_crackers(10+5, 15+5)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



print