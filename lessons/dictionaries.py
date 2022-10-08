"""demonstrating capabilities of a dictionary."""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize into an empty dictionary
schools = dict()

# Set a keyword value into the dictionary
schools['UNC'] = 19_400
schools['DUKE'] = 6_717
schools['NCSU'] = 26_150

# Print a dictionary literal representation
# print(schools)

# Printing with a dictionary
# print(f"UNC had { schools['UNC'] } students.")

# Remove a key-value pair from a dictionary
# by its key
# schools.pop('DUKE')

#est for the existence of a key
is_duke_present: bool = 'DUKE' in schools
# print(f"DUKE is present: { is_duke_present }")

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")