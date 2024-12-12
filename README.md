# Competence Scoring Calculator Library

## Overview

The Competence Scoring Calculator Library is a Python package designed to calculate competence scores for employees in an organization. It helps assess employees based on a set of evaluation criteria and their corresponding achievements.

## Features

- Accepts evaluation criteria and individual competence achievements as inputs.
- Calculates the total score based on achieved criteria.

## Installation

To use the Competence Scores Library, clone the repository and install the package:

```bash
# Clone the repository
git clone https://github.com/MUGABI-PRAISE/competence-scoring-calculator.git

# Navigate to the project directory
cd competence-scoring-calculator

# Install the library
pip install .
```


## Usage

Below is a step-by-step guide to using the library.

### Import the Library

```python
from competence_scoring_system import CompetenceScorer
from sample_data import create_example_criteria

Note: CompetenceScorer is the class containing the logic
    To ensure modularity, we are separating the file for you to put the individual achievements, that is sample data.
    
    create_example_criteria is a sample dictionary showing a criteria to evaluate employees
```

### Inputs

1. **Evaluation Criteria**: A dictionary where keys are the criterion names and values are their respective weights.
   Example:

   ```python
   evaluation_criteria = {
       'Technical Skills': 40,
       'Teamwork': 30,
       'Problem Solving': 20,
       'Punctuality': 10
   }
   ```

2. **Achievements**: A dictionary where keys match the evaluation criteria and values represent the scores achieved by the employee.
   Example:

   ```python
   achievements = {
       'Technical Skills': 35,
       'Teamwork': 25,
       'Problem Solving': 18
       # 'Punctuality' is missing, indicating it wasn't achieved
   }
   ```

### Calculate the Score

Call the `calculate_score` function with the evaluation criteria and achievements:

```python
total_score = scorer.calculate_score(achievements)
    print(f"Total Score: {total_score}")
```

### Output

The function returns the total score as an integer or float, depending on the weights and achievements.

Example Output:

```
Total Competence Score: 88
```

## Example Code

Here's a complete example:

```python
from competence_scores import calculate_score

evaluation_criteria = {
    'Technical Skills': 40,
    'Teamwork': 30,
    'Problem Solving': 20,
    'Punctuality': 10
}

achievements = {
    'Technical Skills': 35,
    'Teamwork': 25,
    'Problem Solving': 18
}

total_score = calculate_score(evaluation_criteria, achievements)
print(f"Total Competence Score: {total_score}")
```

## Handling Missing Keys

If an achievement is missing for a specific criterion, it is treated as unachieved. For example, if `Punctuality` is missing from the `achievements` dictionary, the score for that criterion will default to `0`.

## Testing

Run the test suite to ensure the library works as expected:

```bash
pytest
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

## License

This library is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or support, please reach out to [[ mugabipraise4@gmail.com](mailto\:mugabipraise4@gmail.com)].

