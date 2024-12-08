The main system class that coordinates all analysis components.

python
class ANARSystem:
    def __init__(self, config: Dict = None)
    def process_text(self, text: str) -> Dict


### TextPreprocessor

Handles preprocessing of Classical Arabic texts.

python
class TextPreprocessor:
    def __init__(self, config: Dict = None)
    def process(self, text: str) -> Dict


### NarrativeAnalyzer

Analyzes narrative structures using graph-based methods.

python
class NarrativeAnalyzer:
    def __init__(self, config: Dict = None)
    def analyze(self, processed_text: Dict) -> Dict


### CulturalProcessor

Processes cultural patterns and references.

python
class CulturalProcessor:
    def __init__(self, config: Dict = None)
    def process(self, processed_text: Dict) -> Dict


## Usage Examples

Basic text processing:
python
from anar import ANARSystem

anar = ANARSystem()
result = anar.process_text("قالت شهرزاد: وحدثني أيها الملك السعيد...")

# Access results
narrative_structure = result['narrative_analysis']
cultural_patterns = result['cultural_analysis']
