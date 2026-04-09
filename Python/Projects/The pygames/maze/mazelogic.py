class MazeLogic:


    def __init__(self, maze):
        
        self.maze = maze


        # These tuples are based on how grid is being iterated in / how it was created
        self.directions = {

            'u': (-1, 0),
            'd': (1, 0),
            'l': (0, -1),
            'r': (0, 1)

        }


        self.scores = {

            'topside': 0,
            'bottomside': 0,
            'rightside':0,
            'leftside': 0

        }


        self.arrows = {

           "u": "↑",
           "d": "↓",
           "r": "→",
           "l": "←"

        }


        self.score_direction_translated = {

            "u": "topside",
            "d": "bottomside",
            "r": "rightside",
            "l": "leftside"

        }


        self.total_assignments = 0
        self.assignments = {}