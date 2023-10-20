money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
sum = money_capital + salary

while sum >= spend:
    months += 1
    sum -= spend
    sum += salary
    spend += spend * 0.05
print("Количество месяцев, которое можно протянуть без долгов:", months)
