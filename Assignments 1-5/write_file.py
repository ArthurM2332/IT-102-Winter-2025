def collect_user_data():
    print("Please answer the following questions")
    name = input("What is your name: ")
    favorite_color = input("What is your favorite color? ")
    first_pet = input("What was your first pet's name? ")
    mothers_maiden_name = input("What is your mother's maiden name? ")
    elementary_school = input("What elementary school did you attend? ")

    return {
     "Name":name,
     "Favorite color":favorite_color,
     "First pet's name":first_pet,
     "Mother's maiden name":mothers_maiden_name, 
     "Elementary school":elementary_school
    }
def save_to_file(data, filename="hackme.txt"):
    with open(filename, "w") as file:
        for key,value in data.items():
            file.write(f"{key}: {value}\n")
    print(f"Information has been saved to {filename},")    
save_to_file(collect_user_data())        


