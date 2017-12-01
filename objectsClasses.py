class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greet = []

    def greet(self,other_person):
        print('Hello %s, I am %s' %(other_person.name, self.name))
        self.greeting_count += 1

        if len(self.unique_greet) == 0:
            self.unique_greet.append(other_person.name)

        print("the greeting count is %d"%(self.greeting_count))
        for name in self.unique_greet:
            if name != other_person.name:
                self.unique_greet.append(other_person.name)

    def print_contact_info(self):
        print("Sonny's email: %s, Sonny's phone number: %s" %(self.email, self.phone))

    def num_friends(self):
        print(len(self.friends))

    def __repr__(self):
        return  (self.name + self.email + self.phone)

    def number_unique_people_greeted(self):
        print(len(self.unique_greet))



sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')
marry = Person('Marry','jordan@aol.com','495-586-3456')
sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)
sonny.print_contact_info()
jordan.friends.append(sonny)
sonny.friends.append(jordan)
jordan.num_friends()
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(marry)
sonny.number_unique_people_greeted()
print(jordan)


class Vehicle(object):
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(str(car.year) +" " + car.make + " " + car.model)

car = Vehicle('Nissan', 'Leaf', 2015)
print (car.make, car.model, car.year)
car.print_info()
