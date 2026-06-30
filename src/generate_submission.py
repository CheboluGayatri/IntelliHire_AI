
import pandas as pd

def generate_submission(
        ranked,
        output_file
):

    rows = []

    for rank, candidate in enumerate(
            ranked,
            start=1
    ):

        rows.append({

            "candidate_id":
                candidate[
                    "candidate_id"
                ],

            "rank":
                rank,

            "score":
                candidate[
                    "score"
                ],

            "reasoning":
                candidate[
                    "reasoning"
                ]

        })

    df = pd.DataFrame(rows)

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved: {output_file}"
    )