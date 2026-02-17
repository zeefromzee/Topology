"""Vertex removal and link computation.

This module analyzes the effect of removing vertices from simplicial
complexes and computes vertex links.
"""


def vertex_link(complex, vertex):
    """Compute the link of a vertex in a simplicial complex.
    
    The link of a vertex v is the subcomplex consisting of all faces
    that don't contain v but are contained in a face with v.
    
    Args:
        complex: SimplicialComplex instance.
        vertex: Vertex whose link to compute.
        
    Returns:
        SimplicialComplex representing the link.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def vertex_star(complex, vertex):
    """Compute the star of a vertex.
    
    Args:
        complex: SimplicialComplex instance.
        vertex: Vertex whose star to compute.
        
    Returns:
        SimplicialComplex representing the star.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def remove_vertex(complex, vertex):
    """Remove a vertex from a complex.
    
    Args:
        complex: SimplicialComplex instance.
        vertex: Vertex to remove.
        
    Returns:
        New SimplicialComplex with vertex removed.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def analyze_vertex_criticality(complex, vertices=None):
    """Analyze how critical each vertex is to the topology.
    
    Args:
        complex: SimplicialComplex instance.
        vertices: Vertices to analyze. If None, analyzes all vertices.
        
    Returns:
        Dictionary mapping vertices to criticality measures.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")
