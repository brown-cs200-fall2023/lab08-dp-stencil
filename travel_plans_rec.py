from math import inf # for infinity

class TravelPlansRec:
    def __init__(self, distance : int, snack_cost : list[int]):
        # the field representing the distance (# of steps) you can travel before stopping 
        self.distance = distance
        # the array storing the cost of stopping at a single store
        # indices are the store numbers, values are the corresponding snack costs
        self.snack_cost = snack_cost
        # the number/index of the last store (naming for readability of later code)
        self.max_store_num = len(self.snack_cost) - 1

    def optimal_cost(self) -> int:
        return self.optimal_cost_helper(0)

    def optimal_cost_helper(self, index : int) -> int:
        # if index names a store within allowed distance to destination
        #   can finish trip after stopping only at this store
        if index > (self.max_store_num - self.distance):
            return self.snack_cost[index]
        else: # will need later stops
            min_value = inf
            # try each next allowed stop and use the smallest value
            # range goes from first number to second number - 1
            for next_stop in range(index + 1, index + self.distance + 1):
                compare = self.optimal_cost_helper(next_stop)
                if compare < min_value:
                    min_value = compare

            return self.snack_cost[index] + min_value


if __name__ == "__main__":
    test = TravelPlansRec(2, [1, 5, 2, 2, 4, 3])
    optimal_cost = test.optimal_cost()
    print(optimal_cost)
