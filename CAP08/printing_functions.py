def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Trasnfere cada design para completed_models após a impressão.    
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simula a criação de um impressão 3D a partir do design
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Mostre todos os modelos impressos."""
    print("\nThe fllowing models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
