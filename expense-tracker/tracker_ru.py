print("Добро пожаловать в трекер расходов!")
print()
print("Меню:")
print("1. Добавить расходы")
print("2. Показать все расходы")
print("3. Посчитать общие расходы")
print("4. Очистить расходы")
print("5. Выход")
expenses = []
Total = 0.0
Average = 0.0
while True:
    choice = int(input())
    if choice == 5:
        print("Вы покинули трекер расходов, пока!")
        break
    elif choice == 1:
        money = float(input())
        expenses.append(money)
        print("Успешно добавлено")
    elif choice == 2:
        if expenses == []:
            print("Расходов нет.")
        else:
            print("Твои расходы:")
            for i, amount in enumerate(expenses, 1):
                print(f"{i}. {amount}")
    elif choice == 3:
        if expenses == []:
            print("Расходов нет.")
        else:
            for i in expenses:
                Total += i
            Average = Total / len(expenses)
            print(f"Всего потрачено: {Total}")
            print(f"В среднем потрачено: {Average}")
    elif choice == 4:
        expenses.clear()
        Total = 0.0
        Average = 0.0
        print("Расходы были очищены.")
    else:
        print("Неизвестаня команда, попробуй снова!")
