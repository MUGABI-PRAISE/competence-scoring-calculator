from competence_scoring_system import CompetenceScorer
from sample_data import create_example_criteria

# Demonstration
def example_usage():
    # Create scorer with criteria
    criteria = create_example_criteria()
    scorer = CompetenceScorer(criteria)

    # Example achievements matching the criteria structure
    achievements = {
        "academic_qualifications": {
            "PhD": 1,
            "Bachelors": "First Class"
        },
        "publications": {
            "peer_reviewed": "First Author",
            "book": 1
        },
        "teaching_experience": 5,
        "supervision": {
            "PhD": 2,
            "Masters": 3
        },
        "community_service": 1,
        "performance_conduct": 1
    }

    total_score = scorer.calculate_score(achievements)
    print(f"Total Score: {total_score}")

example_usage()

