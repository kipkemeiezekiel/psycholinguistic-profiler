import streamlit as st
import pandas as pd
import re
from collections import Counter
from scraper import WebScraper  # Imports your upgraded autonomous web parser

class AdvancedProfiler:
    def __init__(self, excel_path=None):
        # Default fallback matrix mapping core tracking traits
        self.lexicon_matrix = {
            "Ego & Hubris": {
                "keywords": ["i", "me", "my", "myself", "always", "never", "obviously", "clearly", "superior"],
                "ocean_vector": {"Openness": 0.1, "Conscientiousness": 0.0, "Extraversion": 0.4, "Agreeableness": -0.6, "Neuroticism": -0.3}
            },
            "Docility & Passivity": {
                "keywords": ["whatever", "sorry", "apologize", "agree", "depend", "submissive", "yield"],
                "ocean_vector": {"Openness": -0.2, "Conscientiousness": 0.1, "Extraversion": -0.4, "Agreeableness": 0.7, "Neuroticism": 0.4}
            },
            "Existential Detachment": {
                "keywords": ["nothing", "perish", "grave", "void", "meaningless", "empty", "futile", "escapism"],
                "ocean_vector": {"Openness": 0.5, "Conscientiousness": -0.3, "Extraversion": -0.6, "Agreeableness": 0.0, "Neuroticism": 0.5}
            }
        }
        if excel_path:
            self.load_lexicon_from_excel(excel_path)

    def load_lexicon_from_excel(self, file_path):
        """Custom spreadsheet file parser mapping uploaded lexicon structures using pandas."""
        try:
            df = pd.read_excel(file_path)
            required_fields = ['Trait', 'Keywords', 'O', 'C', 'E', 'A', 'N']
            missing_fields = [field for field in required_fields if field not in df.columns]
            
            if missing_fields:
                st.sidebar.error(f"Spreadsheet error. Missing fields: {missing_fields}")
                return
                
            new_matrix = {}
            for _, row in df.iterrows():
                if pd.isna(row['Trait']) or pd.isna(row['Keywords']):
                    continue
                trait_name = str(row['Trait']).strip()
                keywords_list = [word.strip().lower() for word in str(row['Keywords']).split(',') if word.strip()]
                
                new_matrix[trait_name] = {
                    "keywords": keywords_list,
                    "ocean_vector": {
                        "Openness": float(row.get('O', 0)),
                        "Conscientiousness": float(row.get('C', 0)),
                        "Extraversion": float(row.get('E', 0)),
                        "Agreeableness": float(row.get('A', 0)),
                        "Neuroticism": float(row.get('N', 0))
                    }
                }
            self.lexicon_matrix = new_matrix
            st.sidebar.success("📊 Custom lexicon parsed successfully!")
        except Exception as e:
            st.sidebar.error(f"Spreadsheet parser error: {str(e)}")

    def analyze_profile(self, text_sample):
        cleaned_text = text_sample.lower()
        tokens = re.findall(r'\b[a-z_]+\b', cleaned_text)
        total_tokens = len(tokens)
        
        if total_tokens == 0:
            return None
            
        token_counts = Counter(tokens)
        trait_densities = {}
        ocean_scores = {"Openness": 50.0, "Conscientiousness": 50.0, "Extraversion": 50.0, "Agreeableness": 50.0, "Neuroticism": 50.0}
        
        for trait, data in self.lexicon_matrix.items():
            matches = sum(token_counts[word] for word in data["keywords"])
            density = (matches / total_tokens) * 100
            trait_densities[trait] = round(density, 2)
            
            for dim, weight in data["ocean_vector"].items():
                ocean_scores[dim] += (density * weight * 10)
                
        for dim in ocean_scores:
            ocean_scores[dim] = max(0.0, min(100.0, round(ocean_scores[dim], 2)))
            
        return total_tokens, trait_densities, ocean_scores

# --- Streamlit Dashboard Interface UI ---
st.set_page_config(page_title="Psycholinguistic Profiler", layout="wide")
st.title("🧠 Computational Psycholinguistic Profiling Dashboard")

st.sidebar.header("📁 Database Configuration")
uploaded_file = st.sidebar.file_uploader(
    "Upload Master Lexicon Excel File", 
    type=["xlsx"], 
    key="unique_master_lexicon_uploader_v1"
)

profiler = AdvancedProfiler(uploaded_file if uploaded_file else None)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌐 Data Ingestion Channel")
    
    # Introduce an interactive selection tab for input flexibility
    input_mode = st.radio("Select Text Source Mode:", ["Manual Entry Portfolio", "Live Web URL Scraper"])
    final_text_corpus = ""
    
    if input_mode == "Manual Entry Portfolio":
        final_text_corpus = st.text_area("Paste text sample or narrative statements here:", height=300)
    else:
        target_url = st.text_input("Enter public article or webpage URL:", placeholder="https://wikipedia.org")
        if target_url:
            with st.spinner("Extracting and sanitizing remote text elements..."):
                scraped_result = WebScraper.extract_article_text(target_url)
                
                # Check if the scraper returned an error message string
                if scraped_result.startswith("Error") or scraped_result.startswith("Unhandled") or scraped_result.startswith("Network"):
                    st.error(scraped_result)
                else:
                    st.success(f"Successfully harvested {len(scraped_result)} characters from target URL!")
                    final_text_corpus = st.text_area("Extracted Web Content Preview (Editable):", value=scraped_result, height=250)

    run_analysis = st.button("Execute Computational Profiling", type="primary")

with col2:
    st.subheader("📊 Algorithmic Output")
    if run_analysis and final_text_corpus:
        results = profiler.analyze_profile(final_text_corpus)
        if results:
            total_tokens, densities, ocean = results
            st.metric("Total Tokens Processed", total_tokens)
            
            st.write("**Lexical Trait Densities:**")
            for trait, score in densities.items():
                st.progress(min(score / 100.0, 1.0))
                st.caption(f"{trait}: {score}%")
                
            st.write("**Estimated OCEAN Personality Spectrum Metrics:**")
            ocean_df = pd.DataFrame(list(ocean.items()), columns=["Dimension", "Score out of 100"])
            st.data_editor(ocean_df, use_container_width=True, disabled=True)
        else:
            st.error("No valid linguistic tokens found in processed text field.")