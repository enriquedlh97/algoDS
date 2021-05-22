import os
import sys

import pytest

from algosds.problems.categories.binary_search_trees.bst_construction import BST, BST_recursive, BST_iterative

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

#  tests = [(, ),]

"""

Input:

{
  "classMethodsToCall": [
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [15],
      "method": "insert"
    },
    {
      "arguments": [2],
      "method": "insert"
    },
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [13],
      "method": "insert"
    },
    {
      "arguments": [22],
      "method": "insert"
    },
    {
      "arguments": [1],
      "method": "insert"
    },
    {
      "arguments": [14],
      "method": "insert"
    },
    {
      "arguments": [12],
      "method": "insert"
    },
    {
      "arguments": [10],
      "method": "remove"
    },
    {
      "arguments": [15],
      "method": "contains"
    }
  ],
  "rootValue": 10
}

Output:

[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [2],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": "2", "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [13],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": null, "value": 15},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [22],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [1],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [14],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [12],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [10],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "12", "left": "5", "right": "15", "value": 12},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "12"
    }
  },
  {
    "arguments": [15],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "12", "left": "5", "right": "15", "value": 12},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "12"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [15],
      "method": "insert"
    }
  ],
  "rootValue": 10
}

Output:

[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [15],
      "method": "insert"
    },
    {
      "arguments": [10],
      "method": "contains"
    },
    {
      "arguments": [5],
      "method": "contains"
    },
    {
      "arguments": [15],
      "method": "contains"
    },
    {
      "arguments": [1],
      "method": "contains"
    },
    {
      "arguments": [6],
      "method": "contains"
    },
    {
      "arguments": [11],
      "method": "contains"
    },
    {
      "arguments": [16],
      "method": "contains"
    }
  ],
  "rootValue": 10
}

Output:

[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [10],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [1],
    "method": "contains",
    "output": false,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [6],
    "method": "contains",
    "output": false,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [11],
    "method": "contains",
    "output": false,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [16],
    "method": "contains",
    "output": false,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [15],
      "method": "insert"
    },
    {
      "arguments": [5],
      "method": "remove"
    },
    {
      "arguments": [15],
      "method": "remove"
    },
    {
      "arguments": [10],
      "method": "remove"
    }
  ],
  "rootValue": 10
}

Output:

[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": null, "value": 10}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [10],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": null, "value": 10}
      ],
      "root": "10"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [15],
      "method": "insert"
    },
    {
      "arguments": [10],
      "method": "contains"
    },
    {
      "arguments": [5],
      "method": "contains"
    },
    {
      "arguments": [15],
      "method": "contains"
    },
    {
      "arguments": [10],
      "method": "remove"
    },
    {
      "arguments": [5],
      "method": "remove"
    },
    {
      "arguments": [15],
      "method": "remove"
    },
    {
      "arguments": [10],
      "method": "contains"
    },
    {
      "arguments": [5],
      "method": "contains"
    },
    {
      "arguments": [15],
      "method": "contains"
    }
  ],
  "rootValue": 10
}

Output:

[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [10],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [10],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "15", "left": "5", "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "15"
    }
  },
  {
    "arguments": [5],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "15"
    }
  },
  {
    "arguments": [15],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "15"
    }
  },
  {
    "arguments": [10],
    "method": "contains",
    "output": false,
    "tree": {
      "nodes": [
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "15"
    }
  },
  {
    "arguments": [5],
    "method": "contains",
    "output": false,
    "tree": {
      "nodes": [
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "15"
    }
  },
  {
    "arguments": [15],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "15"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [2],
      "method": "insert"
    },
    {
      "arguments": [3],
      "method": "insert"
    },
    {
      "arguments": [4],
      "method": "insert"
    },
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [6],
      "method": "insert"
    },
    {
      "arguments": [7],
      "method": "insert"
    },
    {
      "arguments": [8],
      "method": "insert"
    },
    {
      "arguments": [9],
      "method": "insert"
    },
    {
      "arguments": [10],
      "method": "insert"
    },
    {
      "arguments": [11],
      "method": "insert"
    },
    {
      "arguments": [12],
      "method": "insert"
    },
    {
      "arguments": [13],
      "method": "insert"
    },
    {
      "arguments": [14],
      "method": "insert"
    },
    {
      "arguments": [15],
      "method": "insert"
    },
    {
      "arguments": [16],
      "method": "insert"
    },
    {
      "arguments": [17],
      "method": "insert"
    },
    {
      "arguments": [18],
      "method": "insert"
    },
    {
      "arguments": [19],
      "method": "insert"
    },
    {
      "arguments": [20],
      "method": "insert"
    },
    {
      "arguments": [2],
      "method": "remove"
    },
    {
      "arguments": [4],
      "method": "remove"
    },
    {
      "arguments": [6],
      "method": "remove"
    },
    {
      "arguments": [8],
      "method": "remove"
    },
    {
      "arguments": [11],
      "method": "remove"
    },
    {
      "arguments": [13],
      "method": "remove"
    },
    {
      "arguments": [15],
      "method": "remove"
    },
    {
      "arguments": [17],
      "method": "remove"
    },
    {
      "arguments": [19],
      "method": "remove"
    },
    {
      "arguments": [1],
      "method": "insert"
    },
    {
      "arguments": [2],
      "method": "insert"
    },
    {
      "arguments": [3],
      "method": "insert"
    },
    {
      "arguments": [4],
      "method": "insert"
    },
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [6],
      "method": "insert"
    },
    {
      "arguments": [7],
      "method": "insert"
    },
    {
      "arguments": [8],
      "method": "insert"
    },
    {
      "arguments": [9],
      "method": "insert"
    },
    {
      "arguments": [10],
      "method": "insert"
    },
    {
      "arguments": [9000],
      "method": "contains"
    }
  ],
  "rootValue": 1
}

Output:

[
  {
    "arguments": [2],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [3],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": null, "value": 3}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [4],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [6],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [7],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": null, "value": 7}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [8],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [9],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": null, "value": 9}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [10],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": null, "value": 10}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [11],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": null, "value": 11}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [12],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": null, "value": 12}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [13],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": null, "value": 13}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [14],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [16],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": null, "value": 16}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [17],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": null, "value": 17}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [18],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": null, "value": 18}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [19],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": null, "value": 19}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [20],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [2],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": "5", "value": 4},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [4],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": "7", "value": 6},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [6],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": "9", "value": 8},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [8],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "11", "value": 10},
        {"id": "11", "left": null, "right": "12", "value": 11},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [11],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "13", "value": 12},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [13],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "15", "value": 14},
        {"id": "15", "left": null, "right": "16", "value": 15},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [15],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "17", "value": 16},
        {"id": "17", "left": null, "right": "18", "value": 17},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [17],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "19", "value": 18},
        {"id": "19", "left": null, "right": "20", "value": 19},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [19],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": null, "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [1],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "1-2", "left": null, "right": null, "value": 1}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [2],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": null, "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [3],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "3-2", "left": null, "right": null, "value": 3},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [4],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": null, "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "3-2", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": "5-2", "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "3-2", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [6],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": "5-2", "right": "9", "value": 7},
        {"id": "9", "left": null, "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "5-2", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "3-2", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [7],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": "5-2", "right": "9", "value": 7},
        {"id": "9", "left": "7-2", "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "7-2", "left": null, "right": null, "value": 7},
        {"id": "5-2", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "3-2", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [8],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": "5-2", "right": "9", "value": 7},
        {"id": "9", "left": "7-2", "right": "10", "value": 9},
        {"id": "10", "left": null, "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "7-2", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8},
        {"id": "5-2", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "3-2", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [9],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": "5-2", "right": "9", "value": 7},
        {"id": "9", "left": "7-2", "right": "10", "value": 9},
        {"id": "10", "left": "9-2", "right": "12", "value": 10},
        {"id": "12", "left": null, "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "9-2", "left": null, "right": null, "value": 9},
        {"id": "7-2", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8},
        {"id": "5-2", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "3-2", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [10],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": "5-2", "right": "9", "value": 7},
        {"id": "9", "left": "7-2", "right": "10", "value": 9},
        {"id": "10", "left": "9-2", "right": "12", "value": 10},
        {"id": "12", "left": "10-2", "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "10-2", "left": null, "right": null, "value": 10},
        {"id": "9-2", "left": null, "right": null, "value": 9},
        {"id": "7-2", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8},
        {"id": "5-2", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "3-2", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [9000],
    "method": "contains",
    "output": false,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "3", "value": 1},
        {"id": "3", "left": "1-2", "right": "5", "value": 3},
        {"id": "5", "left": "3-2", "right": "7", "value": 5},
        {"id": "7", "left": "5-2", "right": "9", "value": 7},
        {"id": "9", "left": "7-2", "right": "10", "value": 9},
        {"id": "10", "left": "9-2", "right": "12", "value": 10},
        {"id": "12", "left": "10-2", "right": "14", "value": 12},
        {"id": "14", "left": null, "right": "16", "value": 14},
        {"id": "16", "left": null, "right": "18", "value": 16},
        {"id": "18", "left": null, "right": "20", "value": 18},
        {"id": "20", "left": null, "right": null, "value": 20},
        {"id": "10-2", "left": null, "right": null, "value": 10},
        {"id": "9-2", "left": null, "right": null, "value": 9},
        {"id": "7-2", "left": null, "right": "8", "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8},
        {"id": "5-2", "left": null, "right": "6", "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "3-2", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4},
        {"id": "1-2", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [2],
      "method": "insert"
    },
    {
      "arguments": [3],
      "method": "insert"
    },
    {
      "arguments": [4],
      "method": "insert"
    },
    {
      "arguments": [1],
      "method": "remove"
    }
  ],
  "rootValue": 1
}

Output:

[
  {
    "arguments": [2],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [3],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": null, "value": 3}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [4],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": null, "right": "2", "value": 1},
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [1],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "2", "left": null, "right": "3", "value": 2},
        {"id": "3", "left": null, "right": "4", "value": 3},
        {"id": "4", "left": null, "right": null, "value": 4}
      ],
      "root": "2"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [-2],
      "method": "insert"
    },
    {
      "arguments": [-3],
      "method": "insert"
    },
    {
      "arguments": [-4],
      "method": "insert"
    },
    {
      "arguments": [1],
      "method": "remove"
    }
  ],
  "rootValue": 1
}

Output:

[
  {
    "arguments": [-2],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": "-2", "right": null, "value": 1},
        {"id": "-2", "left": null, "right": null, "value": -2}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [-3],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": "-2", "right": null, "value": 1},
        {"id": "-2", "left": "-3", "right": null, "value": -2},
        {"id": "-3", "left": null, "right": null, "value": -3}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [-4],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "1", "left": "-2", "right": null, "value": 1},
        {"id": "-2", "left": "-3", "right": null, "value": -2},
        {"id": "-3", "left": "-4", "right": null, "value": -3},
        {"id": "-4", "left": null, "right": null, "value": -4}
      ],
      "root": "1"
    }
  },
  {
    "arguments": [1],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "-2", "left": "-3", "right": null, "value": -2},
        {"id": "-3", "left": "-4", "right": null, "value": -3},
        {"id": "-4", "left": null, "right": null, "value": -4}
      ],
      "root": "-2"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [10],
      "method": "remove"
    },
    {
      "arguments": [15],
      "method": "contains"
    }
  ],
  "rootValue": 10
}

Output:

[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [10],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "5"
    }
  },
  {
    "arguments": [15],
    "method": "contains",
    "output": false,
    "tree": {
      "nodes": [
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "5"
    }
  }
]


Input:

{
  "classMethodsToCall": [
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [15],
      "method": "insert"
    },
    {
      "arguments": [2],
      "method": "insert"
    },
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [13],
      "method": "insert"
    },
    {
      "arguments": [22],
      "method": "insert"
    },
    {
      "arguments": [1],
      "method": "insert"
    },
    {
      "arguments": [14],
      "method": "insert"
    },
    {
      "arguments": [12],
      "method": "insert"
    },
    {
      "arguments": [5],
      "method": "remove"
    },
    {
      "arguments": [5],
      "method": "remove"
    },
    {
      "arguments": [12],
      "method": "remove"
    },
    {
      "arguments": [13],
      "method": "remove"
    },
    {
      "arguments": [14],
      "method": "remove"
    },
    {
      "arguments": [22],
      "method": "remove"
    },
    {
      "arguments": [2],
      "method": "remove"
    },
    {
      "arguments": [1],
      "method": "remove"
    },
    {
      "arguments": [15],
      "method": "contains"
    }
  ],
  "rootValue": 10
}

Output:

[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [2],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": "2", "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [13],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": null, "value": 15},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [22],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [1],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [14],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [12],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "5", "left": "2", "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [12],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [13],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "14", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [14],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [22],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [2],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "1", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [1],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "10"
    }
  }
]


"""