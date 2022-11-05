import datetime as dt


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        date_format = '%d.%m.%Y'
        if isinstance(date, str):
            date = dt.datetime.strptime(date, date_format).date()
        self.date = date


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, x):  #Сохранить данные
        self.records.append(x)

    def get_today_stats(self):
        date_now = dt.datetime.now().date()
        amount = [x.amount for x in self.records if date_now == x.date]
        return sum(amount)

    def get_week_stats(self): # Сколько дененг потраченно за 7 дней(коллорий полученно)
        date_now = dt.datetime.now().date()
        date_week = date_now - dt.timedelta(days=7)
        amount = [x.amount for x in self.records if date_week <= date_now]
        return sum(amount)


class Cash_calculator(Calculator):
    # USD_Rate = 60
    # EUR_Rate = 65

    def get_today_cash_remained(self, currency):
        # currency = currency
        name_currency = {"rub": ("RUB", 1),
            "usd": ("USD", 60),
            "eur": ("EUR", 65)}
        if currency in name_currency:
            names_currency, exchancge_currency = name_currency[currency]
            total_amount = self.get_today_stats()
            if self.limit - total_amount == 0:
                return f'Денег нет держись'
            elif self.limit - total_amount > 0:
                return f'На сегодня осталось {round((self.limit - total_amount)/exchancge_currency,2)} {names_currency} '
            elif self.limit - total_amount < 0:
                return f'Денег нет держись: твой долг - {round((total_amount - self.limit)/exchancge_currency,2)} {names_currency}'

r1 = Record(amount=145, comment="Безудержный шопинг", date="02.11.2022")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="03.11.2022")
r3 = Record(amount=691, comment="Катание на такси", date="04.11.2022")

cash_calculator = Cash_calculator(1000)
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=200, comment="бар в Танин др", date="05.11.2022"))
print(cash_calculator.get_today_cash_remained("usd"))
