from datetime import date, time

def trabalhando_com_date():
    date_atual = date.today()
    data_atual_str = date_atual.strftime('%A %B %Y')
    print(type(date_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    time(hour=15, minute=18,)


if __name__ == '__main__':
    trabalhando_com_date()
