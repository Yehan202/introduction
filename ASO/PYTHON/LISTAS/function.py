a = ["-u", "Bob", "-uid", "1024", "-g", "users"]

def lista():
    name = "Bob"
    uid = "1024"
    group = "users"
    return name, uid, group

name, uid, group = lista()
print(f"name: {name}, uid: {uid}, group: {group}")
