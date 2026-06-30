def build_candidate_text(candidate):

    text = []

    profile = candidate["profile"]

    text.append(profile.get("headline", ""))
    text.append(profile.get("summary", ""))
    text.append(profile.get("current_title", ""))

    for exp in candidate["career_history"]:

        text.append(exp.get("title", ""))
        text.append(exp.get("description", ""))

    for skill in candidate["skills"]:

        text.append(skill.get("name", ""))

    return " ".join(text)


def experience_score(candidate):

    years = candidate["profile"][
        "years_of_experience"
    ]

    if 5 <= years <= 9:
        return 1.0

    elif 3 <= years <= 12:
        return 0.7

    return 0.3


def behavior_score(candidate):

    s = candidate["redrob_signals"]

    score = 0

    if s["open_to_work_flag"]:
        score += 0.20

    score += s["recruiter_response_rate"] * 0.25

    score += s["interview_completion_rate"] * 0.20

    score += (
        s["profile_completeness_score"]
        / 100
    ) * 0.15

    score += (
        min(
            s["saved_by_recruiters_30d"],
            20
        ) / 20
    ) * 0.20

    return min(score, 1.0)


def retrieval_score(candidate):

    text = ""

    for exp in candidate["career_history"]:

        text += (
            exp["title"] + " "
            + exp["description"]
        ).lower()

    keywords = [

        "retrieval",
        "ranking",
        "recommendation",
        "search",
        "embeddings",
        "vector",
        "faiss",
        "milvus",
        "pinecone",
        "weaviate",
        "qdrant",
        "elasticsearch",
        "opensearch"

    ]

    matches = 0

    for word in keywords:

        if word in text:
            matches += 1

    return min(matches / 5, 1.0)


def role_fit_score(candidate):

    text = ""

    for exp in candidate["career_history"]:

        text += (
            exp["title"] + " "
            + exp["description"]
        ).lower()

    roles = [

        "ai engineer",
        "ml engineer",
        "machine learning engineer",
        "data scientist",
        "nlp engineer",
        "applied scientist",
        "recommendation",
        "search engineer"

    ]

    score = 0

    for role in roles:

        if role in text:
            score += 1

    return min(score / 3, 1.0)


def title_penalty(candidate):

    title = candidate["profile"][
        "current_title"
    ].lower()

    bad_titles = [

        "marketing",
        "hr",
        "accountant",
        "content writer",
        "graphic designer",
        "customer support"

    ]

    for bad in bad_titles:

        if bad in title:
            return -0.25

    return 0