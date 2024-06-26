# В последовательности на n целых чисел умножить все элементы на первый элемент 
 
numbers = [2, 3, 4, 5, 6] 
 
first_element = numbers[0] 
 
multiplied_numbers = [num * first_element for num in numbers] 
 
print("Исходная последовательность чисел:", numbers) 
print("Результат умножения всех чисел на первый элемент:", multiplied_numbers)

# _________________________________________________________________________________________

# Составить генератор (yield), который переведёт 
# символы строки из нижнего регистра в верхний 
 
def uppercase_generator(input_string): 
    for char in input_string: 
        if char.islower(): 
            yield char.upper() 
        else: 
            yield char 
 
# Пример использования 
input_string = "И восстали машины из пепла ядерного огня" 
result = ''.join(uppercase_generator(input_string)) 
print(result)
