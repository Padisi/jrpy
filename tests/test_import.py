def test_import():
    import jrpy as jrpy

def test_create_particle():
    import numpy as np
    import jrpy as jrpy
    p = jrpy.particle(np.array([1,1]),np.array([0,0]), 1,rgb=(0,0,1))
