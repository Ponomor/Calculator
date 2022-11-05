# Сохранять новую запись о приёме пищи— метод add_record()
# Считать, сколько калорий уже съедено сегодня — метод get_today_stats()
# Определять, сколько ещё калорий можно/нужно получить сегодня — метод get_calories_remained()
# Считать, сколько калорий получено за последние 7 дней — метод get_week_stats()
import datetime as dt


class Records:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        date_format = "%d.%m.%Y"
        if isinstance(date, str):
            date = dt.datetime.strptime(date, date_format).date()
        self.date = date


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_week_states(self):
        now = dt.datetime.now().date()
        week = now - dt.timedelta(days=7)
        amount = [record.amount for record in self.records if week <= now]
        return sum(amount)

    def get_today_stats(self):
        now = dt.datetime.now().date()
        amount = [record.amount for record in self.records if now == record.date]
        return sum(amount)


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        stats = self.get_today_stats()
        summa = self.limit - stats
        summa_1 = stats - self.limit
        if stats < self.limit:
            return f"Сегодня можно съесть что-нибудь ещё но не больше {summa} коллорий"
        elif stats > self.limit:
            return f"Хватит есть лимит коллорий превышен на {summa_1}"
        # Сегодня можно съесть что-нибудь ещё но не больше N
        # Хватит есть лимит коллорий превышен на N

r1 = Records(amount=1186, comment="Кусок тортика. И ещё один.", date="05.11.2022")
r2 = Records(amount=84, comment="Йогурт.", date="03.11.2022")
r3 = Records(amount=1140, comment="Баночка чипсов.", date="01.11.2022")

calories_calculator = CaloriesCalculator(limit=int(input("Ввод количества калорий(1200 для женщин, 1800 для мужчин) ")))
calories_calculator.add_record(Records(amount=300, comment="банка колы"))
calories_calculator.add_record(Records(amount=200, comment="бутерброд", date="05.11.2022"))
print(calories_calculator.get_calories_remained())