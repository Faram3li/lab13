class AUTO:
    def __init__(self, model, manufacturer, year):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year

    def change_year(self, new_year):
        self.year = new_year

    def display(self):
        print(f"Модель: {self.model}, Виробник: {self.manufacturer}, Рік випуску: {self.year}")

def create_auto_list(n):
    auto_list = []
    for _ in range(n):
        model = input("Введіть модель: ")
        manufacturer = input("Введіть виробника: ")
        year = int(input("Введіть рік випуску: "))
        auto = AUTO(model, manufacturer, year)
        auto_list.append(auto)
    return auto_list

def display_auto_list(auto_list):
    for auto in auto_list:
        auto.display()

def search_auto(auto_list, model):
    for auto in auto_list:
        if auto.model == model:
            return auto
    return None

n = int(input("Введіть кількість автомобілів: "))
auto_list = create_auto_list(n)
display_auto_list(auto_list)

search_model = input("Введіть модель для пошуку: ")
found_auto = search_auto(auto_list, search_model)
if found_auto:
    print("Знайдено автомобіль:")
    found_auto.display()
else:
    print("Автомобіль не знайдено")
