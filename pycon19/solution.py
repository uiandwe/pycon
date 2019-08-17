"""
input eg)
{
    'pikachu': ['snack', 'coke', 'hamberger'],
    'charmander': ['snack', 'coke', 'hamberger'],
    'squirtle': ['snack', ],
}
output eg)
[['pikachu', 'charmander'], ['squirtle']]
"""
import collections

class Solution:
    def solve(self, meals):
        ret_list = collections.OrderedDict()
        for item in meals.keys():
            key = '_'.join(sorted(meals[item]))
            if key in ret_list.keys():
                ret_list[key].append(item)
            else:
                ret_list[key] = [item]

        return ret_list.values()
