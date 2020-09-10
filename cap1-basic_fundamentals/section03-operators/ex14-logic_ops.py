fui_ao_cinema = False
escovei_os_dentes = True
ouvi_música = False
programei = True

# Or
print(bool(fui_ao_cinema or escovei_os_dentes)) # True
print(bool(fui_ao_cinema or ouvi_música)) # False

print()

# And
print(bool(programei and escovei_os_dentes)) # True
print(bool(programei and ouvi_música)) # False

print()

# Not
print(bool(not ouvi_música)) # True
print(bool(not programei)) # False

print()