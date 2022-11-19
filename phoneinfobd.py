import phonenumbers
from phonenumbers import geocoder,carrier,timezone
bgreen="\033[1;32m"

logo = bgreen+str("""
███    ███ ██████         ██     ██ ███████ ██████  
████  ████ ██   ██        ██     ██ ██      ██   ██ 
██ ████ ██ ██████         ██  █  ██ █████   ██████  
██  ██  ██ ██   ██        ██ ███ ██ ██      ██   ██ 
██      ██ ██   ██ ██      ███ ███  ███████ ██████  
                                                    
                                                    
""")

print(logo)
number = input("Enter Your Number with (Country code example:+880) : ")

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(reg)