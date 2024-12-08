from anar import ANARSystem

def analyze_sindbad():
    """Example analysis of a Sindbad story."""
    # Load sample text
    with open('examples/sample_texts/sindbad.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        
    # Initialize system
    anar = ANARSystem()
    
    # Process text
    result = anar.process_text(text)
    
    # Print narrative structure
    print("=== Narrative Structure ===")
    for story in result['narrative_analysis']['nested_stories']:
        print(f"\nFrame: {story['frame_marker']}")
        for element in story['elements']:
            print(f"  {element['type']}: {element['text']}")
            
    # Print cultural patterns
    print("\n=== Cultural Patterns ===")
    for pattern in result['cultural_analysis']['patterns']:
        print(f"\nType: {pattern['category']}")
        print(f"Pattern: {pattern['pattern']}")
        print(f"Confidence: {pattern['confidence']:.2f}")
        
    # Print character relationships
    print("\n=== Character Network ===")
    char_graph = result['character_graph']
    for char1 in char_graph.nodes():
        for char2 in char_graph.neighbors(char1):
            print(f"{char1} <-> {char2}")

if __name__ == "__main__":
    analyze_sindbad()

