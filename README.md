# ANAR: Arabic Narrative Analysis and Recognition System

ANAR is a Python library for analyzing Classical Arabic narratives, with special focus on the analysis of texts like the 1001 Arabian Nights. It provides tools for narrative structure analysis, cultural pattern recognition, and morphological processing of Classical Arabic texts.

## Features

- Graph-based narrative structure analysis
- Cultural pattern recognition and preservation
- Classical Arabic morphological analysis
- Frame story detection
- Nested narrative analysis
- Cultural reference preservation

## Installation

```bash
pip install -r requirements.txt
python setup.py install
```

## Quick Start

```python
from anar import ANARSystem

# Initialize the system
anar = ANARSystem()

# Process a text
text = "قالت شهرزاد: وحدثني أيها الملك السعيد..."
result = anar.process_text(text)

# Access results
narrative_structure = result.narrative_graph
cultural_elements = result.cultural_patterns
frame_stories = result.frame_stories
```

## Requirements

See requirements.txt for full dependencies.

## Documentation

See the /docs directory for detailed API documentation and examples.
