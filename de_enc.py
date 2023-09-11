import json

input_file_path = "de_ini.json" 
output_file_path_de = "de_ini2.json"

try:
    with open(input_file_path, "r") as input_file:
        input_data = json.load(input_file)

except FileNotFoundError:
    print(f"Input file '{input_file_path}' not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error decoding JSON in '{input_file_path}'. Make sure it's a valid JSON file.")
    exit(1)

# Step 2: Process the JSON data (e.g., you can modify or analyze the data  here)
# For example, let's add a new key-value pair to each item in a list

# for item in input_data:
#     item["processed"] = True

def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_uu(json_data, key):
    # Make a deep copy of the input JSON data
    encrypted_json = json_data.copy()

    # Encrypt the "uu" values in the "l_s" list
    for item in encrypted_json["l_s"]:
        item["uu"] = caesar_cipher(item["uu"], key)
        item["nn"] = caesar_cipher(item["nn"], key)

    encrypted_json["tit1"] = caesar_cipher(encrypted_json["tit1"], key)


    return encrypted_json



# Encryption key (you can choose any integer)
encryption_key = 9

# Encrypt the "uu" values and get the modified JSON
encrypted_json = encrypt_uu(input_data, encryption_key)


try:
    with open(output_file_path_de, "w") as output_file:
        json.dump(encrypted_json, output_file, indent=2)  # Indent for pretty formatting
except Exception as e:
    print(f"Error occurred while writing to the output JSON file: {str(e)}")
    exit(1)


print(f"Processed JSON data saved to '{output_file_path_de}' successfully.")

