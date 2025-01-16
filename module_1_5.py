immutable_var = (1, 2, True, 'Rising')
print('Immutable tuple:', immutable_var)
# immutable_var[1] = 5
# Если запустить команду изменения кортежа (второй
# элемент под номером 1) консоль выдает ошибку что
# кортеж не может быть изменен, следовательно
# данная компанда недопустима
mutable_list = [1, 2, True, 'Rising']
mutable_list.append('Higher')
print('Muteable list:', mutable_list)