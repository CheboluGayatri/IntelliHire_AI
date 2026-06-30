from .semantic_match import get_similarity

from .feature_engineering import (
    build_candidate_text,
    experience_score,
    behavior_score,
    retrieval_score,
    role_fit_score,
    title_penalty,
)


def rank_candidates(candidates, jd_text):
    ranked = []

    for i, candidate in enumerate(candidates):

        if i % 1000 == 0:
            print(f"Processed {i}/{len(candidates)}")

        text = build_candidate_text(candidate)

        semantic = get_similarity(
            jd_text,
            text
        )

        retrieval = retrieval_score(candidate)
        role_fit = role_fit_score(candidate)
        behavior = behavior_score(candidate)
        experience = experience_score(candidate)
        penalty = title_penalty(candidate)

        final_score = (
            0.35 * semantic
            + 0.25 * retrieval
            + 0.20 * role_fit
            + 0.10 * behavior
            + 0.10 * experience
            + penalty
        )

        years = candidate["profile"]["years_of_experience"]
        title = candidate["profile"]["current_title"]
        response_rate = candidate["redrob_signals"]["recruiter_response_rate"]

        reasoning = (
            f"{title}; "
            f"{years:.1f} yrs; "
            f"response rate {response_rate:.2f}"
        )

        ranked.append(
            {
                "candidate_id": candidate["candidate_id"],
                "score": round(final_score, 4),
                "reasoning": reasoning,
            }
        )

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked