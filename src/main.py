from .load_data import load_candidates
from .ranking_engine import rank_candidates
from .generate_submission import generate_submission


def main():
    print("Loading candidates...")

    candidates = load_candidates("data/candidates.jsonl")

    print(f"Loaded {len(candidates)} candidates")

    with open(
        "data/job_description.txt",
        "r",
        encoding="utf-8"
    ) as f:
        jd_text = f.read()

    print("Ranking candidates...")

    ranked = rank_candidates(
        candidates,
        jd_text
    )

    print("\nTOP 10 CANDIDATES\n")

    for candidate in ranked[:10]:
        print(candidate)

    generate_submission(
        ranked,
        "outputs/submission.csv"
    )

    print("\nSubmission file generated successfully!")


if __name__ == "__main__":
    main()