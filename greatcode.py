first_name="Imali"
last_name="Okola"
age=20
country="kenya"
school="AkiraChix"
language="python"
full_name=first_name+ last_name
print(f"my name is {full_name} from {country}I am {age} years old \n I am a student at {school} and I love {language} ")#string formating using f statement
y=[15,25,35,45,55]
x=[a*5 for a in y]
print(x)
m=[10,20,30,40,40,20]
p=[x%3 for x in m]
print(p)
v=[x*3 for x in m]
print(v)#list compression
fruits=["mango","banana","pineapple","water_melon","apples"]
fruits.extend(["cucumber","tomatoes"])#appending
fruits.sort()#sorts fruits in ascending order
print(fruits)
for fruit in fruits:#for loop
    print(fruit)
    print(fruit.upper())
    print(fruit.capitalize())

    a=(10,25,30,24,35,76)#tuple
    b=(4,3,5,6,7)
    c=a+b#concatinaton
    print(c)
    l=len(a)
    print(l)#checks length

    print("welcome to my page!")
    name=(input("what is your name?: "))
    age=int(input("what is your age?: "))
    if(age>=18):
        print("you are old enough to play")
        break
    else:
        print("game over!")
        break
















