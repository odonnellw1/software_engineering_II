#Author: William O'Donnell
#Purpose: Lab 1 exersices
#Date: 14 October 2021

#Project 1 / seconds and minutes in a day
print("Project 1")
hours = 24
minutes = hours*60
seconds = minutes*60
print("The number of minutes in 24 hours is: ", minutes, "minutes")
print("The number of seconds in 24 hours is: ", seconds, "seconds")
print()

#Project 2 / Area and circumfrence given the radius
print("Project 2")
pi = 22/7
area = pi*2**2
print("The area is ", area, "sq.cm")
circumfrence = 2*pi*2
print("The circumfrence is ", circumfrence, "cm")
print()

#Project 3 / Area and new area when area changes
print("Project 3")
pi = 22/7
radius = 2
area = pi*radius**2
print("The area is ", area, "sq.cm")
radius = 5
area = pi*radius**2
print("The new area is ", area, "sq.cm")
print()

#Project4 / Square root of 9
print("Project 4")
print("The square root is:", 9**.5)
print()

#Project5 / Convert given km to miles
print("Project 5")
conversion_factor = 0.6214
print("20 km is equal to ", 20*0.6214, "miles")
print()

#Project6 / Alphabet to months of the year
print("Project 6")
A = "January"
B = "February"
C = "March"
D = "April"
E = "May"
F = "June"
G = "July"
H = "August"
I = "September"
J = "October"
K = "November"
L = "December"
print("The Spring semester consists of: " + A, B, C, D, "and " + E, sep=", ")
print("Summer is between the months of: " + F + " and " + H)
print()

#Project7 / Area of triangle with given side lengths
print("Project 7")
a = 12
b = 15
c = 18
s = (a+b+c)/2
K = (s*(s-a)*(s-b)*(s-c))**.5
print("The area of the given triangle is", K)
print()