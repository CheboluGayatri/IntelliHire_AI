# 🚀 IntelliHire AI – Intelligent Candidate Discovery & Ranking System

> **🏆 Redrob × Hack2Skill INDIA.RUNS 2026**  
> **Track 01 – The Data & AI Challenge**

<p align="center">
  <img src="Project Architecture.png" alt="IntelliHire AI Architecture" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/AI-NLP-green">
  <img src="https://img.shields.io/badge/SentenceTransformers-Embeddings-orange">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow">
  <img src="https://img.shields.io/badge/Status-Hackathon-success">
</p>

---

# 📌 Project Overview

Recruitment platforms process thousands of candidate profiles for every job opening. Traditional Applicant Tracking Systems (ATS) rely primarily on keyword matching, which often fails to identify highly qualified candidates using different terminology.

**IntelliHire AI** is an AI-powered Candidate Discovery and Ranking System that understands the contextual meaning of job descriptions and candidate profiles. Instead of relying only on keywords, it combines semantic similarity, experience relevance, recruiter behavioral signals, and role-fit analysis to generate an accurate, explainable, and intelligent ranked shortlist.

The project was developed for the **Redrob × Hack2Skill INDIA.RUNS 2026 – Data & AI Challenge**.

---

# 🎯 Problem Statement

Traditional ATS systems suffer from several limitations:

- Keyword-based filtering misses qualified candidates.
- Different terminology leads to poor matching.
- Irrelevant profiles may receive higher rankings.
- Candidate recommendations lack transparency.
- Recruiters spend significant time manually reviewing resumes.

Our objective is to develop an intelligent AI recruiter capable of understanding candidate profiles semantically and recommending the most suitable candidates.

---

# 🎯 Objectives

- Improve candidate discovery accuracy.
- Understand job descriptions semantically.
- Reduce false-positive candidate matches.
- Evaluate multiple candidate signals.
- Generate explainable recommendations.
- Produce an intelligent ranked shortlist.
- Enable lightweight CPU-based execution.

---

# ✨ Key Features

- ✅ Semantic Candidate Matching
- ✅ AI-Powered Multi-Factor Ranking
- ✅ Experience Evaluation
- ✅ Role Fit Assessment
- ✅ Behavioral Signal Analysis
- ✅ Explainable AI Recommendations
- ✅ Fast CPU-Compatible Pipeline
- ✅ Modular Python Architecture

---

# 🏗️ System Architecture

The architecture consists of six major layers:

1. **Input Layer**
   - Job Description
   - Candidate Dataset

2. **Processing Pipeline**
   - Data Loading
   - Feature Engineering
   - Semantic Matching
   - Multi-Signal Scoring
   - Ranking Engine

3. **AI Models**
   - Sentence Transformer
   - Cosine Similarity
   - Weighted Scoring Algorithm

4. **Explainability Module**
   - Recommendation Reasoning
   - Score Breakdown

5. **Storage Layer**
   - Candidate Features
   - Embeddings
   - Ranking Results

6. **Output Layer**
   - Ranked Candidate List
   - Submission CSV

---

# 🔄 End-to-End Workflow

```text
Job Description
        │
        ▼
Load Candidate Profiles
        │
        ▼
Feature Engineering
        │
        ▼
Sentence Embeddings
        │
        ▼
Semantic Similarity
        │
        ▼
Experience Scoring
        │
        ▼
Behavioral Analysis
        │
        ▼
Role Fit Evaluation
        │
        ▼
Weighted Ranking Engine
        │
        ▼
Ranked Candidate Shortlist
        │
        ▼
Submission CSV
```

---

# 🧠 Candidate Signals Used

## Technical Signals

- AI / ML Skills
- Recommendation Systems
- Search & Retrieval
- Vector Databases
- NLP Experience

## Experience Signals

- Years of Experience
- Previous Projects
- Career History
- Industry Experience

## Behavioral Signals

- Recruiter Response Rate
- Open-to-Work Status
- Candidate Activity
- Interview Completion Rate

## Role Fit Signals

- Current Designation
- Previous Roles
- Domain Expertise

---

# 🤖 AI Models & Algorithms

| Component | Technique |
|-----------|-----------|
| Embedding Model | Sentence Transformer (all-MiniLM-L6-v2) |
| Similarity | Cosine Similarity |
| Ranking | Weighted Multi-Factor Scoring |
| Feature Engineering | Experience, Retrieval, Behavior, Role Fit |
| Explainability | Rule-Based Recommendation Generation |

---

# 📊 Ranking Methodology

The final ranking score is computed using:

```python
Final Score =
0.35 × Semantic Similarity
+ 0.25 × Retrieval Score
+ 0.20 × Role Fit Score
+ 0.10 × Behavioral Score
+ 0.10 × Experience Score
+ Title Penalty
```

### Why these weights?

- **Semantic Similarity (35%)** captures contextual relevance.
- **Retrieval Score (25%)** rewards expertise in search and recommendation systems.
- **Role Fit (20%)** measures alignment with the target position.
- **Behavior (10%)** identifies active and engaged candidates.
- **Experience (10%)** values relevant professional history.

---

# 📖 Explainable AI

Every ranked recommendation includes:

- Candidate Job Title
- Years of Experience
- Final Score
- Recruiter Response Rate
- Recommendation Reason

This improves transparency and helps recruiters understand why a candidate was selected.

---

# 📁 Project Structure

```text
IntelliHire_AI/
│
├── data/
│   ├── candidates.jsonl
│   ├── job_description.txt
│   └── sample_submission.csv
│
├── outputs/
│   └── submission.csv
│
├── src/
│   ├── load_data.py
│   ├── semantic_match.py
│   ├── feature_engineering.py
│   ├── ranking_engine.py
│   ├── generate_submission.py
│   └── main.py
│
├── Project Architecture.png
├── README.md
├── requirements.txt
└── presentation.pdf
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| Sentence Transformers | Semantic Embeddings |
| Transformers | NLP Models |
| Scikit-learn | Cosine Similarity |
| Pandas | Data Processing |
| NumPy | Numerical Computation |

---

# 📦 Installation

```bash
git clone https://github.com/CheboluGayatri/IntelliHire_AI.git

cd IntelliHire_AI

pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python src/main.py
```

---

# 📤 Output

The system generates a ranked CSV file containing:

| Candidate ID | Rank | Score | Reason |
|--------------|------|--------|--------|
| CAND_000004 | 1 | 0.7045 | AI Research Engineer; 6.3 yrs; response rate 0.79 |

Output:

```text
outputs/submission.csv
```

---

# 🚀 Future Enhancements

- FAISS Vector Search
- Pinecone Integration
- Retrieval-Augmented Generation (RAG)
- Learning-to-Rank Models
- LLM-Based Candidate Reasoning
- Recruiter Feedback Loop
- Real-Time Candidate Recommendation API

---

# 🎥 Demo Video

https://drive.google.com/file/d/1aBsbUzsCTRbZ6L9gIRCxG5uWEQ5FYp0w/view?usp=sharing

---

# 💻 GitHub Repository

https://github.com/CheboluGayatri/IntelliHire_AI

---

# 🙏 Acknowledgements

- Redrob
- Hack2Skill
- Hugging Face
- Sentence Transformers
- Scikit-learn
- Open Source Community

---

# 👩‍💻 Developed By

**Gayatri Chebolu**

**B.Tech – Artificial Intelligence**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- Generative AI
- Recommendation Systems
- Search & Retrieval

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 🏆 Hackathon Submission

**Project:** IntelliHire AI – Intelligent Candidate Discovery & Ranking System

**Track:** Data & AI Challenge

**Event:** Redrob × Hack2Skill INDIA.RUNS 2026

> Building the next generation of AI-powered recruitment through semantic understanding, intelligent ranking, and explainable recommendations.
