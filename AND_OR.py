#use of AND and OR keyword

#use of AND keyword
age=25
result= age<20 and age>22    #here 1st condition is false and 2nd is true therefore acc to table final o/p is false.
positive=age<28 and age>24    #here 1st condition is true and 2nd is also true therefore the o/p is also true.

print(result)
print(positive)


#use of OR keyword
default_age=20
user=0

output=user or default_age
print(output)
