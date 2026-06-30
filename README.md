# 🚀 IntelliHire AI – Intelligent Candidate Discovery & Ranking System

> ### 🏆 Redrob × Hack2Skill INDIA.RUNS 2026
> ### 📍 Track 01 – The Data & AI Challenge

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge)
![Sentence Transformers](https://img.shields.io/badge/Sentence--Transformers-NLP-green?style=for-the-badge)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Hackathon-success?style=for-the-badge)

</p>

---

# 👥 Team Information

| Item | Details |
|------|---------|
| **Team Name** | IntelliHire AI |
| **Hackathon** | Redrob × Hack2Skill INDIA.RUNS 2026 |
| **Track** | Track 01 – The Data & AI Challenge |
| **Developer** | Gayatri Chebolu |

---

# 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Why IntelliHire AI?](#-why-intellihire-ai)
- [Key Features](#-key-features)
- [Solution Overview](#-solution-overview)
- [Design Decisions](#️-design-decisions)
- [System Architecture](#️-system-architecture)
- [End-to-End Workflow](#-end-to-end-workflow)
- [Candidate Signals Used](#-candidate-signals-used)
- [AI Models & Algorithms](#-ai-models--algorithms)
- [Ranking Methodology](#-ranking-methodology)
- [Explainable AI](#-explainable-ai)
- [Results](#-results)
- [Runtime & Scalability](#-runtime--scalability)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Run the Project](#️-run-the-project)
- [Output](#-output)
- [Demo Video](#-demo-video)
- [GitHub Repository](#-github-repository)
- [Acknowledgements](#-acknowledgements)
- [Developer](#-developed-by)

---

# 📌 Project Overview

Recruitment platforms generate thousands of candidate profiles for every open position. Traditional Applicant Tracking Systems (ATS) primarily depend on exact keyword matching, often overlooking highly qualified candidates whose resumes use different terminology or describe similar skills differently.

**IntelliHire AI** is an AI-powered Candidate Discovery and Ranking System designed to overcome these limitations using semantic understanding and intelligent ranking.

Instead of relying solely on keyword matching, the system understands the contextual meaning of both job descriptions and candidate profiles. It combines multiple candidate signals, including semantic similarity, professional experience, recruiter behavioral signals, and role relevance, to identify the most suitable candidates.

The result is an intelligent, explainable, and highly accurate candidate ranking pipeline that assists recruiters in making better hiring decisions while reducing manual screening effort.

---

# 🎯 Problem Statement

Traditional Applicant Tracking Systems (ATS) primarily rely on exact keyword matching.

Although simple and fast, this approach suffers from several limitations:

- Highly relevant candidates may be missed because they use different terminology.
- Profiles with repeated keywords may receive higher rankings despite being less suitable.
- Candidate-job matching lacks contextual understanding.
- Recruiters receive little transparency regarding ranking decisions.
- Valuable behavioral and engagement signals are ignored.

The objective of this project is to build an intelligent AI recruiter capable of understanding candidate profiles semantically and recommending the most suitable candidates using explainable AI techniques.

---

# 🎯 Objectives

The primary objectives of IntelliHire AI are:

- Improve candidate discovery accuracy.
- Understand job descriptions semantically.
- Reduce false-positive candidate matches.
- Evaluate candidates using multiple ranking signals.
- Incorporate recruiter behavioral intelligence.
- Generate transparent and explainable recommendations.
- Produce an accurate ranked shortlist for recruiters.
- Support lightweight CPU-based execution suitable for real-world deployment.

---

# 🌟 Why IntelliHire AI?

Unlike traditional ATS systems that rely on exact keyword matching, IntelliHire AI understands the context and meaning behind candidate profiles.

### Traditional ATS

- Keyword-based filtering
- Static rule-based ranking
- Ignores recruiter behavior
- Limited contextual understanding
- No explainability
- High false-positive rate

### IntelliHire AI

- Semantic candidate matching
- AI-driven multi-factor ranking
- Behavioral intelligence
- Role-fit analysis
- Explainable recommendations
- Reduced false positives
- Context-aware candidate discovery

By combining semantic understanding with recruiter intelligence, IntelliHire AI delivers more reliable candidate recommendations while improving recruiter trust.

---

# ✨ Key Features

- ✅ Semantic Candidate Matching using Sentence Transformers
- ✅ Context-aware Job Description Understanding
- ✅ Multi-Factor Candidate Ranking Engine
- ✅ Experience-Based Evaluation
- ✅ Recruiter Behavioral Signal Analysis
- ✅ Role Fit Assessment
- ✅ Explainable Candidate Recommendations
- ✅ Lightweight CPU-Compatible Architecture
- ✅ Fast Candidate Ranking Pipeline
- ✅ Transparent Scoring Mechanism
- ✅ Easily Scalable Architecture
- ✅ Modular Python Implementation

---

# 💡 Solution Overview

IntelliHire AI combines Natural Language Processing (NLP), semantic search, and multi-factor ranking techniques to identify the most suitable candidates for a given job description. Instead of relying solely on keyword matching, the system evaluates candidates using multiple signals such as semantic similarity, professional experience, role relevance, recruiter engagement, and behavioral intelligence.

The ranking engine assigns a weighted score to each candidate, ensuring that recommendations are accurate, explainable, and aligned with the hiring requirements.

### The ranking system considers:

- 🧠 Semantic Similarity
- 💼 Experience Relevance
- 🎯 Role Fit
- 🔍 Retrieval Expertise
- 📊 Behavioral Signals
- 📖 Explainable AI

The final output is a transparent and intelligently ranked shortlist of candidates.

---

# ⚙️ Design Decisions

The system was designed with three primary goals:

- **High Accuracy:** Capture contextual relevance instead of exact keyword matches.
- **Explainability:** Provide recruiters with transparent reasons behind every recommendation.
- **Efficiency:** Ensure fast CPU-based execution without requiring expensive GPU resources.

Instead of using a large language model for every ranking request, IntelliHire AI uses a lightweight Sentence Transformer for semantic understanding combined with a weighted multi-factor ranking engine. This design provides an excellent balance between performance, scalability, interpretability, and computational efficiency.

---

# 🏗️ System Architecture

```text
                       Job Description
                              │
                              ▼
             Sentence Transformer Embeddings
                              │
                              ▼
                   Candidate Profile Embeddings
                              │
                              ▼
                    Semantic Similarity Engine
                              │
                              ▼
                    Feature Engineering Layer
        ┌────────────┬─────────────┬────────────┬────────────┐
        ▼            ▼             ▼            ▼
 Experience      Role Fit      Behavioral     Retrieval
   Score          Score          Score          Score
        └────────────┴─────────────┴────────────┘
                              │
                              ▼
                  Weighted Multi-Factor Ranking
                              │
                              ▼
                  Explainable Candidate Ranking
                              │
                              ▼
                  Ranked Candidate Shortlist
```

---

# 🔄 End-to-End Workflow

The entire candidate ranking pipeline consists of the following stages:

```text
Job Description
        │
        ▼
Load Candidate Profiles
        │
        ▼
Generate Sentence Embeddings
        │
        ▼
Compute Semantic Similarity
        │
        ▼
Feature Engineering
        │
        ▼
Experience Evaluation
        │
        ▼
Role Fit Analysis
        │
        ▼
Behavioral Signal Analysis
        │
        ▼
Weighted Ranking Engine
        │
        ▼
Generate Explainable Scores
        │
        ▼
Submission CSV
```

---

# 🧠 Candidate Signals Used

Our ranking engine combines multiple candidate attributes instead of relying on a single matching score.

## 🔹 Technical Signals

These signals evaluate the candidate's technical expertise.

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Natural Language Processing
- Search & Retrieval Systems
- Recommendation Systems
- Ranking Algorithms
- Vector Databases
- Hybrid Search
- Python Programming

---

## 🔹 Experience Signals

Professional experience plays an important role in determining candidate suitability.

The system evaluates:

- Total Years of Experience
- Relevant Industry Experience
- Previous AI/ML Projects
- Career Progression
- Technical Responsibilities
- Domain Expertise

---

## 🔹 Role Fit Signals

Role Fit measures how closely a candidate's professional background aligns with the target position.

Examples include:

- Current Job Title
- Previous Roles
- AI/ML Experience
- Product Engineering Background
- Retrieval System Experience
- Recommendation Engine Development

---

## 🔹 Behavioral Signals

Behavioral intelligence improves ranking quality by identifying active and engaged candidates.

Signals include:

- Recruiter Response Rate
- Open-to-Work Status
- Interview Completion Rate
- Candidate Activity
- Profile Completeness
- Recruiter Saves

---

# 🤖 AI Models & Algorithms

## Embedding Model

**Sentence Transformer (all-MiniLM-L6-v2)**

The embedding model converts both the job description and candidate profiles into dense vector representations that capture contextual meaning rather than exact keywords.

### Why MiniLM?

- Lightweight transformer model
- Fast CPU inference
- High semantic accuracy
- Low memory consumption
- Suitable for large-scale candidate ranking

---

## Semantic Matching

Semantic similarity between the Job Description and Candidate Profile is computed using:

- Cosine Similarity
- Sentence Embeddings

This enables the system to identify candidates with relevant skills even when different terminology is used.

---

## Ranking Algorithm

The ranking engine combines multiple candidate signals into a unified score using a weighted multi-factor scoring mechanism.

Candidate ranking considers:

- Semantic Similarity
- Retrieval Expertise
- Role Fit
- Behavioral Intelligence
- Experience Relevance

---

## Feature Engineering

Several engineered features improve ranking quality.

| Feature | Purpose |
|---------|---------|
| Semantic Score | Measures contextual relevance |
| Experience Score | Rewards relevant experience |
| Retrieval Score | Evaluates search and ranking expertise |
| Role Fit Score | Measures job alignment |
| Behavioral Score | Measures recruiter engagement |
| Title Penalty | Penalizes unrelated job titles |

These features collectively produce a more reliable ranking than traditional keyword-based Applicant Tracking Systems.

# 📊 Ranking Methodology

The final candidate ranking is generated using a **Weighted Multi-Factor Scoring Algorithm** that combines semantic understanding with domain-specific heuristics. Rather than relying on a single similarity score, IntelliHire AI evaluates each candidate across multiple dimensions to produce a balanced and explainable ranking.

The ranking engine considers:

- Semantic relevance between the Job Description and Candidate Profile
- Retrieval and Search expertise
- Role alignment
- Professional experience
- Recruiter behavioral signals
- Job title relevance

Each feature contributes to the final score according to its importance in determining candidate suitability.

---

## 🧮 Final Ranking Formula

```python
Final Score =
0.35 × Semantic Similarity
+ 0.25 × Retrieval Score
+ 0.20 × Role Fit Score
+ 0.10 × Behavioral Score
+ 0.10 × Experience Score
+ Title Penalty
```

Candidates are ranked in descending order based on the final score.

---

## ⚖️ Why These Weights?

The ranking weights were carefully selected to balance semantic understanding with practical recruitment considerations.

| Component | Weight | Reason |
|------------|--------|--------|
| Semantic Similarity | **35%** | Primary indicator of contextual relevance between the job description and candidate profile. |
| Retrieval Score | **25%** | Measures expertise in search, recommendation systems, vector databases, and retrieval techniques required for the target role. |
| Role Fit Score | **20%** | Evaluates alignment between previous roles and the desired AI/ML position. |
| Behavioral Score | **10%** | Rewards candidates who actively engage with recruiters and maintain updated profiles. |
| Experience Score | **10%** | Reflects relevant professional experience and industry exposure. |
| Title Penalty | Variable | Reduces scores for candidates whose current role is unrelated to the target position. |

These weights are currently **heuristic-based**, allowing transparent decision-making. Future versions can automatically learn optimal weights using recruiter feedback and Learning-to-Rank algorithms.

---

# 📖 Explainable AI

One of the major limitations of traditional ATS platforms is the lack of transparency in candidate recommendations. Recruiters often receive a ranked list without understanding *why* a candidate was selected.

IntelliHire AI addresses this challenge by generating **explainable recommendations** for every ranked candidate.

Each recommendation includes:

- 👤 Current Job Title
- 💼 Years of Experience
- 🛠 Relevant Skills
- 📊 Recruiter Response Rate
- 🎯 Role Alignment
- 📈 Overall Ranking Score
- 💡 Reason for Recommendation

### Example

| Candidate | Explanation |
|------------|-------------|
| Senior Machine Learning Engineer | 7.5 years of AI/ML experience, strong retrieval expertise, excellent recruiter response rate, and high semantic similarity with the job description. |

This improves recruiter trust and makes hiring decisions more transparent.

---

## 🛡 Preventing Hallucinations

Unlike generative AI systems that may produce unsupported information, IntelliHire AI only generates explanations using **verified candidate attributes**.

Validation includes:

- Candidate profile information
- Professional experience
- Career history
- Skills
- Recruiter engagement metrics
- Role-related metadata

No external assumptions or fabricated information are introduced into the recommendation process.

---

# 📈 Results

The proposed ranking engine demonstrates significant improvements over traditional keyword-based Applicant Tracking Systems.

### Key Improvements

- ✅ Improved semantic candidate matching
- ✅ Reduced false-positive recommendations
- ✅ Better identification of AI/ML professionals
- ✅ Transparent and explainable ranking decisions
- ✅ Intelligent behavioral analysis
- ✅ Fast CPU-based execution
- ✅ Lightweight deployment
- ✅ Scalable architecture

---

## 📊 Comparison with Traditional ATS

| Traditional ATS | IntelliHire AI |
|-----------------|----------------|
| Exact keyword matching | Semantic understanding |
| Static filters | Multi-factor AI ranking |
| Rule-based scoring | Context-aware scoring |
| Ignores recruiter signals | Behavioral intelligence |
| No explainability | Explainable recommendations |
| High false positives | Improved candidate relevance |

---

# ⚡ Runtime & Scalability

IntelliHire AI is designed to provide high-quality candidate ranking while maintaining low computational cost.

### Performance Characteristics

- ⚡ Lightweight Sentence Transformer model
- 💻 CPU-compatible execution
- 🚀 Fast cosine similarity computation
- 🧠 Low memory consumption
- 📈 Easily scalable for large candidate datasets
- 🔍 Suitable for vector database integration

The modular architecture also enables future deployment with distributed retrieval systems such as **FAISS**, **Pinecone**, or other vector search platforms without major architectural changes.

---

# ⚠️ Limitations

Although IntelliHire AI significantly improves candidate discovery, there are several opportunities for future improvement.

Current limitations include:

- Ranking weights are manually designed rather than learned from recruiter feedback.
- Performance depends on the completeness and quality of candidate profiles.
- The current implementation does not use Large Language Models (LLMs) for advanced reasoning.
- Candidate ranking is heuristic-based rather than trained using Learning-to-Rank algorithms.
- Evaluation has not yet been conducted on a large-scale real-world recruitment benchmark.

Despite these limitations, the current approach provides an effective balance between **accuracy**, **explainability**, **speed**, and **computational efficiency**, making it well-suited for a hackathon proof of concept.

# 🚀 Future Enhancements

The current version of IntelliHire AI provides an efficient and explainable candidate ranking pipeline. However, several enhancements can further improve ranking quality, scalability, and recruiter experience.

## Planned Enhancements

### 🔍 FAISS / Pinecone Vector Database

Replace linear similarity search with vector databases for scalable semantic retrieval across millions of candidate profiles.

**Benefits**

- Faster candidate retrieval
- Low-latency semantic search
- Better scalability
- Production-ready deployment

---

### 🤖 Retrieval-Augmented Generation (RAG)

Integrate Retrieval-Augmented Generation to produce richer candidate explanations using retrieved profile information.

**Benefits**

- Better recruiter insights
- Improved explainability
- More contextual recommendations

---

### 📈 Learning-to-Rank Models

Replace manually designed ranking weights with machine learning ranking algorithms.

Possible models include:

- LambdaMART
- XGBoost Ranking
- RankNet
- LightGBM Ranker

These models can learn optimal ranking strategies directly from recruiter feedback.

---

### 🧠 LLM-Based Candidate Reasoning

Incorporate Large Language Models to perform deeper reasoning about candidate suitability.

Potential applications:

- Resume summarization
- Skill gap analysis
- Interview question generation
- Candidate justification
- Career progression analysis

---

### 🔄 Recruiter Feedback Loop

Enable continuous improvement by learning from recruiter actions.

Examples include:

- Candidate shortlisted
- Candidate rejected
- Candidate hired
- Interview performance

The ranking model can automatically adapt over time based on recruiter preferences.

---

### ⚡ Real-Time Candidate Recommendations

Deploy IntelliHire AI as an online recommendation system capable of ranking candidates instantly as new profiles become available.

---

# 📁 Project Structure

```text
IntelliHire_AI/

│
├── data/
│   ├── candidates.jsonl
│   └── job_description.txt
│
├── outputs/
│   └── submission.csv
│
├── load_data.py
├── semantic_match.py
├── feature_engineering.py
├── ranking_engine.py
├── generate_submission.py
├── main.py
│
├── requirements.txt
├── README.md
└── presentation.pdf
```

---

# 🛠 Technologies Used

| Technology | Purpose | Why Selected |
|------------|----------|--------------|
| Python | Core Development | Easy to build scalable AI applications |
| Sentence Transformers | Semantic Embeddings | High-quality sentence representations |
| all-MiniLM-L6-v2 | Embedding Model | Lightweight, CPU-friendly, fast inference |
| Transformers | NLP Support | Modern transformer architecture |
| Scikit-learn | Cosine Similarity | Efficient similarity computation |
| Pandas | Data Processing | Fast manipulation of structured data |
| NumPy | Numerical Computing | High-performance mathematical operations |
| JSON | Candidate Dataset | Lightweight structured storage |
| CSV | Submission Output | Standard hackathon submission format |

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/CheboluGayatri/IntelliHire_AI.git
```

Navigate to the project folder

```bash
cd IntelliHire_AI
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Execute the following command:

```bash
python main.py
```

The pipeline automatically performs the following steps:

1. Load the Job Description
2. Load Candidate Profiles
3. Generate Sentence Embeddings
4. Compute Semantic Similarity
5. Perform Feature Engineering
6. Calculate Weighted Scores
7. Rank Candidates
8. Generate the Submission CSV

---

# 📤 Output

The system generates a ranked CSV file containing:

| Column | Description |
|----------|-------------|
| Candidate ID | Unique candidate identifier |
| Rank | Candidate ranking position |
| Final Score | Overall ranking score |
| Recommendation Reason | Explainable justification |

### Example Output

| Candidate ID | Rank | Final Score |
|--------------|------|------------|
| C1023 | 1 | 0.91 |
| C1041 | 2 | 0.88 |
| C1098 | 3 | 0.86 |

Output Location

```text
outputs/
└── submission.csv
```

---

# 📊 Why IntelliHire AI?

Unlike traditional Applicant Tracking Systems, IntelliHire AI combines semantic understanding with multiple ranking signals to provide more accurate and explainable recommendations.

### Key Advantages

- ✅ Context-aware semantic matching
- ✅ Multi-factor ranking engine
- ✅ Explainable AI recommendations
- ✅ Behavioral intelligence
- ✅ Experience-aware ranking
- ✅ Lightweight CPU execution
- ✅ Modular architecture
- ✅ Easy scalability
- ✅ Transparent scoring mechanism

---

# 🎥 Demo Video

Watch the complete project demonstration here:

**Demo Video**

https://drive.google.com/file/d/1aBsbUzsCTRbZ6L9gIRCxG5uWEQ5FYp0w/view?usp=sharing

---

# 💻 GitHub Repository

Source code is available at:

https://github.com/CheboluGayatri/IntelliHire_AI

---

# 🙏 Acknowledgements

We sincerely thank:

- Redrob
- Hack2Skill
- Hugging Face
- Sentence Transformers
- Scikit-learn
- NumPy
- Pandas
- Open Source Community

for providing the tools, libraries, and platform that made this project possible.

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
- Intelligent Recommendation Systems
- Search & Retrieval Systems

---

# ⭐ Support the Project

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates future improvements and helps others discover the project.

---

## 🏆 Hackathon Submission

**Redrob × Hack2Skill INDIA.RUNS 2026**

**Track 01 – The Data & AI Challenge**

**Project Title:** IntelliHire AI – Intelligent Candidate Discovery & Ranking System

> Building the next generation of AI-powered recruitment through semantic understanding, intelligent ranking, and explainable recommendations.

