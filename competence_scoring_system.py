from typing import Dict, Any

class CompetenceScorer:
    def __init__(self, criteria: Dict[str, Any]):
        """
        Initialize the scorer with predefined criteria.
        :param criteria: A dictionary containing scoring criteria for different competence areas.
        """
        self.criteria = criteria

    def calculate_score(self, achievements: Dict[str, Any]) -> float:
        """
        Calculate total score based on achievements against predefined criteria.
        :param achievements: A dictionary of candidate's achievements
        :return: Total calculated score
        """
        total_score = 0

        for area, scoring_rules in self.criteria.items():
            # Skip areas that are not in achievements
            if area not in achievements:
                continue

            # If the scoring rule is a simple numeric value, add it directly
            if isinstance(scoring_rules, (int, float)):
                total_score += scoring_rules if achievements[area] else 0

            # If the scoring rule is a dictionary, handle it accordingly
            elif isinstance(scoring_rules, dict):
                area_score = 0

                # Iterate through achievements in the current area
                for achievement_type, achievement_value in achievements[area].items():
                    # Check if the achievement type is in the scoring rules
                    if achievement_type in scoring_rules:
                        score = scoring_rules[achievement_type]
                        if isinstance(score, (int, float)):
                            area_score += score

                total_score += area_score

        return total_score

    @classmethod
    def from_json(cls, json_file: str):
        """
        Create a scorer instance from a JSON file.
        :param json_file: Path to the JSON file containing criteria
        :return: CompetenceScorer instance
        """
        import json
        with open(json_file, 'r') as f:
            criteria = json.load(f)
        return cls(criteria)
