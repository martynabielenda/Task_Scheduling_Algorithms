from itertools import permutations

def brute_force_algorithm(IPA, Lager, Stout):
    # Lista wszystkich permutacji kolejności produkcji
    all_permutations = permutations([IPA, Lager, Stout])
    
    # Minimalny czas produkcji ustawiony na nieskończoność
    min_production_time = float('inf')
    
    # Iteracja przez wszystkie permutacje
    for permutation in all_permutations:
        total_time = 0
        # Obliczenie łącznego czasu produkcji dla aktualnej permutacji
        for i in range(len(permutation[0])):
            total_time += max(permutation[j][i] for j in range(3))
        # Aktualizacja minimalnego czasu produkcji
        min_production_time = min(min_production_time, total_time)
    
    return min_production_time

# Przykładowe czasy trwania dla każdego rodzaju piwa (w minutach)
IPA = [60, 7 * 24 * 60, 14 * 24 * 60, 1 * 24 * 60, 1 * 24 * 60]
Lager = [90, 14 * 24 * 60, 28 * 24 * 60, 2 * 24 * 60, 1 * 24 * 60]
Stout = [75, 10 * 24 * 60, 21 * 24 * 60, 2 * 24 * 60, 1 * 24 * 60]

# Wywołanie algorytmu brute force
min_production_time_brute_force = brute_force_algorithm(IPA, Lager, Stout)

# Konwersja wyniku na dni
min_production_time_brute_force_days = min_production_time_brute_force / (24 * 60)

# Wyświetlenie wyniku
print("Minimalny czas produkcji wszystkich trzech piw (algorytm brute force):", min_production_time_brute_force_days, "dni")