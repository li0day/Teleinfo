import pyfiglet as pyfiglet
import phonenumbers

print(pyfiglet.figlet_format("Teleinfo"))


print("Autor = li0day")
print("E-mail = li0day@tutanota.com")
print("Instagram = https://www.instagram.com/li0day/")
print("Wersja = 1.0")


from phonenumbers import is_possible_number, is_valid_number, parse
from phonenumbers import carrier, geocoder, timezone

print("~" * 50) 
print("~" * 50) 

mobileNo = input("Podaj numer telefonu z prefixem dla kraju")
mobileNo = phonenumbers.parse(mobileNo)

# get timezone a phone number
print(timezone.time_zones_for_number(mobileNo))

# Getting carrier of a phone mobile
print(carrier.name_for_number(mobileNo, "en"))

# Getting region information
print(geocoder.description_for_number(mobileNo, "en"))

# Validating a phone number
print("Ważność numeru telefonu :", is_valid_number(mobileNo))

# Checking possibility of a number
print("Możliwość numeru telefonu :", is_possible_number(mobileNo))
input()
