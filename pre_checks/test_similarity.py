from load_data import load_candidates
from feature_engineering import build_candidate_text
from semantic_match import get_similarity

candidates = load_candidates(
    "data/candidates.jsonl"
)

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as f:

    jd = f.read()

candidate_text = build_candidate_text(
    candidates[0]
)

score = get_similarity(
    jd,
    candidate_text
)

print("Similarity Score:", score)