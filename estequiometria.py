from chemlib import Reaction

def stoichiometry(reactants, products):
    """
    Calcula los coeficientes estequiométricos para balancear una reacción química.

    :param reactants: Diccionario con los reactivos y sus cantidades iniciales.
    :param products: Diccionario con los productos y sus cantidades iniciales.
    :return: Fórmula de la reacción balanceada y los coeficientes.
    """
    reaction = Reaction(reactants, products)
    reaction.balance()
    return reaction.formula, reaction.coefficients

reactants = {"H2": 2, "O2": 1}
products = {"H2O": 2}
formula, coefficients = stoichiometry(reactants, products)
print(f"Reacción balanceada: {formula}")
print(f"Coeficientes: {coefficients}")
