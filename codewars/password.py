def password(cc):
    return len(cc) in (4,6) and cc.isdigit()



print(password("1a3456"))
print(password("123"))
print(password("12a4"))
print(password("1234a"))
print(password("1234"))
print(password("123456"))

password("123")
password("12a4")
password("1234a")