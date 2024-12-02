import re

text = """
Rama is a major deity in Hinduism. +91 67894 34567
He is worshipped as the seventh and one of the most popular avatars of Vishnu.
In Rama-centric Hindu traditions,9723700141 he is considered the Supreme Being.
Also considered as the ideal man (maryāda puruṣottama),23563 23893
Rama is the male protagonist of the Hindu epic Ramayana.
His birth is celebrated every year on Rama Navami,
which falls on the ninth day of the bright half (Shukla Paksha) of the lunar cycle of Chaitra (March–April),
the first month in the Hindu calendar.(91) 97345 67345 
90345-56341
"""

mobile = r'\d{10}'
mobile1 = r'\d{5}\s\d{5}'
mobile2 = r'[+]\d{2}\s\d{5}\s\d{5}'
mobile3 = r'\d{5}[-]\d{5}'
mobile4 = r'[(]\d{2}[)]\s\d{5}\s\d{5}'

find = mobile + '|' + mobile1 + '|' + mobile2 + '|' + mobile3 + '|' + mobile4
m = re.findall(find, text)

print(m)

if m:
    print("find {0} mobile number".format(len(m)))
else:
    print("not find mobile number")