# 🚀 IntelliHire AI – Intelligent Candidate Discovery & Ranking System

> **🏆 Redrob × Hack2Skill INDIA.RUNS 2026**  
> **Track 01 – The Data & AI Challenge**

<p align="center">
  <img src="Project Architecture.png" alt="IntelliHire AI System Architecture" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/AI-NLP-green" />
  <img src="https://img.shields.io/badge/SentenceTransformers-all--MiniLM--L6--v2-orange" />
  <img src="https://img.shields.io/badge/Status-Hackathon%20Project-success" />
</p>

---

# 📌 Project Overview

Recruiters often receive thousands of applications for a single job opening. Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, which can overlook qualified candidates whose resumes use different terminology or phrasing.

**IntelliHire AI** is an AI-powered Candidate Discovery and Ranking System that understands both job descriptions and candidate profiles using semantic embeddings instead of simple keyword matching.

The system combines multiple ranking signals, including semantic similarity, professional experience, recruiter behavioral signals, retrieval expertise, and role-fit analysis to produce an accurate, transparent, and explainable ranking of candidates.

Developed as part of the **Redrob × Hack2Skill INDIA.RUNS 2026 – Data & AI Challenge**, IntelliHire AI demonstrates how AI can improve modern recruitment by delivering intelligent recommendations while maintaining recruiter trust through explainable scoring.

---

# 🎯 Problem Statement

Traditional ATS platforms suffer from several limitations:

- Dependence on exact keyword matching
- Poor understanding of contextual meaning
- Highly qualified candidates being overlooked
- Irrelevant profiles receiving higher rankings
- Limited transparency in ranking decisions

The goal of IntelliHire AI is to overcome these challenges by building an intelligent ranking system capable of understanding candidate relevance beyond keywords.

---

# 🎯 Objectives

- Improve candidate discovery accuracy
- Perform semantic understanding of job descriptions
- Reduce false-positive candidate matches
- Integrate multiple candidate evaluation signals
- Generate explainable recommendations
- Produce an intelligent ranked shortlist
- Enable fast CPU-compatible execution

---

# ✨ Key Features

- ✅ Semantic Candidate Matching
- ✅ Multi-Factor Ranking Engine
- ✅ Experience Evaluation
- ✅ Role Fit Assessment
- ✅ Behavioral Signal Analysis
- ✅ Explainable AI Recommendations
- ✅ Lightweight CPU-Compatible Model
- ✅ Fast Ranking Pipeline
- ✅ Modular Python Architecture

---

# 💡 Solution Overview

Instead of relying solely on keyword matching, IntelliHire AI evaluates candidates using multiple complementary signals.

The ranking engine combines:

- Semantic Similarity
- Experience Relevance
- Retrieval Expertise
- Role Fit
- Behavioral Intelligence
- Explainable AI

Each candidate receives a weighted score based on these factors, resulting in a more accurate and transparent ranking.

---

# 🏗️ System Architecture

The system follows a modular pipeline consisting of six stages:

1. **Input Layer**
   - Job Description
   - Candidate Dataset

2. **Processing Pipeline**
   - Data Loading
   - Feature Engineering
   - Semantic Matching
   - Multi-Signal Scoring

3. **Ranking Engine**
   - Weighted Score Aggregation
   - Candidate Ranking

4. **Explainability Module**
   - Recommendation Reason Generation
   - Score Interpretation

5. **Storage Layer**
   - Candidate Features
   - Embeddings
   - Results

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
Generate Sentence Embeddings
        │
        ▼
Semantic Similarity
        │
        ▼
Multi-Factor Feature Scoring
        │
        ▼
Weighted Ranking Engine
        │
        ▼
Explainable Recommendations
        │
        ▼
Submission CSV
```
---

# 🧠 Candidate Signals Used

To evaluate each candidate comprehensively, IntelliHire AI combines multiple signals rather than relying on a single metric.

## Technical Signals

- AI / Machine Learning Skills
- Natural Language Processing
- Recommendation Systems
- Search & Retrieval
- Vector Database Knowledge
- Software Engineering Skills

## Experience Signals

- Years of Professional Experience
- Previous Projects
- Career Progression
- Industry Exposure

## Behavioral Signals

- Recruiter Response Rate
- Open-to-Work Status
- Candidate Activity
- Interview Completion Rate

## Role Fit Signals

- Current Job Title
- Previous Roles
- Domain Expertise
- Skill Alignment

By combining these signals, the system produces a balanced and context-aware ranking.

---

# 🤖 AI Models & Algorithms

| Component | Technique Used |
|-----------|----------------|
| Embedding Model | Sentence Transformer (all-MiniLM-L6-v2) |
| Similarity Measure | Cosine Similarity |
| Ranking Algorithm | Weighted Multi-Factor Scoring |
| Feature Engineering | Rule-Based Feature Extraction |
| Explainability | Score-Based Recommendation Generation |

### Sentence Transformer

The system uses **all-MiniLM-L6-v2** to convert both job descriptions and candidate profiles into dense vector embeddings.

These embeddings capture contextual meaning rather than exact keyword matches.

### Cosine Similarity

Semantic similarity between the job description and candidate profile is calculated using cosine similarity.

Higher similarity indicates a better contextual match.

### Multi-Factor Ranking

Instead of relying only on semantic similarity, IntelliHire AI combines multiple evaluation signals into a single weighted ranking score.

---

# 📊 Ranking Methodology

Each candidate receives a final ranking score based on several independent evaluation metrics.

The scoring formula is:

```python
Final Score =
0.35 × Semantic Similarity
+ 0.25 × Retrieval Score
+ 0.20 × Role Fit Score
+ 0.10 × Behavioral Score
+ 0.10 × Experience Score
+ Title Penalty
```

### Scoring Components

| Component | Purpose |
|-----------|----------|
| Semantic Similarity | Measures contextual match between job description and candidate profile |
| Retrieval Score | Rewards expertise in search, retrieval, recommendation systems, and AI |
| Role Fit | Measures alignment between candidate role and target role |
| Behavioral Score | Uses recruiter interaction and activity signals |
| Experience Score | Rewards relevant professional experience |
| Title Penalty | Penalizes completely unrelated job titles |

Candidates are sorted in descending order of their final score to produce the final ranked shortlist.

---

# 📖 Explainable AI

One of the key goals of IntelliHire AI is transparency.

Instead of producing only a numerical score, the system also explains **why** a candidate was recommended.

Each ranked candidate includes:

- Current Job Title
- Years of Experience
- Recruiter Response Rate
- Final Ranking Score
- Recommendation Reason

### Example

```text
Candidate ID : CAND_000004

Rank : 1

Score : 0.7045

Reason :
AI Research Engineer
6.3 years of experience
Recruiter response rate 0.79
Strong semantic match with job description
```

This improves recruiter trust and helps users understand the reasoning behind every recommendation.

---

# 📈 Results

IntelliHire AI successfully demonstrates:

- Improved semantic candidate matching
- Reduced false-positive recommendations
- Better AI/ML candidate identification
- Transparent ranking decisions
- Fast CPU-compatible execution
- Modular and scalable architecture

Compared to traditional keyword-based filtering, the proposed system provides a more context-aware and explainable ranking process.
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
└── AI_Recruiter_Ranker.pdf
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
| JSON | Candidate Dataset |
| CSV | Submission Output |

---

# ⚙️ Requirements

- Python 3.10+
- sentence-transformers
- transformers
- scikit-learn
- pandas
- numpy

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/CheboluGayatri/IntelliHire_AI.git
```

Move into the project folder

```bash
cd IntelliHire_AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Execute:

```bash
python src/main.py
```

The pipeline automatically performs the following steps:

1. Load candidate profiles
2. Read the job description
3. Generate semantic embeddings
4. Compute semantic similarity
5. Engineer candidate features
6. Calculate weighted ranking scores
7. Rank all candidates
8. Generate the submission CSV

---

# 📤 Output

After execution, the system generates:

```text
outputs/
└── submission.csv
```

The output contains:

| Candidate ID | Rank | Score | Recommendation |
|--------------|------|--------|----------------|
| CAND_000004 | 1 | 0.7045 | AI Research Engineer; 6.3 yrs; response rate 0.79 |

Each recommendation includes an explainable reason that summarizes the candidate's strongest matching attributes.

---
# 🚀 Future Enhancements

The current implementation demonstrates a lightweight and explainable ranking pipeline. Future improvements include:

- 🔹 FAISS Vector Search for scalable semantic retrieval
- 🔹 Pinecone integration for cloud vector storage
- 🔹 Retrieval-Augmented Generation (RAG)
- 🔹 Learning-to-Rank algorithms (LambdaMART, XGBoost Ranker)
- 🔹 LLM-based candidate reasoning
- 🔹 Recruiter feedback loop for continuous learning
- 🔹 Real-time recommendation API
- 🔹 Interactive recruiter dashboard

---

# 📈 Project Highlights

✅ Semantic candidate matching

✅ Multi-factor ranking engine

✅ Explainable AI recommendations

✅ Lightweight CPU-compatible implementation

✅ Modular Python architecture

✅ Fast candidate ranking pipeline

✅ Easy to extend and deploy

---

# 🎥 Demo Video

Watch the complete project demonstration here:

**Demo Video**

https://drive.google.com/file/d/1aBsbUzsCTRbZ6L9gIRCxG5uWEQ5FYp0w/view?usp=sharing

---

# 💻 GitHub Repository

GitHub Repository:

https://github.com/CheboluGayatri/IntelliHire_AI

---

# 🙏 Acknowledgements

Special thanks to:

- Redrob
- Hack2Skill
- Hugging Face
- Sentence Transformers
- Scikit-learn
- NumPy
- Pandas
- Open Source Community

for providing the tools and resources that made this project possible.

---

# 👩‍💻 Developed By

## Gayatri Chebolu

**Bachelor of Technology (B.Tech)**

**Artificial Intelligence**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- Large Language Models (LLMs)
- Generative AI
- Recommendation Systems
- Search & Retrieval

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates future improvements and helps others discover the project.

---

# 🏆 Hackathon Submission

**Event:** Redrob × Hack2Skill INDIA.RUNS 2026

**Track:** The Data & AI Challenge

**Project:** IntelliHire AI – Intelligent Candidate Discovery & Ranking System

> Building the next generation of AI-powered recruitment through semantic understanding, intelligent ranking, and explainable recommendations.
