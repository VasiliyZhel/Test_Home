def get_chips_count():
    """Функция рассчитывает количество чипсов,
    которое нужно съесть, чтоб набрать требуемое
    количество каллорий"""
    s = int(input("Сколько каллорий вы хотите набрать?: "))
    kkal_to100 = 510 # Каллорий в ста граммах продукта
    weight_one = 140 # Вес пачки
    kkal_in_one = kkal_to100 * weight_one // 100 # Каллорий в пачке
    one_gramm_kkal = kkal_in_one / weight_one # Каллорий в грамме
    itog = s / one_gramm_kkal # Итоговое количество грамм
    part_of_box = itog / weight_one # Количество пачек
    print(f"Вам необходимо съесть {itog.__round__(2)} грамм, что равняется {part_of_box.__round__(2)} Пачки ")

s = ""
while s != "нет":
    get_chips_count()
    s = input("Вы хотите продолжить?: ")