entered_list = input("Введите список чисел, разделенных пробелом: ").split()
num_list = list(map(int, entered_list))
print("Максимальное значение:", max(num_list))
print("Максимальное значение:", min(num_list))