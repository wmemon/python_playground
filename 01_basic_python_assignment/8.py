ids = [4353, 2314, 2956, 3382, 9362, 3900]
ids.remove(3382)
print(ids.index(9362))
ids.insert(ids.index(9362)+1,4499)
ids.extend([5566,1830])
ids.reverse()
print(f"After reversing: {ids}")
ids.sort()
print(f"After sorting:- {ids}")