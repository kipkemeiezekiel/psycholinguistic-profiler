import unittest
from profiler import PsycholinguisticProfiler

class TestPsycholinguisticProfiler(unittest.TestCase):
    def setUp(self):
        """Initializes a fresh profiler instance before each test scenario runs."""
        self.profiler = PsycholinguisticProfiler()

    def test_empty_input_handling(self):
        """Validates that the engine securely rejects empty strings or whitespace errors."""
        empty_sample = "    "
        result = self.profiler.analyze_profile(empty_sample)
        
        self.assertIn("Error", result)
        self.assertEqual(result["Error"], "Text pool contains no valid linguistic tokens.")

    def test_tokenization_normalization(self):
        """Verifies that punctuation is stripped and keywords are evaluated case-insensitively."""
        punctuated_sample = "I! AM! CLEARLY! MYSELF!!!"
        tokens, total_count = self.profiler._preprocess_text(punctuated_sample)
        
        self.assertEqual(total_count, 4)
        self.assertIn("clearly", tokens)
        self.assertIn("myself", tokens)

    def test_trait_density_calculation(self):
        """Ensures that density metrics are accurately computed mathematically."""
        # This corpus contains exactly 10 words, 2 of which are core 'Ego & Hubris' tokens ("I", "my")
        ego_heavy_sample = "I believe that my personal direction is completely absolute today."
        result = self.profiler.analyze_profile(ego_heavy_sample)
        
        # Expected density = (2 matches / 10 words) * 100 = 20.0%
        calculated_density = result["Trait_Densities_Percentage"]["Ego & Hubris"]
        self.assertEqual(calculated_density, 20.0)

    def test_ocean_metric_boundaries(self):
        """Validates that the scaling vector engines safely cap numeric boundaries between 0 and 100."""
        # A massive repetition of ego-heavy tokens that could blow out the scoring weights
        extreme_sample = "I me my myself always never obviously clearly superior " * 50
        result = self.profiler.analyze_profile(extreme_sample)
        
        # Ensure scaling logic strictly honors the floor and ceiling parameters
        for dimension, score in result["Estimated_OCEAN_Profile"].items():
            self.assertTrue(0.0 <= score <= 100.0, f"Dimension {dimension} went out of bounds with score {score}")

if __name__ == "__main__":
    unittest.main()
