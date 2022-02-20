# cat = {'number_of_legs': 4,
#        'tail': True,
#        'color': 'Black'}
#
# cat_2 = {'number_of_legs': 4,
#          'tail': True,
#          'color': 'Black'}
#
# cat_3 = {'number_of_legs': 4,
#          'tail': True,
#          'color': 'Black'}


def say_color(c):
    print(c['color'])



class Cats:

    NUMBER_LEGS = 4
    TAIL = True
    COUNT_OF_LIFES = 9

    def __init__(self, color, name, weight=5):
        self.color = color
        self.name = name
        self.weight = weight
        if not isinstance(color, str):
            self.color = None

        self.amount_of_mices = []

    def say_name(self):
        print(self.name)

    def walk(self, num_steps):
        if isinstance(num_steps, int):
            print(f'{self.name} walked {num_steps} steps.')
        else:
            print("Inappropriate step amount")

    def count_food(self, k=1.5, n_days=7):
        aof = (self.weight * k) * n_days
        print(f"{self.name} needs {aof}kg of food")
        return aof

    def diet(self, kg_per_day, n_days):
        print(f"Init weight of {self.name}: {self.weight}")
        self.weight += kg_per_day * n_days
        print(f"{self.name} is now have weight {self.weight}")

    def cought_mice(self):
        self.amount_of_mices.append(1)



cat_1 = Cats("Red", "Peach")
cat_2 = Cats("Black", "Ugol", 10)
cat_3 = Cats(3, "Murchik", 3)

print(cat_1 == cat_2)

# cat_1.say_name()
# cat_2.say_name()

# food_for_cat_3 = cat_3.count_food(k=0.3, n_days=10)
# print(food_for_cat_3)

# cat_2.diet(-0.3, 10)

# for i in range(10):
#     cat_1.cought_mice()
#
# print(cat_1.amount_of_mices)
# print(len(cat_1.amount_of_mices))
"""
a = Strings('4545')
"""
