salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен
total_spend = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for _ in range(months): #считаем все затраты
    total_spend += spend
    spend *= increase

money_capital = -int(salary * months - total_spend)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
