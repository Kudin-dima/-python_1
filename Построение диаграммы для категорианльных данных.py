#Построение диаграммы для категориальных данных
import matplotlib.pyplot as plt
import numpy as np

fruits = ["apple", "peach", "orange", "bannana", "melon"]
counts = [34, 25, 43, 31, 17]

plt.bar(fruits, counts) #разметки
plt.title("Fruits!")#заголовок
plt.xlabel("Fruit")#ось абсцисс
plt.ylabel("Count")#ось ординат

plt.show()