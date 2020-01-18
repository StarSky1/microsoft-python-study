import json

# Create a dictionary object
person_dict={'first':'Christopher','last':'Harrison'}
# Add additional key pairs as needed to dictionary
person_dict['City']='Seattle'

# Convert dictionary to JSON object
person_json=json.dumps(person_dict)
print(person_dict)
print(person_json)

# Create staff dictionary which assigns a person to a role 
staff_dict={}
staff_dict['Program Manager']=person_dict

# Convert dictionary to json object
staff_json=json.dumps(staff_dict)

# print json object
print(staff_dict)
print(staff_json)

# Create a list object of programming languages
languages_list=['CSharp','Python','JavaScript']
# add list to dictionary
person_dict['languages']=languages_list

# convert dictionary to json object
person_json=json.dumps(person_dict)
print(person_json)