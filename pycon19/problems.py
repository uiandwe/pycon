import json
import os


problem_set = [
    (
        {
            'a': 'ham meat ham coke',
            'b': 'ham cider sandwitch blah',
            'c': 'ham ham coke meat',
        },
        [['a', 'c'], ['b']]
    ),
]


if 'PYCON19_SOLUTION' in os.environ:
    with open(os.environ['PYCON19_SOLUTION'], 'r') as fp:
        problem_set.extend(json.load(fp))
