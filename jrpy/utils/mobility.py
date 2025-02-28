import numpy as np

def f(r, a=1):
    r = np.asarray(r)  # Convert input to a NumPy array if it's not already
    result = np.where(r<2*a, 1-9*r/(32*a), 3*a/(4*r)+0.5*(a/r)**3)
    return result if isinstance(r, np.ndarray) else result.item()  # Return scalar if input was scalar

def g(r, a=1):
    r = np.asarray(r)  # Convert input to a NumPy array if it's not already
    result = np.where(r<2*a, 3*r/(32*a), 3*a/(4*r)-1.5*(a/r)**2)
    return result if isinstance(r, np.ndarray) else result.item()  # Return scalar if input was scalar

def O(pos):
    return np.einsum('ni,nj->nij', pos, pos)

def mu_rpy(pos_i,pos_j,a=1):
    pos = pos_i-pos_j
    was_1D = pos.ndim==1
    pos = np.atleast_2d(pos)
    r = np.linalg.norm(pos, axis=1)
    fI = np.einsum('ij,n->nij', np.eye(2), f(r, a=a))
    gO = O(pos)*(g(r,a=a)/(r*r))[:,None,None]
    result = fI+gO
    return np.squeeze(result) if was_1D else result


