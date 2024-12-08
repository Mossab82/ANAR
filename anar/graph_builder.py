import networkx as nx
from typing import Dict, List

class GraphBuilder:
    """Builder for narrative and cultural graph representations."""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        
    def build_narrative_graph(
        self,
        narrative_analysis: Dict,
        cultural_analysis: Dict
    ) -> nx.DiGraph:
        """Build comprehensive narrative graph with cultural elements.
        
        Args:
            narrative_analysis: Output from NarrativeAnalyzer
            cultural_analysis: Output from CulturalProcessor
            
        Returns:
            NetworkX DiGraph representing the narrative structure
        """
        G = nx.DiGraph()
        
        # Add narrative elements
        for story in narrative_analysis['nested_stories']:
            story_id = f"story_{len(G.nodes)}"
            G.add_node(
                story_id,
                type='story',
                frame=story['frame_marker']
            )
            
            # Add story elements
            prev_node = story_id
            for element in story['elements']:
                node_id = f"{element['type']}_{len(G.nodes)}"
                G.add_node(
                    node_id,
                    type=element['type'],
                    text=element['text']
                )
                G.add_edge(prev_node, node_id)
                prev_node = node_id
                
        # Add cultural elements
        for pattern in cultural_analysis['patterns']:
            pattern_id = f"cultural_{len(G.nodes)}"
            G.add_node(
                pattern_id,
                type='cultural',
                category=pattern['category'],
                text=pattern['pattern'],
                info=pattern['info']
            )
            
            # Link to relevant story elements
            for node in G.nodes():
                if G.nodes[node]['type'] in ['character', 'event']:
                    if pattern['pattern'] in G.nodes[node]['text']:
                        G.add_edge(node, pattern_id)
                        
        return G
        
    def build_character_graph(
        self,
        narrative_analysis: Dict
    ) -> nx.Graph:
        """Build character interaction graph.
        
        Args:
            narrative_analysis: Output from NarrativeAnalyzer
            
        Returns:
            NetworkX Graph representing character relationships
        """
        return narrative_analysis['character_network']

