immutable_var =(1,2,3,4,5,False,'Str')
print(immutable_var)
#immutable_var[0]=10 - 'tuple' object does not support item assignment - не поддерживает обращение по элементам
immutable_list = [1,2,True,'Str']
print(immutable_list)
immutable_list[3] = False
print(immutable_list)