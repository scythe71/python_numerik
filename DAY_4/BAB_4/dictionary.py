# Dictionary adalah list yang memiliki key dan value
# Key adalah index yang kita buat sendiri
# Value adalah isi dari key tersebut
data_dict = {
    "USA": "Washington DC",
    "Indonesia": "Jakarta",
    "Malaysia": "Kuala Lumpur"
}

for key, value in data_dict.items():
    print(f"Key: {key}, Value: {value}") # Output: Key: USA, Value: Washington DC
                                         # Output: Key: Indonesia, Value: Jakarta
                                         # Output: Key: Malaysia, Value: Kuala Lumpur