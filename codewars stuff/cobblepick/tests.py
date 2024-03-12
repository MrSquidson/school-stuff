import codewars_test as test
from solution import stone_pick

@test.describe("Fixed Tests")
def Examples():
    
    @test.it("Example Test Case")
    def example_tests():
        test.assert_equals(stone_pick(["Sticks"]*4 + ["Cobblestone"]*6), 2)
        test.assert_equals(stone_pick(["Sticks"]*2 + ["Cobblestone"]*1), 0)
        test.assert_equals(stone_pick(["Sticks"]*4 + ["Wool"]*3 + ["Dirt"]*6), 0)
        test.assert_equals(stone_pick(["Wood"]*2 + ["Cobblestone"]*12), 4)
    
    @test.it("Picks greater than or equal to 1")
    def more_equal_than():
        test.assert_equals(stone_pick(["Sticks"]*4 + ["Cobblestone"]*3), 1)
        test.assert_equals(stone_pick(["Sticks"]*31 + ["Cobblestone"]*25), 8)
        test.assert_equals(stone_pick(["Sticks"]*64 + ["Cobblestone"]*64), 21)
    
    @test.it("Picks with non-eligible materials")
    def mixed_junk():
        test.assert_equals(stone_pick(["Sticks", "Wool", "Dirt", "Diamond", "Stone", "Cobblestone", "Sticks", "Cobblestone", "Cobblestone"]), 1)
        test.assert_equals(stone_pick(["Wool", "Dirt", "Diamond", "Sticks", "Cobblestone", "Cobblestone"]), 0)
        test.assert_equals(stone_pick(["Wool"]*21 + ["Sticks"]*11 + ["Stone"]*31 + ["Cobblestone"]*41 + ["Diamond"]*8), 5)
    
    @test.it("No Picks")
    def no_picks():
        test.assert_equals(stone_pick(["Wool", "Dirt", "Diamond", "Sticks"]), 0)
        test.assert_equals(stone_pick(["Wood", "Dirt", "Cobblestone", "Sticks"]), 0)
        test.assert_equals(stone_pick(["Dirt"]*51 + ["Cobblestone"]*21 + ["Sticks"] + ["Wool"]*41 + ["Diamond"]*12), 0)
    
    @test.it("Picks with only wood and no sticks")
    def wood_only():
        test.assert_equals(stone_pick(["Wood"]*51 + ["Cobblestone"]*91), 30)
        test.assert_equals(stone_pick(["Wood"]*12 + ["Cobblestone"]*120), 24)
        test.assert_equals(stone_pick(["Wood"]*33 + ["Cobblestone"]*50), 16)
    
    @test.it("No Materials")
    def none():
        test.assert_equals(stone_pick([]), 0)