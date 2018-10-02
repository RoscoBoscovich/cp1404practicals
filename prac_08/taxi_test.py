"""Write lines of code for each of the following (hint: use the methods available in the Taxi class):

Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km

Drive the taxi 40km

Print the taxi's details and the current fare

Restart the meter (start a new fare) and then drive the car 100km

Print the details and the current fare"""

from prac_08.taxi import Taxi

prius1 = Taxi("Prius 1", 100)

prius1.drive(40)

print(prius1)
print(prius1.get_fare())

prius1.start_fare()

prius1.drive(100)

print(prius1)
print(prius1.get_fare())
