import pytest

from travel_plans_dp import TravelPlansDP
from travel_plans_rec import TravelPlansRec

# TODO: implement more tests
def test_rec_and_dp_equal():
    stores1 = [1, 5, 2, 2, 4, 3]
    rec1 = TravelPlansRec(2, stores1)
    dp1 = TravelPlansDP(2, stores1)
    assert rec1.optimal_cost() == dp1.optimal_cost()
