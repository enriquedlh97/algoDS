import os
import sys

import pytest

from algosds.problems.categories.graphs.depth_first_search import Node

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


#  tests = [(, ),]


"""
test 1:
    input: 
        {
  "graph": {
    "nodes": [
      {"children": ["B", "C", "D"], "id": "A", "value": "A"},
      {"children": ["E", "F"], "id": "B", "value": "B"},
      {"children": [], "id": "C", "value": "C"},
      {"children": ["G", "H"], "id": "D", "value": "D"},
      {"children": [], "id": "E", "value": "E"},
      {"children": ["I", "J"], "id": "F", "value": "F"},
      {"children": ["K"], "id": "G", "value": "G"},
      {"children": [], "id": "H", "value": "H"},
      {"children": [], "id": "I", "value": "I"},
      {"children": [], "id": "J", "value": "J"},
      {"children": [], "id": "K", "value": "K"}
    ],
    "startNode": "A"
  }
}

output: ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

test 2:

input:

{
  "graph": {
    "nodes": [
      {"children": ["B", "C"], "id": "A", "value": "A"},
      {"children": ["D"], "id": "B", "value": "B"},
      {"children": [], "id": "C", "value": "C"},
      {"children": [], "id": "D", "value": "D"}
    ],
    "startNode": "A"
  }
}

output: 

["A", "B", "D", "C"]

test 3:

input: 

{
  "graph": {
    "nodes": [
      {"children": ["B", "C", "D", "E"], "id": "A", "value": "A"},
      {"children": [], "id": "B", "value": "B"},
      {"children": ["F"], "id": "C", "value": "C"},
      {"children": [], "id": "D", "value": "D"},
      {"children": [], "id": "E", "value": "E"},
      {"children": [], "id": "F", "value": "F"}
    ],
    "startNode": "A"
  }
}

output:

["A", "B", "C", "F", "D", "E"]

test 4:

input: 

{
  "graph": {
    "nodes": [
      {"children": ["B"], "id": "A", "value": "A"},
      {"children": ["C"], "id": "B", "value": "B"},
      {"children": ["D", "E"], "id": "C", "value": "C"},
      {"children": ["F"], "id": "D", "value": "D"},
      {"children": [], "id": "E", "value": "E"},
      {"children": [], "id": "F", "value": "F"}
    ],
    "startNode": "A"
  }
}

output:

["A", "B", "C", "D", "F", "E"]


test 5:

input: 

{
  "graph": {
    "nodes": [
      {"children": ["B", "C", "D", "E", "F"], "id": "A", "value": "A"},
      {"children": ["G", "H", "I"], "id": "B", "value": "B"},
      {"children": ["J"], "id": "C", "value": "C"},
      {"children": ["K", "L"], "id": "D", "value": "D"},
      {"children": [], "id": "E", "value": "E"},
      {"children": ["M", "N"], "id": "F", "value": "F"},
      {"children": [], "id": "G", "value": "G"},
      {"children": ["O", "P", "Q", "R"], "id": "H", "value": "H"},
      {"children": [], "id": "I", "value": "I"},
      {"children": [], "id": "J", "value": "J"},
      {"children": ["S"], "id": "K", "value": "K"},
      {"children": [], "id": "L", "value": "L"},
      {"children": [], "id": "M", "value": "M"},
      {"children": [], "id": "N", "value": "N"},
      {"children": [], "id": "O", "value": "O"},
      {"children": ["T", "U"], "id": "P", "value": "P"},
      {"children": [], "id": "Q", "value": "Q"},
      {"children": ["V"], "id": "R", "value": "R"},
      {"children": [], "id": "S", "value": "S"},
      {"children": [], "id": "T", "value": "T"},
      {"children": [], "id": "U", "value": "U"},
      {"children": ["W", "X", "Y"], "id": "V", "value": "V"},
      {"children": [], "id": "W", "value": "W"},
      {"children": ["Z"], "id": "X", "value": "X"},
      {"children": [], "id": "Y", "value": "Y"},
      {"children": [], "id": "Z", "value": "Z"}
    ],
    "startNode": "A"
  }
}

output:

["A", "B", "G", "H", "O", "P", "T", "U", "Q", "R", "V", "W", "X", "Z", "Y", "I", "C", "J", "D", "K", "S", "L", "E", "F",
 "M", "N"]

"""


#  @pytest.mark.parametrize("graph, answer", tests)
#  def test_depth_first_search(graph, answer):
#      assert self.depth_first_search(graph) == answer
