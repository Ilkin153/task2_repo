from datetime import datetime, timedelta

today = datetime.now()
print(today.strftime('%d-%m-%Y'))

otuz_gun = timedelta(days=30)

tarix = today + otuz_gun
print(tarix.strftime('%d-%m-%Y'))