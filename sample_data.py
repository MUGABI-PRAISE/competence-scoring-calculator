# Example criteria
def create_example_criteria():
    return {
        "academic_qualifications": {
            "PhD": 12,
            "Masters": 8,
            "Bachelors": {
                "First Class": 6,
                "Second Upper": 4
            }
        },
        "publications": {
            "peer_reviewed": {
                "First Author": 4,
                "Corresponding": 2,
                "Co-Author": 1
            },
            "book": 12,
            "book_chapter": 4
        },
        "teaching_experience": 1,  # Simple score for each year of experience
        "supervision": {
            "PhD": 6,
            "Masters": 2
        },
        "community_service": 5,  # Fixed score
        "performance_conduct": 3  # Fixed score
    }
