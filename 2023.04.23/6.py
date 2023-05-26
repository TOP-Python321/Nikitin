num_ticket = input()
num_list = [int(i) for i in num_ticket]
if sum(num_list[:3]) == sum(num_list[3:]):
    print('да')
else:
    print('нет')


# 912651
# да

# 632813
# нет


# ИТОГ: отлично — 3/3
