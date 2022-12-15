
def calc_salt(mass):
    try:
        salt = int(mass) * 0.01
        return salt
    except Exception:
        print("invalid literal for int() with base 10: 'abc' ")
        return 0.0

print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))