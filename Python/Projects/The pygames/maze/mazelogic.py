class MazeLogic:


    def __init__(self, maze):
        
        self.maze = maze


        # These tuples are based on how grid is being iterated in / how it was created
        self.directions = {

            'l': (0, -1),
            'r': (0, 1),
            'u': (-1, 0),
            'd': (1, 0)

        }


        self.scores = {

            'topside': 0,
            'bottomside': 0,
            'leftside': 0,
            'rightside':0

        }


        self.arrows = {

           "l": "←",
           "r": "→",
           "u": "↑",
           "d": "↓"

        }


        self.total_assignments = 0
        self.assignments = {}