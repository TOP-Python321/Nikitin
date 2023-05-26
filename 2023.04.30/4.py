case = {}
while True:
    inp = input('Введите число и строку через пробел: ').split()
    if not inp: 
        break
    case[inp[0]] = inp[1]

enter_value = input('Введите значение из словаря: ')

for k, v in case.items(): 
    if v == enter_value:
        print(k)
        break
else:
    print('! value error !')

# Пример ввода 1:
    # 1004 ER_CANT_CREATE_FILE
    # 1005 ER_CANT_CREATE_TABLE
    # 1006 ER_CANT_CREATE_DB
    # 1007 ER_DB_CREATE_EXISTS
    # 1008 ER_DB_DROP_EXISTS
    # 1010 ER_DB_DROP_RMDIR
    # 1016 ER_CANT_OPEN_FILE
    # 1022 ER_DUP_KEY
    # ER_CANT_CREATE_DB

# Пример вывода 1:
    # 1006

# Пример ввода 2:
    # 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
    # 4108 ER_GIPK_COLUMN_EXISTS
    # 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
    # 4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
    # 4114 ER_CTE_RECURSIVE_NOT_UNION
    # ER_CANT_OPEN_FILE

# Пример вывода 2:
    # ! value error !
    

