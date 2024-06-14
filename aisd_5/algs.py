def dynamic(capacity, weights, values, num_items):
    # Inicjalizacja tablicy pomocniczej dla przechowywania wyników
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]

    # Wypełnianie tablicy pomocniczej zgodnie z algorytmem programowania dynamicznego
    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Odtworzenie wybranych przedmiotów
    selected_items = []
    remaining_capacity = capacity
    for i in range(num_items, 0, -1):
        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:
            selected_items.append(i)
            remaining_capacity -= weights[i - 1]

    return dp[num_items][capacity], selected_items


def brute(capacity, weights, values, num_items):
    def knapsack_recursive(capacity, weights, values, n):
        if n == 0 or capacity == 0:
            return 0, []

        if weights[n - 1] > capacity:
            return knapsack_recursive(capacity, weights, values, n - 1)
        
        without_curr_value, without_indices = knapsack_recursive(capacity, weights, values, n - 1)
        with_curr_value, with_indices = knapsack_recursive(capacity - weights[n - 1], weights, values, n - 1)
        with_curr_value += values[n - 1]

        if with_curr_value > without_curr_value:
            return with_curr_value, with_indices + [n]
        else:
            return without_curr_value, without_indices

    max_value, selected_items = knapsack_recursive(capacity, weights, values, num_items)
    return max_value, list(reversed(selected_items))