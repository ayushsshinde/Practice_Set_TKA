cars = ["bmw", "mahindra", "suzuki", "rolls royce", "bentley", "aston martin", "tata", "audi", "mustang"]

#Q1)Append
cars.append("ferrai")
print(cars)

#Q2)Insert
cars.insert(3, "porsche")
print(cars)

#Q3)Clear
#cars.clear()
#print(cars)

#Q4)Sort
cars.sort()
print(cars)

#Q5)Remove
cars.remove("audi")
print(cars)

#Q6)Index
index_number=cars.index("mustang")
print(index_number)

#Q7)Extend
cars.extend(["tesla", "nissan"])
print(cars)

#Q8)Pop
popped_car = cars.pop()
print("Popped Car:", popped_car)

#Q9)Count
bmw_count = cars.count("bmw")
print("Count of 'bmw':", bmw_count)

#Q10)Append Multiple
cars.extend(["jaguar", "fiat"])
print(cars)

#Q11)Insert Multiple
cars[2:2] = ["volvo", "honda"]
print(cars)

#Q12)Clear If Empty
if cars:
    print("List is not empty:", cars)
else:
    cars.clear()
    print("List was empty and has been cleared.")

#Q13)Sort Descending
sorted_cars_desc = sorted(cars, reverse=True)
print("Cars Descending:", sorted_cars_desc)

#Q14)Remove All Occurrences
cars = [car for car in cars if car != "bmw"]
print("After Removing All Occurrences of 'bmw':", cars)

#Q15)Find Last Index
last_index_tata = len(cars) - 1 - cars[::-1].index("tata")
print("Last Index of 'tata':", last_index_tata)

#Q16)Extend with Condition
if "bmw" in cars:
    cars.extend(["ferrari", "lambo"])
print("After Extend with :", cars)


