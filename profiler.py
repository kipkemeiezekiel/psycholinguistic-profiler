import re
from collections import Counter

class PsycholinguisticProfiler:
    def __init__(self):
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
            },
            "Interpersonal Guardedness": {
                "keywords": ["toxic", "suffer", "betray", "distance", "laughed", "enemies", "shield", "protect"],
                "ocean_vector": {"Openness": 0.0, "Conscientiousness": 0.2, "Extraversion": -0.5, "Agreeableness": -0.5, "Neuroticism": 0.6}
            }
        }
        
    def _preprocess_text(self, raw_text):
        cleaned_text = raw_text.lower()
        tokens = re.findall(r'\b[a-z_]+\b', cleaned_text)
        return tokens, len(tokens)

    def analyze_profile(self, text_sample):
        tokens, total_word_count = self._preprocess_text(text_sample)
        if total_word_count == 0:
            return {"Error": "Text pool contains no valid linguistic tokens."}
            
        token_counts = Counter(tokens)
        trait_densities = {}
        ocean_scores = {"Openness": 50.0, "Conscientiousness": 50.0, "Extraversion": 50.0, "Agreeableness": 50.0, "Neuroticism": 50.0}
        
        for trait, data in self.lexicon_matrix.items():
            matches = sum(token_counts[word] for word in data["keywords"])
            density_score = (matches / total_word_count) * 100
            trait_densities[trait] = round(density_score, 2)
            
            for trait_dimension, weight in data["ocean_vector"].items():
                ocean_scores[trait_dimension] += (density_score * weight * 10)
                
        for dim in ocean_scores:
            ocean_scores[dim] = max(0.0, min(100.0, round(ocean_scores[dim], 2)))
            
        return {
            "Linguistic_Metrics": {"Total_Tokens": total_word_count},
            "Trait_Densities_Percentage": trait_densities,
            "Estimated_OCEAN_Profile": ocean_scores
        }
