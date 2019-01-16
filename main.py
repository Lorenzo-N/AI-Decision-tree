import random

import Dataset
import Test

TESTS = True
random.seed(2)

plant = Dataset.load_plant_data()
krk = Dataset.load_krk_data()
poker = Dataset.load_poker_data()

if TESTS:
    print("\n\nPlant tests")
    Test.print_p_table(plant)
    Test.print_m_table(plant)

    print("\n\nChess tests")
    Test.print_p_table(krk)
    Test.print_m_table(krk)

    print("\n\nPoker tests")
    Test.print_p_table(poker)
    Test.print_m_table(poker)
else:
    Test.print_tree(plant, m=0)
