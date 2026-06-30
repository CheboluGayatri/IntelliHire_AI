# 🚀 Intelligent Candidate Discovery & Ranking System

> An AI-powered candidate ranking system that intelligently matches candidates with job descriptions using semantic understanding, behavioral signals, and multi-factor scoring.

---

## 📌 Problem Statement

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, often overlooking highly relevant candidates and ranking irrelevant profiles.

This project aims to develop an intelligent candidate ranking system that understands the actual meaning behind candidate profiles and job descriptions using Artificial Intelligence and Natural Language Processing techniques.

---

## 🎯 Objectives

- Improve candidate-job matching accuracy.
- Go beyond traditional keyword-based systems.
- Incorporate semantic understanding.
- Consider behavioral and experience signals.
- Generate explainable candidate rankings.

---

## 💡 Solution Overview

The proposed system combines:

- Semantic similarity matching
- Experience analysis
- Behavioral signal evaluation
- Role-fit analysis
- Retrieval expertise evaluation
- Weighted candidate ranking

The final output is a ranked list of candidates along with reasoning for each recommendation.

---

## ⚙️ Features

✅ Semantic candidate matching

✅ Multi-factor ranking system

✅ Behavioral signal analysis

✅ Experience evaluation

✅ Role-fit analysis

✅ Explainable AI recommendations

✅ Lightweight and scalable architecture

---

## 🏗️ System Architecture

```text
                 Job Description
                        │
                        ▼
             Semantic Embedding Model
                        │
                        ▼
               Candidate Profiles
                        │
                        ▼
              Feature Engineering
                        │
        ┌────────┬─────────┬────────┐
        ▼        ▼         ▼        ▼

 Experience  Behavior  Role Fit  Retrieval

        └────────┬─────────┬────────┘
                 ▼
            Ranking Engine
                 ▼
           Final Candidate Rank
```

---

## 🔄 Workflow

```text
Job Description
        ↓
Load Candidate Profiles
        ↓
Feature Engineering
        ↓
Semantic Matching
        ↓
Feature Scoring
        ↓
Weighted Ranking
        ↓
Ranked Candidates
        ↓
Submission CSV
```

---

## 🧠 Candidate Signals

### Technical Signals
- AI/ML skills
- Search systems
- Recommendation systems
- Retrieval systems

### Experience Signals
- Years of experience
- Industry exposure
- Previous roles

### Behavioral Signals
- Recruiter response rate
- Open-to-work status
- Interview completion rate
- Profile completeness

### Role Fit Signals
- Current designation
- Career history
- Relevant domain expertise

---

## 🤖 Semantic Matching

The system uses:

- **Sentence Transformers**
- **all-MiniLM-L6-v2**
- **Cosine Similarity**

This enables the model to understand the context and meaning of candidate profiles instead of relying only on keywords.

---

## 📊 Ranking Methodology

The final score is calculated using weighted scoring:

```python
Final Score =

0.35 × Semantic Similarity

+ 0.25 × Retrieval Score

+ 0.20 × Role Fit Score

+ 0.10 × Behavioral Score

+ 0.10 × Experience Score

+ Title Penalty
```

---

## 📂 Project Structure

```text
Intelligent-Candidate-Ranking/
│
├── data/
│   ├── candidates.jsonl
│   └── job_description.txt
│
├── load_data.py
├── semantic_match.py
├── feature_engineering.py
├── ranking_engine.py
├── generate_submission.py
├── main.py
│
├── outputs/
│   └── submission.csv
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core development |
| Sentence Transformers | Embeddings |
| Scikit-learn | Cosine similarity |
| Pandas | Data processing |
| NumPy | Numerical computations |
| Transformers | NLP support |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/intelligent-candidate-ranking.git

cd intelligent-candidate-ranking
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📤 Output

The system generates:

- Candidate ID
- Rank
- Score
- Reasoning

Example:

| Candidate ID | Rank | Score |
|-------------|------:|-------:|
| C1023 | 1 | 0.91 |

---

## 📈 Results

- Improved semantic matching.
- Reduced false positives.
- Better AI/ML candidate identification.
- Explainable recommendations.
- Behavioral intelligence.

---

## 🚀 Future Improvements

- Vector databases (FAISS, Pinecone)
- RAG-based retrieval
- Learning-to-Rank models
- LLM-based reasoning
- Recruiter feedback loops
- Real-time candidate recommendations

---

## 🎥 Demo Video

https://drive.google.com/file/d/1aBsbUzsCTRbZ6L9gIRCxG5uWEQ5FYp0w/view?usp=sharing

```text
uploaded demo video link
```

---

## 💻 GitHub Repository

```text
https://github.com/CheboluGayatri/IntelliHire_AI
```

---

## 🙏 Acknowledgements

- Redrob AI
- Sentence Transformers
- Hugging Face
- Scikit-learn
- Open Source Community

---

## 👩‍💻 Developed By

### Gayatri Chebolu

B.Tech – Artificial Intelligence

Passionate about:
- Artificial Intelligence
- Machine Learning
- NLP
- Generative AI
- Intelligent Systems

---

⭐ If you found this project useful, please give it a star.

# Redrob Hackathon 2026 Submission

**Intelligent Candidate Discovery & Ranking System**
