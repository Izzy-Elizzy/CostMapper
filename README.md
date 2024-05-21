# Livability Rating Map

This project aims to provide a comprehensive livability rating for different locations, presented in the form of an interactive map. The livability rating is calculated based on various factors such as housing prices, rent, mortgage rates, food costs, utility costs, and median salaries. Users can explore the map and view the livability ratings for different areas.

ACCESS HERE: https://izzy-elizzy.github.io/CostMapper/
             
             

## Features

- **Interactive Map**: Explore an interactive map displaying livability ratings for different locations.
- **Livability Rating Calculation**: The livability rating is calculated using a weighted average approach, considering factors such as housing prices, rent, mortgage rates/costs, food costs, utility costs, and median salaries.
- **Customizable Weights**: Users can adjust the weights assigned to each factor, reflecting their personal preferences and priorities.
- **Normalized Scoring**: Each factor is scored on a scale of 0 to 1, where higher values are more desirable (except for housing, rent, mortgage, food, and utility costs, where lower values are more desirable).
- **National Median Reference**: The scoring is based on the comparison of local values with national/overall median values, providing a more representative baseline.

## Usage

1. **Open the Interactive Map**: Access the interactive map by visiting the project's website or running the application locally.
2. **Explore the Map**: Navigate through the map to view the livability ratings for different locations. The ratings are visually represented using color coding or other indicators.
3. **Customize Weights (Optional)**: Adjust the weights assigned to each factor by using the provided sliders or input fields. This allows you to prioritize the factors that are most important to you.
4. **View Details**: Click on a specific location to access more detailed information, including the individual factor scores and the overall livability rating.

## Formulas

The following formulas are used to calculate the individual scores:

- **Housing Score**: `Housing Score = 1 / (1 + (Housing Price / National Median Housing Price))` ✔️ - 5-21
- **Rent Score**: `Rent Score = 1 / (1 + (Rent Value / National Median Rent))`✔️ - 5-21
- **Mortgage Score**: `Mortgage Score = 1 / (1 + (Mortgage Rate/Cost / National Median Mortgage Rate/Cost))`
- **Food Score**: `Food Score = 1 / (1 + (Food Cost / National Median Food Cost))`
- **Utilities Score**: `Utilities Score = 1 / (1 + (Utility Cost / National Median Utility Cost))`
- **Salary Score**: `Salary Score = 1 / (1 + (National Median Salary / Median Salary))`✔️ - 5-21

The overall livability rating is calculated using the following equation:

```
Livability Rating = (w1 * Housing Score + w2 * Rent Score + w3 * Mortgage Score + w4 * Food Score + w5 * Utilities Score + w6 * Salary Score) / (w1 + w2 + w3 + w4 + w5 + w6)
```

## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).
