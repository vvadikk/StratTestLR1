from datetime import datetime, date

current_datetime = datetime.now()
june_1st_2025 = date(2025, 6, 1)
days_until_june_1st_2025 = (june_1st_2025 - current_datetime.date()).days
print('Сегодня', current_datetime.date())
print('Время:', current_datetime.time().strftime('%H:%M:%S'))
print('День недели:', current_datetime.weekday())
print('До 1 июня 2025', days_until_june_1st_2025, 'дней')