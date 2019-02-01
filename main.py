import random
from enum import Enum, auto

import Dataset
import Test


# Modalità del programma
class MODE(Enum):
    PRINT_TABLE = auto()
    EXPORT_TABLE = auto()
    PRINT_TREE = auto()


# Settings: selezionare una modalità ed eventualmente un seed per l'ordinamento casuale dei dati
mode = MODE.PRINT_TABLE
random.seed(1)

# Caricamento dati
poker = Dataset.load_poker_data()
plant = Dataset.load_plant_data()
chess = Dataset.load_chess_data()

# Esecuzione dei test con i rispettivi output in base alla modalità selezionata
if mode == MODE.PRINT_TABLE:
    print("\n\nPlant tests")
    Test.print_p_table(plant)
    Test.print_m_table(plant)

    print("\n\nChess tests")
    Test.print_p_table(chess)
    Test.print_m_table(chess)

    print("\n\nPoker tests")
    Test.print_p_table(poker)
    Test.print_m_table(poker)
elif mode == MODE.EXPORT_TABLE:
    print("\n\nPlant tests")
    Test.export_p_table(plant)
    Test.export_m_table(plant)

    print("\n\nChess tests")
    Test.export_p_table(chess)
    Test.export_m_table(chess)

    print("\n\nPoker tests")
    Test.export_p_table(poker)
    Test.export_m_table(poker)
else:
    # Stampa l'albero di decisione creato: è possibile cambiare il data set o le impostazioni di m e p
    Test.print_tree(plant, m=0)
