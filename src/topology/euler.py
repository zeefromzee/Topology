"""Euler characteristic computation.

This module computes the Euler characteristic of simplicial complexes.
"""


def compute_euler_characteristic(complex):
    """Compute the Euler characteristic of a simplicial complex.
    
    The Euler characteristic is the alternating sum of the number of
    k-dimensional faces: χ = Σ(-1)^k * f_k
    
    Args:
        complex: SimplicialComplex instance.
        
    Returns:
        Integer Euler characteristic.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def euler_from_betti(betti_numbers):
    """Compute Euler characteristic from Betti numbers.
    
    Uses the formula: χ = Σ(-1)^k * β_k
    
    Args:
        betti_numbers: Dictionary mapping dimensions to Betti numbers.
        
    Returns:
        Integer Euler characteristic.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def f_vector(complex):
    """Compute the f-vector (face counts) of a complex.
    
    Args:
        complex: SimplicialComplex instance.
        
    Returns:
        List where f_vector[k] is the number of k-dimensional faces.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def h_vector(complex):
    """Compute the h-vector of a complex.
    
    Args:
        complex: SimplicialComplex instance.
        
    Returns:
        List representing the h-vector.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")
