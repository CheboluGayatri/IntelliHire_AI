from load_data import load_candidates

candidates = load_candidates(
    "data/candidates.jsonl"
)

keywords = [
    "machine learning",
    "ml engineer",
    "ai engineer",
    "nlp",
    "retrieval",
    "ranking",
    "recommendation",
    "search",
    "embeddings"
]

count = 0

for candidate in candidates:

    text = (
        candidate["profile"]["headline"]
        + " "
        + candidate["profile"]["summary"]
    ).lower()

    for keyword in keywords:

        if keyword in text:

            print("=" * 60)
            print(candidate["candidate_id"])
            print(candidate["profile"]["headline"])
            print(candidate["profile"]["years_of_experience"])

            count += 1
            break

    if count == 20:
        break