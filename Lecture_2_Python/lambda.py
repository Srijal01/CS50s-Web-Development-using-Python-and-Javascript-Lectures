people = [
    {"name":"Ram", "house": "Thecho"},
    {"name": "Shyam", "house": "Chapagaun"},
    {"name": "Kumar", "house": "Jawalakhel"}
]

def f(person):                         #or
    return person["name"]

people.sort(key=f)                      #people.sort(key= lambda person: person["name"])

print(people)