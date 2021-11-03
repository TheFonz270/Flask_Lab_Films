class Order():

    def __init__(name, date, films_list):
        self.name = name
        self.date = date
        self.quantity = len(films_list)
        self.films = films_list
        self.total_price = sum(titles.film.price)