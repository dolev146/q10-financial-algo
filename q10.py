import statistics
from typing import List

def compute_budget(total_budget: float, citizen_preferences: List[List[float]]) -> List[float]:
    """
    This function uses a binary search approach to find a budget distribution based on the generalized median voting scheme with linear ascending functions.   
    Parameters:
    - total_budget (float): The total budget available for distribution.
    - citizen_preferences (List[List[float]]): A list of lists, where each inner list represents a
      single citizen's preference distribution across different options.
    Returns:
    - List[float]: The optimized budget distribution across options.
    The algorithm finds the right way to divide the money by repeating steps.
    It uses a rule that changes each person's choice into a straight line.
    Then, it combines these lines and finds the middle value to get close to what everyone wants.
    It makes sure the total money given out does not go over the total money available.
    """
    start = 0
    end = 1
    while end > start:
        linear_functions = []
        merged_preferences = []
        midpoint = (start + end) / 2
        for index in range(1, len(citizen_preferences)):
            linear_function = total_budget * min(1, index * midpoint)
            linear_functions.append(linear_function)
            print(f'Linear Function for index {index}: {linear_function}')
        print(f'Linear Functions : {linear_functions}')
        for option_index in range(len(citizen_preferences[0])): 
            option_preferences = []
            for preferences in citizen_preferences:
                option_preferences.append(preferences[option_index])
            option_preferences += linear_functions
            merged_preferences.append(option_preferences)
        median_values = [statistics.median(preferences) for preferences in merged_preferences]
        total_median_budget = sum(median_values)
        if total_median_budget < total_budget:
            start = midpoint
        elif total_median_budget > total_budget:
            end = midpoint
        elif total_median_budget == total_budget:
            return median_values
    return median_values

if __name__ == '__main__':
    # Example calls to compute_budget
    print(compute_budget(100, [[100, 0, 0], [0, 0, 100]])) # [50.0, 0, 50.0]
    print(compute_budget(30, [[6, 6, 6, 6, 0, 0, 6, 0, 0], [0, 0, 6, 6, 6, 6, 0, 6, 0], [6, 6, 0, 0, 6, 6, 0, 0, 6]])) # [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 2.0, 2.0, 2.0]
    print(compute_budget(130, [[100, 30, 0], [15, 100, 15], [50, 50, 30]])) # [50, 50, 30]


