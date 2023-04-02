from math import inf

class TravelPlansDP:
    def __init__(self, distance : int, snack_cost : list[int]):
        # warning: do NOT change this method
        # the field representing the distance you can travel in one step
        self.distance = distance
        # the array storing what the cost of stopping at a single stop
        self.snack_cost = snack_cost
        # the number/index of the last store (naming for readability of later
        # code)
        self.max_store_num = len(self.snack_cost) - 1

        # the array to store optimal costs 
        self.opt_cost = [inf] * len(self.snack_cost)
        # the array to store optimal paths -- will use this later in lab
        self.opt_path = [[] for _ in range(len(self.snack_cost))]
        self.fill_table()


    def fill_table(self):
        """fill in the min costs and corresponding paths at every index of each
        array"""
        # TODO: implement this method!
        # Step 1: fill in the values for the leaf values from the tree
        # Step 2: fill in the values for the remaining store numbers
        # (from leaves to first store)
        pass

    def optimal_cost(self) -> int:
        """return the optimal cost starting from the first index"""
        # TODO: implement this method!
        pass

    def optimal_path(self) -> list[int]:
        """return the optimal path starting from the first index"""
        # TODO: implement this method!
        # Hint: where will the optimal path for
        # traversing the entire array be stored?
        pass


if __name__ == "__main__":
    stores1 = [1, 5, 2, 2, 4, 3]
    tp1 = TravelPlansDP(2, stores1)
    optimal_cost = tp1.optimal_cost()
    # str in Python is like toString in Java
    print("tp1 optimal cost is " + str(tp1.optimal_cost()))

    # todo: add a breakpoint here and experiment with more optimal cost
    # calculations in the debug console
    pass 