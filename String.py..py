string1="Hello "
name=input("Enter your name:")
string2=string1+name
print(string2)
string3=" , welcome to Python programming"
string4=string2+string3
print(string4)
#String slicing and indexing#
print(string4[0])
print(string4[-1])
print(string4[:5])
print(string4[-11:])
print(string4[::-1])
print(string4[22:28])
#String Methods#
strM="Python beginner tutorial"
print(strM.upper())
print(strM.lower())
print(strM.capitalize())
print(strM.count("t"))
print(strM.replace("Python","Machine Learning"))
#Tuples
tuple1=(10,20,30)
tuple2=(40,50,60)
t_combine=tuple1+tuple2
print("concatenated couple=",t_combine)
print("Repeated elements=",t_combine*3)
print(t_combine[2])
print(t_combine[:3])
print(t_combine[-3:])
