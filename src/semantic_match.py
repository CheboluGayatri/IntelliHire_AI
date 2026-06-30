from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_similarity(text1, text2):
    """
    Compute cosine similarity between two texts.
    """

    emb1 = model.encode(
        text1,
        convert_to_numpy=True
    )

    emb2 = model.encode(
        text2,
        convert_to_numpy=True
    )

    score = cosine_similarity(
        emb1.reshape(1, -1),
        emb2.reshape(1, -1)
    )[0][0]

    return float(score)