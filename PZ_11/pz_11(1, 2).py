# Средствами языка Python сформировать текстовый файл (.txt), содержащий 
# последовательность из целых положительных и отрицательных чисел. Сформировать 
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
# обработку элементов: 
 
# Исходные данные: 
# Количество чисел: 
# Положительные числа: 
# Количество положительных чисел: 
# Отрицательные числа: 
# Количество отрицательных чисел: 
 
 
# переменные 
L = ["-5 -4 -3 -2 -1 0 1 2 3 4 5"] 
 
# функции 
def from_file_to_list(str_name_file): 
  f = open(str_name_file, "r") 
  k = f.read().split() 
  for i in range(len(k)): 
    k[i] = int(k[i]) 
  f.close() 
  return k 
 
def positive_num(mas): 
  mas_positive = [] 
  for i in range(len(mas)): 
    if mas[i] > 0: 
      mas_positive.append(mas[i]) 
  return mas_positive 
 
 
def negative_num(mas): 
  mas_negative = [] 
  for i in range(len(mas)): 
    if mas[i] < 0: 
      mas_negative.append(mas[i]) 
  return mas_negative 
 
 
# запись списка в файл 
file_one = open("text_one.txt", "w") 
file_one.writelines(L) 
file_one.close() 
 
# формируем новый текстовый фал и выполняем обработку элементов 
file_two = open("text_two.txt", "w") 
mas = from_file_to_list("text_one.txt") 
 
file_two.writelines(f"Исходные данные: {mas}\n") 
file_two.writelines(f"Количество чисел: {len(mas)}\n") 
file_two.writelines(f"Положительные числа: {positive_num(mas)}\n") 
file_two.writelines(f"Количество положительных чисел: {len(positive_num(mas))}\n") 
file_two.writelines(f"Отрицательные числа: {negative_num(mas)}\n") 
file_two.writelines(f"Количество отрицательных чисел: {len(negative_num(mas))}") 
file_two.close() 
 
file_two = open("text_two.txt", "r") 
print(file_two.read()) 
file_two.close()

# _________________________________________________________________________________________

# Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое, 
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст 
# в стихотворной форме предварительно заменив все знаки пунктуации на знак «!». 
 
# переменные 
marks = '''!,()-[]{};?@#$%:'"./^&amp;*_''' 
 
# функции 
def count_upper(Str): 
  count = 0 
  for i in range(len(Str)): 
    if Str[i].isupper(): 
      count += 1 
  return count 
 
def replacement_signs(Str): 
  for i in range(len(Str)): 
    if Str[i] in marks: 
      Str = Str.replace(Str[i], '!') 
  return Str 
 
# программа 
file_one = open("бородино.txt", "r", encoding='utf-8') 
str_text = file_one.read() 
print("<----------содержимое первого файла---------->") 
print(str_text) 
print("<-------------------------------------------->") 
print(f"количество букв в верхнем регистре: {count_upper(str_text)}\n") 
file_one.close() 
 
file_two = open("new_file.txt", "w", encoding='utf-8') 
file_two.writelines(replacement_signs(str_text)) 
file_two.close() 
 
file_two = open("new_file.txt", "r") 
print("<----------содержимое второго файла---------->") 
print(file_two.read()) 
print("<-------------------------------------------->") 
file_two.close()
