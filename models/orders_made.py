from models.films import Film
from models.orders import Order

film1 = Film("The Fellowship of the Ring", 10, 178)
film2 = Film("The Two Towers", 10, 179)
film3 = Film("The Return of the King", 10, 179)
film4 = Film("Home Alone", 5, 103)
film5 = Film("Elf", 5, 97)

order1 = Order("Phil", "02/11/21", [film1, film2, film3])
order2 = Order("Nick", "24/12/21", [film4, film5])

orders_list = [order1, order2]