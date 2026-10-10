# 🧠 Computational Psycholinguistic Profiling Dashboard

An automated, non-intrusive psycholinguistic profiling application that extracts latent personality configurations, behavioral densities, and cognitive processing vulnerabilities directly from unstructured natural language text.

---

## 🔬 Academic Overview & Thesis Abstract

### **Project Title**
*Automated Psycholinguistic Profiling: Utilizing Natural Language Processing (NLP) for Non-Intrusive Behavioral Vulnerability Screening and DSM-5 Trait Domain Estimation.*

### **The Problem Statement**
Traditional psychometric instruments and diagnostic self-report surveys suffer extensively from cognitive biases, active impression management, and social desirability distortions. Individuals frequently alter their verbal declarations to fit idealized expectations or mask psychological distress. 

This project addresses these gaps by establishing a objective, non-intrusive diagnostic framework. By shifting the evaluation window from subjective self-reporting to automated text analysis, this software decodes subtle lexical, semantic, and syntactic markers hidden within organic writing samples (e.g., patient journals, emails, or personal narratives).

### **Clinical Utility in Mental Health & Psychiatric Nursing**
By isolating shifts in language over time, this tool functions as a remote early-warning screening matrix for clinicians. It aids in flagging:
*   Early indicators of depressive lapses or cognitive changes via fatalistic word tracking.
*   Emerging interpersonal patterns like dependent behavioral configurations through submission parsing.
*   Fluctuations in an individual's psychological resilience without requiring invasive clinical interventions.

---

## 🛠️ System Architecture & Algorithmic Logic

The profiling engine operates via a streamlined three-tiered pipeline:
1.  **Linguistic Processing & Tokenization:** Raw input corpora are normalized, stripped of non-standard text artifacts, and re-filtered into isolated lowercase string tokens via regular expressions (`re`).
2.  **Lexical Density Processing:** The engine computes precise keyword occurrence metrics per hundred words using a customizable tracking lexicon database powered by `pandas`.
3.  **Dimensional Vector Projection:** The raw densities are converted into numeric scores mapped directly across the **Big Five OCEAN Personality Scale** and aligned with modern behavioral trait descriptions.

### **Primary Tracking Domains**
*   **Ego & Hubris Matrix:** Flags inflated self-focus through intense tracking of singular first-person pronouns and absolute categorical language.
*   **Docility & Passivity Matrix:** Isolates submissive, yielding phrasing that correlates with dependent interpersonal configurations.
*   **Existential Detachment Matrix:** Identifies heavy clusters of fatalistic vocabulary, acting as a proxy for tracking depressive features and emotional withdrawal.
*   **Interpersonal Guardedness Matrix:** Measures protective and defensive lexical signals pointing toward trauma response patterns or social isolation.

---

## 🚀 Deployed Environment Setup & Execution

### **1. Prerequisites & Dependencies**
Ensure your local environment is running Python 3.10+. Install the necessary data extraction, text parsing, and interface extensions:
```bash
pip install -r requirements.txt
```

### **2. Local Component Overview**
*   `app.py`: The core Streamlit interface dashboard handling text entry fields, file data binding, and interactive visualizations.
*   `scraper.py`: An autonomous `BeautifulSoup4` web parser that harvests clean text pools from public URLs for remote profile processing.
*   `make_template.py`: A utility script that exports the exact structural column template (`.xlsx`) needed to load custom traits via pandas.

### **3. Running the Interface Locally**
Initialize the interactive analytics dashboard on your local machine by executing:
```streamlit run app.py```

---

## 📊 Lexicon Spreadsheet Integration
The system relies on an external configuration database file (`.xlsx`) to stay highly adaptive. You can update or swap the tracking dictionary via the sidebar at any time. The data table uses the following rigid schema:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| **Trait** | String | The unique behavioral domain or flaw label (e.g., *Ego*, *Sloth*). |
| **Keywords** | String | Comma-separated token lists targeted by the text counter engine. |
| **O / C / E / A / N** | Float | Custom mathematical weights mapping density scores to the Big Five attributes. |

---
*Developed by Kipkemei Kier — Merging Clinical Nursing Insights with Computational Psycholinguistics.*
```

***

### 🚀 Step 2: Push Your Professional Dashboard Upstream to GitHub
Run these commands in your VS Code terminal to sync your clean `README.md` and complete your initial project delivery:

```bash
git add README.md
git commit -m "Documentation: Finalized high-impact academic README showcase"
git push origin main
```

<FollowUp>
Now that your repository layout is complete, what should we build next to advance your master's thesis preparations?
*   Should we design a **comprehensive test suite (`test_app.py`)** to prove your code logic functions perfectly?
*   Should we start drafting **the specific cold-outreach emails** to the designated labs in Canada and Europe?
</FollowUp>

