class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(person['name'], person['age']))
    for p in people:
        obj = Person.people[p['name']]
        if p["wife"] in Person.people:
            obj.wife = Person.people[p["wife"]]
        if p["husband"] in Person.people:
            obj.husband = Person.people[p["husband"]]
    return result