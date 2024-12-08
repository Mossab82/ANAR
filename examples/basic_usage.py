from anar import ANARSystem

def main():
    # Initialize system
    anar = ANARSystem()
    
    # Sample text
    text = """قالت شهرزاد: وحدثني أيها الملك السعيد أن تاجراً من التجار 
              كان كثير المال، فضرب في الأرض يطلب الربح والتجارة..."""
              
    # Process text
    result = anar.process_text(text)
    
    # Access results
    print("Narrative Structure:")
    for story in result['narrative_analysis']['nested_stories']:
        print(f"Frame: {story['frame_marker']}")
        for element in story['elements']:
            print(f"  {element['type']}: {element['text']}")
            
    print("\nCultural Patterns:")
    for pattern in result['cultural_analysis']['patterns']:
        print(f"Type: {pattern['category']}")
        print(f"Pattern: {pattern['pattern']}")
        print(f"Confidence: {pattern['confidence']:.2f}")
        print()

if __name__ == "__main__":
    main()
