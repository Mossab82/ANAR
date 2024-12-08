import networkx as nx
from typing import Dict, List
import re

class NarrativeAnalyzer:
    """Analyzer for narrative structures in Classical Arabic texts."""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.graph = nx.DiGraph()
        
    def analyze(self, processed_text: Dict) -> Dict:
        """Analyze narrative structure of processed text.
        
        Args:
            processed_text: Output from TextPreprocessor
            
        Returns:
            Dict containing narrative analysis results
        """
        # Extract narrative elements
        narrative_elements = self._extract_narrative_elements(
            processed_text['normalized_text'],
            processed_text['frame_markers']
        )
        
        # Build narrative graph
        self._build_narrative_graph(narrative_elements)
        
        # Detect nested stories
        nested_stories = self._detect_nested_stories()
        
        # Analyze character relationships
        character_network = self._analyze_character_network()
        
        return {
            'narrative_graph': self.graph,
            'nested_stories': nested_stories,
            'character_network': character_network
        }
        
    def _extract_narrative_elements(
        self, 
        text: str, 
        frame_markers: List[Tuple[str, int]]
    ) -> List[Dict]:
        """Extract narrative elements from text.
        
        Args:
            text: Normalized text
            frame_markers: List of frame markers and positions
            
        Returns:
            List of narrative element dictionaries
        """
        elements = []
        
        # Extract characters
        character_patterns = [
            r'[الـ]?ملك\s+\w+',
            r'[الـ]?وزير\s+\w+',
            r'[الـ]?تاجر\s+\w+'
        ]
        
        for pattern in character_patterns:
            for match in re.finditer(pattern, text):
                elements.append({
                    'type': 'character',
                    'text': match.group(),
                    'position': match.start()
                })
        
        # Extract events
        event_patterns = [
            r'فلما كان [^،.]+',
            r'ثم [^،.]+'
        ]
        
        for pattern in event_patterns:
            for match in re.finditer(pattern, text):
                elements.append({
                    'type': 'event',
                    'text': match.group(),
                    'position': match.start()
                })
                
        # Add frame markers as narrative elements
        for marker, position in frame_markers:
            elements.append({
                'type': 'frame',
                'text': marker,
                'position': position
            })
                
        return sorted(elements, key=lambda x: x['position'])
        
    def _build_narrative_graph(self, narrative_elements: List[Dict]):
        """Build directed graph from narrative elements.
        
        Args:
            narrative_elements: List of narrative elements
        """
        prev_node = None
        
        for element in narrative_elements:
            # Add node
            node_id = f"{element['type']}_{len(self.graph.nodes)}"
            self.graph.add_node(
                node_id,
                type=element['type'],
                text=element['text']
            )
            
            # Add edge from previous node if it exists
            if prev_node:
                self.graph.add_edge(prev_node, node_id)
                
            prev_node = node_id
            
    def _detect_nested_stories(self) -> List[Dict]:
        """Detect nested story structures in the narrative graph.
        
        Returns:
            List of nested story dictionaries
        """
        nested_stories = []
        frame_nodes = [
            node for node, attr in self.graph.nodes(data=True)
            if attr['type'] == 'frame'
        ]
        
        for frame_node in frame_nodes:
            # Get subgraph between this frame and next frame
            story = {
                'frame_marker': self.graph.nodes[frame_node]['text'],
                'elements': []
            }
            
            # Add narrative elements until next frame
            current = frame_node
            while current in self.graph:
                next_nodes = list(self.graph.successors(current))
                if not next_nodes:
                    break
                    
                current = next_nodes[0]
                node_data = self.graph.nodes[current]
                
                if node_data['type'] != 'frame':
                    story['elements'].append({
                        'type': node_data['type'],
                        'text': node_data['text']
                    })
                else:
                    break
                    
            nested_stories.append(story)
            
        return nested_stories
        
    def _analyze_character_network(self) -> nx.Graph:
        """Analyze character relationships in the narrative.
        
        Returns:
            NetworkX graph of character relationships
        """
        character_graph = nx.Graph()
        
        # Get character nodes
        character_nodes = [
            node for node, attr in self.graph.nodes(data=True)
            if attr['type'] == 'character'
        ]
        
        # Add characters to graph
        for node in character_nodes:
            character_name = self.graph.nodes[node]['text']
            character_graph.add_node(character_name)
            
        # Add edges between characters that appear in same story segment
        for story in self._detect_nested_stories():
            story_characters = [
                elem['text'] for elem in story['elements']
                if elem['type'] == 'character'
            ]
            
            # Create edges between all characters in story
            for i, char1 in enumerate(story_characters):
                for char2 in story_characters[i+1:]:
                    if char1 in character_graph and char2 in character_graph:
                        character_graph.add_edge(char1, char2)
                        
        return character_graph
