s="Tops Technologies"

print(s)

print(s.capitalize())

print(s.casefold())

print(s.lower())
print(s.upper())

print(s.center(40,"*"))

print(s.find("log"))

print(s.index("T",2))

print(s.swapcase())

print(s.count("o"))

print(s.endswith("ese"))
print(s.startswith("To"))

print("python programing".title())

print("tops123".isalnum())
print("tops".isalnum())
print("123".isalnum())
print("tops 123".isalnum())

print("tops".isalpha())

print("122".isnumeric())

print(s.istitle())

print(" ".isspace())

for i in s:
    print(i,end=" ")
