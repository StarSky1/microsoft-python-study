def get_initial(name,force_uppercase=True):
    if force_uppercase:
        initial=name[0:1].upper()
    else:
        initial=name[0:1]
    return initial

first_name=input('enter your first name:')
# first_name_initial=get_initial(first_name)
first_name_initial=get_initial(force_uppercase=True,\
                                    name=first_name)

print('Your initial is: '+first_name_initial)

def error_logger(error_code,error_serverity,log_to_db,error_message,source_module):
    print('oh no error: '+error_message)
    # Imagine code here that logs our error to a database or file 

first_number=10
second_number=5
# 函数调用的名字命名表示法
if first_number > second_number:
    error_logger(error_code=45,error_serverity=1,\
        log_to_db=True,error_message='Second number greater than first',\
            source_module='my_math_method')