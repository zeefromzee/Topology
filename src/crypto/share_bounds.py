"""Information-theoretic share size bounds.

This module computes theoretical lower and upper bounds on share sizes
for secret sharing schemes.
"""


def shannon_lower_bound(access_structure, secret_size):
    """Compute Shannon's information-theoretic lower bound on share sizes.
    
    Args:
        access_structure: Collection of authorized subsets.
        secret_size: Size of the secret in bits.
        
    Returns:
        Dictionary mapping participants to minimum share sizes.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def compute_rate(access_structure, secret_size, share_sizes):
    """Compute the information rate of a secret sharing scheme.
    
    The information rate is the ratio of secret size to maximum share size.
    
    Args:
        access_structure: Collection of authorized subsets.
        secret_size: Size of the secret in bits.
        share_sizes: Dictionary mapping participants to share sizes.
        
    Returns:
        Information rate as a float.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")


def is_ideal(share_sizes, secret_size):
    """Check if a scheme is ideal (all shares equal secret size).
    
    Args:
        share_sizes: Dictionary mapping participants to share sizes.
        secret_size: Size of the secret in bits.
        
    Returns:
        True if the scheme is ideal, False otherwise.
        
    Raises:
        NotImplementedError: To be implemented.
    """
    raise NotImplementedError("To be implemented")
