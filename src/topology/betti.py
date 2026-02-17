"""Betti number computation.

This module computes Betti numbers of simplicial complexes, which measure
the number of k-dimensional holes.
"""


def compute_betti_numbers(complex, max_dimension=None):
    """Compute all Betti numbers of a simplicial complex.
    
    Args:
        complex: SimplicialComplex instance.
        max_dimension: Maximum dimension to compute. If None, uses complex dimension.
        
    Returns:
        Dictionary mapping dimensions to Betti numbers.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def betti_number(complex, dimension):
    """Compute the k-th Betti number.
    
    The k-th Betti number is the rank of the k-th homology group.
    
    Args:
        complex: SimplicialComplex instance.
        dimension: Dimension k.
        
    Returns:
        Integer Betti number.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def poincare_polynomial(betti_numbers):
    """Construct the Poincare polynomial from Betti numbers.
    
    Args:
        betti_numbers: Dictionary mapping dimensions to Betti numbers.
        
    Returns:
        String representation of the Poincare polynomial.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")
