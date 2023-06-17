# Global Variables

destinations = ["Paris, France", "Shanghai, China", "Los Angelos, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_tourist = ["Erin Wilkes", "Shanghai, China", ['historical site', 'art']]


# Functions
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index



# Function Tests
# print(get_destination_index("Los Angelos, USA"))
# print(get_destination_index("Paris, France"))
# print(get_destination_index("Hyderabad, India"))

test_destination_index = get_traveler_location(test_tourist)
print(test_destination_index)