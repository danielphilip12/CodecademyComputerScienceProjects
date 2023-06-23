class Student:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year
        self.courses = list()
        self.friends = list()
    
    def __repr__(self):
        return "{name} is a {age} year old student in grade {year}".format(name=self.name, age=self.age, year=self.year)
    
    def add_friend(self, friend):
        if type(friend) is not Student:
            return "This is not a fellow student. Make a real friend"
        
        self.friends.append(friend)
        friend.friends.append(self)

    def get_friends(self):
        print("These are {}'s friends".format(self.name))
        for friend in self.friends:
            print(friend.name)