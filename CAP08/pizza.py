def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos a preparar."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green_peppers','extra_cheese')