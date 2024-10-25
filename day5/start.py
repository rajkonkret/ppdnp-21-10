# import kl2
#
# kl2.cz1.ruszaj()

import pakiet
from pakiet import fun  # import pliku z pakietu
import pakiet.fun as pk  # import jako alias

# po dodoaniu do pliku __init__ metoda jest widoczna
pakiet.powitanie()  # Cześć

# po zaimportowaniu pliku metoda jest widoczna
fun.info()  # Jestem pakietem
pk.info()  # Jestem pakietem
pk.powitanie()  # Cześć
# Cześć
# Jestem pakietem
# Jestem pakietem
# Cześć
