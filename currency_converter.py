#currency converter

while True:
    summ = int(input('Введите сумму: '))
    currencies = input('Выберите валюту (USD, EUR, RUS): ')
    match currencies:
        case "USD":
            print(f'{summ} USD =  {summ * 97.8478} RUB')
        case "EUR":
            print(f'{summ} EUR =  {summ * 101.3809} RUB')
        #case "EUR":
            #print(f'{summ} EUR =  {summ * 101.3809} RUB')