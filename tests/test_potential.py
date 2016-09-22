""" Tests the evaluation of the potential for single and array-valued arguments for SHO, bump and KP potentials
"""
import numpy as np
import pytest
from basis.potential import Potential

def test_getattr():
    """Tests the attributes re-routing to potential.params.
    """

    pot= Potential("potentials/kp.cfg")
    assert pot.w == pot.params["w"]

    pot = Potential("potentials/bump.cfg")
    assert pot.a == pot.params["a"]

    pot = Potential("potentials/sho.cfg")
    assert pot.shift == pot.params["shift"]
    with pytest.raises(AttributeError):
        pot.dummy

def adjust(pot, **kwargs):
    """Adjusts the parameters of the potential.

    Args:
    kwargs(dict: parameters and values to overwrite.)
    """
    self.params.update(kwargs)
    self._parse_regions()


def test_sho():
    """Tests the SHO potential.
    """
    pot = Potential("potentials/sho.cfg")

    params = [(2,1,-15,100),
              (1e5,1e3,-1234.,1e5),
              (1./3,1./6,-10,5),
              (np.pi,np.pi/2., -np.sqrt(2),23)]

    for a, shift, V0, N in params:
        pot.adjust(a=a,shift=shift,v0=V0)
        xa= np.linspace(-a,a,N)
        assert pot(shift) == 0.
        assert pot(shift/2.) == V0/4.*shift**2
        assert len(pot(xa))== N
        assert pot(a) == 0.
        assert pot(-5.*a) == 0.
        with pytest.raises(ValueError):
         pot("a")



def test_bump():
    """Tests the bump in the square well potential.
    """

    pot = Potential("potentials/bump.cfg")

    params = [(2,1,-15,100),
              (1e5,1e3,-1234.,1e5),
              (1./3,1./6,-10,5),
              (np.pi,np.pi/2., -np.sqrt(2),23)]


    for a, w, V0, N in params:
        pot.adjust(a=a,w=w,v0=V0)
        x=w+(a-w)/2.
        xa= np.linspace(-a,a,N)
        assert pot(x) == 0. 
        assert pot(3./4*w) == V0
        assert len(pot(xa))== N
        assert pot(-5.*a) == 0.
        assert pot(-w) == V0
        assert pot(a) == 0.
        with pytest.raises(ValueError):
         pot("a")


def test_kp():
    """Tests the bump in the square well potential.
    """

    pot = Potential("potentials/kp.cfg")

    #pot.adjust(n=n,w=w,b=b,v0=V0)
    assert pot(-pot.params["b"]/2)== pot.params["v0"]
    assert pot(pot.params["b"]/2)== 0.
    assert pot(pot.params["w"])== 0.
    
    with pytest.raises(ValueError):
         pot("a")

