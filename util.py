import re
from fuzzywuzzy import fuzz, process
from .models import ProductMapping

# Normalize product names
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.replace("sh", "sheets")  # Handle common abbreviations
    return text.strip()

# Match product names using fuzzy matching
def match_product(input_name, mapping_dict):
    normalized_input = normalize_text(input_name)
    best_match, score = process.extractOne(normalized_input, mapping_dict.keys(), scorer=fuzz.partial_ratio)
    if score > 80:  # Threshold for similarity
        return mapping_dict[best_match], score
    return None, score

# Load mappings from database
def load_mapping():
    mappings = ProductMapping.query.all()
    return {normalize_text(m.supplier_name): m.standardized_name for m in mappings}
