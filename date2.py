from datetime import datetime

first = input("Birinci tarixi daxil edin...(gun-ay-il)")
second = input("Ikinci tarixi daxil edin...(gun-ay-il)")

date1 = datetime.strptime(first, '%d-%m-%Y')
date2 = datetime.strptime(second, '%d-%m-%Y')

ferq = abs(date2 - date1)
print(ferq.days)