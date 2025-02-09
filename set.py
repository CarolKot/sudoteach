# set  это множество. Неупорядоченная, уникальная коллекция элементов.
my_list = [1,2,3,4,5,6,7,8,9,10]
#my_tuple = (1,2,3, "Python" [1,2,3])
my_set = {1,2,3,4}
print(my_set)

my_list = [1,2,3,4,5,6,7,8,9,10]

my_set = {1,1,1,1,2,3,4} # set устранит дубликаты.
print(my_set)


my_set = {1,1,1,1,2,3,4} # set устранит дубликаты.
my_set.add(5) # add добавит 5.
my_set.remove(2) # remove удалит 2.
print(my_set)
