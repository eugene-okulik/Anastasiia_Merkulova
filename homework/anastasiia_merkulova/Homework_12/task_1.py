class Flower:
    origin = 'Netherlands'


    def __init__(self, flower_freshness, color, stem_length, avg_flower_lifespan, price):
        self.flower_freshness = flower_freshness
        self.color = color
        self.stem_length = stem_length
        self.avg_flower_lifespan = avg_flower_lifespan
        self.price = price


    def __repr__(self):
        return (f"{self.__class__.__name__}: "
                f"freshness={self.flower_freshness}, "
                f"color={self.color}, "
                f"stem_length={self.stem_length}, "
                f"lifespan={self.avg_flower_lifespan}, "
                f"price={self.price} ")


class Rose(Flower):
    plant_species = 'Rose'
    temp_range = '15-25°C'
    def __init__(self, flower_freshness, color, stem_length, avg_flower_lifespan, price):
        super().__init__(flower_freshness, color, stem_length, avg_flower_lifespan, price)


class Tulip(Flower):
    plant_species = 'Tulip'
    temp_range = '10-20°C'
    def __init__(self, flower_freshness, color, stem_length, avg_flower_lifespan, price):
        super().__init__(flower_freshness, color, stem_length, avg_flower_lifespan, price)

red_rose = Rose('Fresh', 'Red', 50, 10, 25)
white_rose = Rose('Fresh', 'White', 55, 8, 22)
yellow_rose = Rose('Fresh', 'Yellow' , 55, 3, 30)
orange_tulip = Tulip('Fresh', 'Orange', 30, 2, 15)
red_tulip = Tulip('Fresh', 'Red', 35, 1, 10)
yellow_tulip = Tulip('Fresh', 'Yellow', 35, 2, 12)

flower_list = [red_rose, white_rose, yellow_rose, orange_tulip, red_tulip, yellow_tulip]


class Bouquet:
    def __init__(self, flowers_list: list[Flower]):
        self.flowers_list = flowers_list


    def get_bouquet_cost(self):
        bouquet_cost = 0
        for flower in self.flowers_list:
            bouquet_cost += flower.price
        return bouquet_cost


    def flower_lifespan(self):
        average_lifespan = 0
        for flower in self.flowers_list:
            average_lifespan += flower.avg_flower_lifespan
        avg_lifespan = average_lifespan / len(self.flowers_list)
        return avg_lifespan


    def sort_flower_lifespan(self):
        return sorted(self.flowers_list, key = lambda flower: flower.avg_flower_lifespan)


    def sort_flower_color(self):
        return sorted(self.flowers_list, key = lambda flower:flower.color)


    def sort_flower_stem_length(self):
        return sorted(self.flowers_list, key = lambda flower:flower.stem_length)


    def sort_flower_price(self):
        return sorted(self.flowers_list, key = lambda flower:flower.price)


    def filter_by_avg_lifespan(self, avg_lifespan):
        return list(filter(lambda flower: flower.avg_flower_lifespan == avg_lifespan, self.flowers_list))


bouquet = Bouquet(flower_list)

print(bouquet.get_bouquet_cost())
print(bouquet.flower_lifespan())
print(bouquet.sort_flower_lifespan())
print(bouquet.sort_flower_color())
print(bouquet.sort_flower_stem_length())
print(bouquet.sort_flower_price())
print(bouquet.filter_by_avg_lifespan(8))
