records = {
    "name": "Aditya", 
    "ID": 67, 
    "age": 19, 
    "fav_col": "red"
    }
name_of_student = records.get("name")
id = records.get("ID")
age = records.get("age")
fav = records.get("fav_col")
records["age"] = 21
print(f"Name : {name_of_student}")
print(f"ID no. : {id}")
print(f"Age : {age}")
print(f"Favourite color : {fav}")
group = {"group":"yellow"}
records.update(group)
print(records)
