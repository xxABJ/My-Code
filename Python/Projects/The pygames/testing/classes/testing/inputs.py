from game_settings import *
import pygame

class INPUTS:
    
    _keys = {
        32: 'space',
        1073741906: 'arrow_up',
        1073741905: 'arrow_down',
        1073741904: 'arrow_left',
        1073741903: 'arrow_right',
    }
    

    def __init__(self, event):
        self.event = event
        self.event_key = event.key
        self.keys = {
            'space': False,
            'arrow_up': False,
            'arrow_down': False,
            'arrow_left': False,
            'arrow_right': False,
        }


        print(f"before try: \n{self.keys}")
        try:
            if self.key(self.event_key):
                self.keys[self.convert_key(self.event_key)] = True
                self.check_keydown()
            #else:
            #    print(f"{event_key} is not registered")

        except Exception as e:
            print(f"{e}:", e)
        
        finally:
            print(f"finally: \n{self.keys}")
            self.check_keyup()
            print()

        print(f"before reassign: {self.keys}")
        #self.keys = {
        #    'space': False,
        #    'arrow_up': False,
        #    'arrow_down': False,
        #    'arrow_left': False,
        #    'arrow_right': False,
        #}
        print(f"after reassign: {self.keys}")
        #self.check_keydown()


    def check_keydown(self):
        #print("Not yet Down")
        #print(self.event)
        if self.event.type == pygame.KEYDOWN:
            print(self.event)
            for key, value in self.keys.items():
                if key == 'space' and value == True:
                    print("SPACE!")
        

    def check_keyup(self):
        if self.event.type == pygame.KEYUP:
            for key, value in self.keys.items():
                if key == 'space' and value == True:
                    print(self.event)
                    print("SPACE!")
                    print(self.keys)


    def convert_key(self, event_key):
        return INPUTS._keys[event_key]


    def key(self, key):
        if key in INPUTS._keys:
            return True
        return