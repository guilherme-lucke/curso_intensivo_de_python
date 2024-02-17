def get_city_country(city, country, population=''):
    if population:
        formatted = city.title() + ", " + country.title() + \
            " - população " + str(population) + "."
    else:
        formatted = city.title() + ", " + country.title() + "."
    return formatted
