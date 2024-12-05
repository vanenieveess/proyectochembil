from chemlib import Compound

def percentage_composition(formula):
    """
    Calcula la composición porcentual en masa de un compuesto.
    """
    compound = Compound(formula)
    return compound.mass_percent()

formula = "C2H5OH"  # Etanol
percentages = percentage_composition(formula)
print(f"Composición porcentual en masa de {formula}:")
for element, percent in percentages.items():
  print(f"{element}: {percent:.2f}%")
