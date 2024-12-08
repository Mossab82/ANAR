python
from anar import ANARSystem

# Initialize system
anar = ANARSystem()

# Process a simple story
text = """قالت شهرزاد: وحدثني أيها الملك السعيد أن تاجراً
          من التجار كان كثير المال..."""
          
result = anar.process_text(text)

# Print narrative structure
for story in result['narrative_analysis']['nested_stories']:
    print(f"Frame: {story['frame_marker']}")
    for element in story['elements']:
        print(f"  {element['type']}: {element['text']}")


## Cultural Pattern Analysis

python
# Analyze cultural patterns
text = """في عهد هارون الرشيد كان تاجر عظيم
          ضرب في الأرض يطلب التجارة..."""
          
result = anar.process_text(text)

# Print cultural patterns
for pattern in result['cultural_analysis']['patterns']:
    print(f"Pattern: {pattern['pattern']}")
    print(f"Category: {pattern['category']}")
    print(f"Context: {pattern['info']['context']}")


## Character Network Analysis

python
# Analyze character relationships
result = anar.process_text(text)
char_graph = result['character_graph']

# Print character relationships
for char1 in char_graph.nodes():
    for char2 in char_graph.neighbors(char1):
        print(f"{char1} <-> {char2}")
