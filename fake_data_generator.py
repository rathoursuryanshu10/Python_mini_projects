from faker import Faker

fake = Faker()
print("Name:: "+fake.name())
print ("Address:: "+fake.address())
print("Message:: "+fake.text())
print ("E-Mail:: "+fake.email())
print("Country:: "+fake.country())
print (fake.latitude(), fake.longitude())
print ("URL:: "+fake.url())
