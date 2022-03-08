people = [
    {"name": "Harry", "house": "Gryfndor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Dracp", "house": "Slytherin"}
]

#sort people
#def f(person):
 #return person["house"]
 #people.sort(key=f)
#another shorter approach 

people.sort#(key = lambda person: person ["name"])


print(people)