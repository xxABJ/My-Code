# Wrappers and properties for decorators

class Icecream:
    
    # Class variables to track toppings
    chocolate = False
    sprinkles = False

    def __init__(self, flavor):
        self.flavor = flavor

        self.options()

        self.serve_icecream(cls = Icecream)
        
        
    def options(self):

        toppings = input('Do you want to add any toppings? (y/n): ').lower()
        while toppings not in ['y', 'n']:
            print('Invalid option. Please choose again.')
            toppings = input('Do you want to add any toppings? (y/n): ').lower()
        
        if toppings == 'y':
            topping = input('Chosse an option "chocolate/sprinkles" (c/s): ').lower()
            while topping not in ['c', 's']:
                print('Invalid option. Please choose again.')
                topping = input('Chosse an option "chocolate/sprinkles" (c/s): ').lower()
            
            if topping == 'c':
                Icecream.chocolate = True

                add_topping = input('Do you want to add another topping? (y/n): ').lower()
                while add_topping not in ['y', 'n']:
                    print('Invalid option. Please choose again.')
                    add_topping = input('Do you want to add another topping? (y/n): ').lower()

                if add_topping == 'y':
                    topping = input('Chosse an option "sprinkles" (s): ').lower()
                    while topping != 's':
                        print('Invalid option. Please choose again.')
                        topping = input('Chosse an option "sprinkles" (s): ').lower()
                    Icecream.sprinkles = True
                elif add_topping == 'n':
                    pass

            elif topping == 's':
                Icecream.sprinkles = True

                add_topping = input('Do you want to add another topping? (y/n): ').lower()
                while add_topping not in ['y', 'n']:
                    print('Invalid option. Please choose again.')
                    add_topping = input('Do you want to add another topping? (y/n): ').lower()

                if add_topping == 'y':
                    topping = input('Chosse an option "chocolate" (c): ').lower()
                    while topping != 'c':
                        print('Invalid option. Please choose again.')
                        topping = input('Chosse an option "chocolate" (c): ').lower()
                    Icecream.chocolate = True
                elif add_topping == 'n':
                    pass
        
        elif toppings == 'n':
            print('\n•  No toppings will be added.')

    @classmethod
    def chocolate_topping(cls, func):
        def wrapper(*args, **kwargs):
            print('•    Adding chocolate topping! 🍫')
            return func(*args, **kwargs)
        return wrapper
      
    @classmethod
    def sprinkles_topping(cls, func):
        def wrapper(*args, **kwargs):
            print('•    Adding sprinkles topping! 🌈')
            return func(*args, **kwargs)
        return wrapper

    def icecream(self):
        print(f'Serving a delicious {self.flavor} ice cream! 🍦')
    
    def serve_icecream(self, cls):
        match (Icecream.chocolate, Icecream.sprinkles):
            
            case (True, True):
                @cls.chocolate_topping
                @cls.sprinkles_topping
                def topping_wrapper():
                    self.icecream()

            case (True, False):
                @cls.chocolate_topping
                def topping_wrapper():
                    self.icecream()

            case (False, True):
                @cls.sprinkles_topping
                def topping_wrapper():
                    self.icecream()
        
        try:
            if topping_wrapper():
                print()
                topping_wrapper()
        except:
            self.icecream()
            print()

# Example usage
if __name__ == "__main__":
    my_icecream = Icecream('Vanilla')