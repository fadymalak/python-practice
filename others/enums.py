import enum

"""
 1- enumrate(Union[List,Set])
 2- enum class
"""
############# Part 1 ###################
lis = ["a", "b", "c"]
for idx in range(len(lis)):
    item = lis[idx]
    print(f"{idx} -> {item}")

# more pythonic
for idx, item in enumerate(lis):
    print(f"{idx} -> {item}")

for idx, (_, val) in enumerate({"id": "12"}.items()):
    print(f"{idx} -> {val}")
############## Part 2 #################
class Codes(enum.IntEnum):
    ok = 200
    accepted = 201
    redirect = 302


x = Codes(200)  # return Codes.ok
print(x)
print(x.value)
x2 = Codes
print(x2.ok)
