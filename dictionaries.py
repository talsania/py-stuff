# dictionaries
band = {
    "vocals": 'plant',
    "guitar": "page"
}
band2 = dict(vocals = "plant", guitar = "page")
print(band)
print(band2)
print(type(band))
print(len(band))
# access items
print(band["vocals"])
print(band.get("guitar"))
# list all keys
print(band.keys())
# list all values
print(band.values())
# list of key-value pairs as tuples
print(band.items())
# verify a key exists
print("guitar" in band)
print("triangle" in band)
# change values
band["vocals"] = "coverdale"
band.update({"bass": "JPJ"})
print(band)
# remove items
print(band.pop("bass"))
print(band)
band["drums"] = "bonham"
print(band)
print(band.popitem())  # tuple
print(band)
# del and clear
band["drums"] = "bonham"
del band["drums"]
print(band)
band2.clear()
print(band2)
del band2
# copy dictionaries
# band2 = band  # create a refrence
# print("bad copy!")
# print(band2)
# print(band)
# band2["drums"] = "dave"
# print(band)
band2 = band.copy()
band2["drums"] = "dave"
print("good copy!")
print(band)
print(band2)
# or use the dict() constructor func
band3 = dict(band)
print("good copy!")
print(band3)
# nested dictionaries
member1 = {
    "name": "plant",
    "instrument": "vocals"
}
member2 = {
    "name": "plant",
    "instrument": "vocals"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])