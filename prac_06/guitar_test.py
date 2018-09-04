""" Guitar testing proogram"""

from prac_06.guitar_class import Guitars

gibson = Guitars("Gibson L-5 CES", 1922, 16035.40)
print(gibson.get_age())
print(gibson.is_vintage())

