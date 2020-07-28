capitals={'Karnataka':'Bangalore','Maharashtra':'Mumbai','Tamilnadu':'Chennai'}
print(f"Keys:- {capitals.keys()}")
print(f"Values:- {capitals.values()}")
print(f"items(Gives key-value pairs): {capitals.items()}")
print(f"{capitals.get('Karnataka')}")
print(capitals)
other_capitals = {'Gujarat': 'Ahmedabad'}
capitals.update(other_capitals)
print(capitals)
print(other_capitals)