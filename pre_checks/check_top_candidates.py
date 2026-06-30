from load_data import load_candidates

candidates = load_candidates("data/candidates.jsonl")

for c in candidates[:5]:

    print("=" * 50)

    print(c["candidate_id"])

    print(c["profile"]["headline"])

    print(c["profile"]["years_of_experience"])

    print(c["redrob_signals"]["recruiter_response_rate"])

    print(c["redrob_signals"]["open_to_work_flag"])