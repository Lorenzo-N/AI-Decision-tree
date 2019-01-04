import Dataset
import Test

TESTS = False
plant = Dataset.load_plant_data()
poker = Dataset.load_poker_data()

if TESTS:
    print("\n\nPlant tests")
    Test.print_p_table(plant)
    Test.print_m_table(plant)

    print("\n\nPoker tests")
    Test.print_p_table(poker)
    Test.print_m_table(poker)
else:
    Test.print_tree(poker, m=0)
