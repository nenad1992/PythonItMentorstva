from methods import load_file, save_file

data = load_file("data/user.json")

data.append({
    "name": "Test Test"
})

save_file("data/user.json", data)