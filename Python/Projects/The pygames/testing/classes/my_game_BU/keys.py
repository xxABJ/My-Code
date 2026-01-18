class Keyboard:


    #pressed_keys = {
    #    "a": False,
    #    "s": False,
    #    "d": False,
    #    "w": False,
    #    "space": False,
    #    "enter": False,
    #    "esc": False,
    #    "arrow_up": False,
    #    "arrow_down": False,
    #    "arrow_right": False,
    #    "arrow_left": False
    #}


    keys = {
        97:"a",
        115:"s",
        100:"d",
        119:"w",
        32:"space",
        13:"enter",
        27:"esc",
        1073741906:"arrow_up",
        1073741905:"arrow_down",
        1073741903:"arrow_right",
        1073741904:"arrow_left"
    }


    def __init__(self):

        self.pressed_keys = {
            "a": False,
            "s": False,
            "d": False,
            "w": False,
            "space": False,
            "enter": False,
            "esc": False,
            "arrow_up": False,
            "arrow_down": False,
            "arrow_right": False,
            "arrow_left": False
        }


    def get_key_pressed(eventkey):
        for key, value in Keyboard.keys.items():
            if key == eventkey:
                return (key, value)
        return (eventkey, "Not registered key.")


    def reset_pressed(self):
        self.pressed_keys = {
        "a": False,
        "s": False,
        "d": False,
        "w": False,
        "space": False,
        "enter": False,
        "esc": False,
        "arrow_up": False,
        "arrow_down": False,
        "arrow_right": False,
        "arrow_left": False
    }
        return

    def is_pressed(self, keystr):
        for key, value in self.pressed_keys.items():
            if key == keystr:
                #print(keystr)
                self.pressed_keys[key] = True
                return 
        self.reset_pressed()
