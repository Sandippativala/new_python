import re

text = """
Rama is a major deity in Hinduism.
He is worshipped as the seventh and one of the most popular avatars of Vishnu.
In Rama-centric Hindu traditions,krunal_pati90_.vala@gmail.com he is considered the Supreme Being.
Also considered as the ideal man (maryāda puruṣottama),sandip_pativala123@gmail.com
Rama is the male protagonist of the Hindu epic Ramayana.
His birth is celebrated every year on Rama Navami,
which falls on the ninth day of the bright half (Shukla Paksha) of the lunar cycle of Chaitra (March–April),
the first month in the Hindu calendar.   
pativlala.krunal@gmail.com
"""

email = r'[a-z]+[a-z0-9._]+@[a-z]{4,}+\.[a-z]{2,}'
    
e = re.findall(email, text)

print(e)

if e:
    print("find {0} valid email".format(len(e)))
else:
    print("invalid email")