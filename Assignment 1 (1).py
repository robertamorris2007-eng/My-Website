name = input('what is your name: ')
adress = input( 'what is your street adress: ')
city = input('enter city: ')
state = input('enter state: ')
Zip = input(str('enter Zip code: '))
nuumber = input(str('what is your phone number: '))
major = input('what is your major: ')
cookies = int(input("How many cookies do you want to make? "))

sugar_per_cookie = 1.5 / 48
butter_per_cookie = 1 / 48
flour_per_cookie = 2.75 / 48

sugar_needed = sugar_per_cookie * cookies
butter_needed = butter_per_cookie * cookies
flour_needed = flour_per_cookie * cookies

print(f"\nTo make {cookies} cookies, you will need:")
print(f"{sugar_needed:.2f} cups of sugar")
print(f"{butter_needed:.2f} cups of butter")
print(f"{flour_needed:.2f} cups of flour")

