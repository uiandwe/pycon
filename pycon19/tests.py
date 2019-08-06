import time
from unittest import TestCase

from .solution import Solution
from .problems import problem_set


class MyTest(TestCase):
    def run(self, result=None):
        super(MyTest, self).run(result=result)

    @classmethod
    def setUpClass(cls):
        cls.solver = Solution()
        cls.start = time.time()

    def test_1(self):
        for problem, solution in problem_set:
            actual = sorted(self.solver.solve(problem))
            self.assertEqual(actual, sorted(solution))

    @classmethod
    def tearDownClass(cls):
        elapsed = time.time() - cls.start
