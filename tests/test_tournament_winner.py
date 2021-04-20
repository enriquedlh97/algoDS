import os
import sys

import pytest

from algosds.problems.categories.arrays.tournament_winner import tournament_winner

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [([
              ["HTML", "C#"],
              ["C#", "Python"],
              ["Python", "HTML"]
          ], [0, 0, 1], "Python"),
         ([
              ["HTML", "Java"],
              ["Java", "Python"],
              ["Python", "HTML"]
          ], [0, 1, 1], "Java"),
         ([
              ["HTML", "Java"],
              ["Java", "Python"],
              ["Python", "HTML"],
              ["C#", "Python"],
              ["Java", "C#"],
              ["C#", "HTML"]
          ], [0, 1, 1, 1, 0, 1], "C#"),
         ([
              ["HTML", "Java"],
              ["Java", "Python"],
              ["Python", "HTML"],
              ["C#", "Python"],
              ["Java", "C#"],
              ["C#", "HTML"],
              ["SQL", "C#"],
              ["HTML", "SQL"],
              ["SQL", "Python"],
              ["SQL", "Java"]
            ], [0, 1, 1, 1, 0, 1, 0, 1, 1, 0], "C#"),
         ([
              ["Bulls", "Eagles"]
            ], [1], "Bulls"),
         ([
              ["Bulls", "Eagles"],
              ["Bulls", "Bears"],
              ["Bears", "Eagles"]
            ], [0, 0, 0], "Eagles"),
         ([
              ["Bulls", "Eagles"],
              ["Bulls", "Bears"],
              ["Bulls", "Monkeys"],
              ["Eagles", "Bears"],
              ["Eagles", "Monkeys"],
              ["Bears", "Monkeys"]
            ], [1, 1, 1, 1, 1, 1], "Bulls"),
         ([
              ["AlgoMasters", "FrontPage Freebirds"],
              ["Runtime Terror", "Static Startup"],
              ["WeC#", "Hypertext Assassins"],
              ["AlgoMasters", "WeC#"],
              ["Static Startup", "Hypertext Assassins"],
              ["Runtime Terror", "FrontPage Freebirds"],
              ["AlgoMasters", "Runtime Terror"],
              ["Hypertext Assassins", "FrontPage Freebirds"],
              ["Static Startup", "WeC#"],
              ["AlgoMasters", "Static Startup"],
              ["FrontPage Freebirds", "WeC#"],
              ["Hypertext Assassins", "Runtime Terror"],
              ["AlgoMasters", "Hypertext Assassins"],
              ["WeC#", "Runtime Terror"],
              ["FrontPage Freebirds", "Static Startup"]
          ], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0], "AlgoMasters"),
         ([
              ["HTML", "Java"],
              ["Java", "Python"],
              ["Python", "HTML"],
              ["C#", "Python"],
              ["Java", "C#"],
              ["C#", "HTML"],
              ["SQL", "C#"],
              ["HTML", "SQL"],
              ["SQL", "Python"],
              ["SQL", "Java"]
            ], [0, 0, 0, 0, 0, 0, 1, 0, 1, 1], "SQL"),
         ([
              ["A", "B"]
            ], [0], "B")
        ]


@pytest.mark.parametrize("competitions, results, answer", tests)
def test_tournament_winner(competitions, results, answer):
    assert tournament_winner(competitions, results) == answer
