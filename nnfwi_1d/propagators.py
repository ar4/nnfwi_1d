"""Propagate a 1D wavefield using an 16th order finite difference method.
"""
import numpy as np
import nnfwi_1d
from nnfwi_1d import prop

class Propagator(object):
    """A 16th order finite difference propagator for the 1D wave equation."""
    def __init__(self, model, dx, dt=None, npad=450):
        self.nx = len(model)
        self.dx = np.float32(dx)
        max_vel = np.max(model)
        if dt:
            self.dt = dt
        else:
            self.dt = 0.6 * self.dx / max_vel
        self.npad=npad
        self.nx_padded = self.nx + 2*self.npad
        #self.model_padded = np.pad(model, (8, 8), 'edge')
        self.model_padded = np.pad(model, (self.npad, self.npad), 'edge')

class propagator(Propagator):
    """A Fortran implementation."""
    def step(self, num_steps, source):
        """Propagate wavefield."""

        self.disp = np.zeros([self.nx_padded, num_steps+2], np.float32,
                             order='F')

        source_len = len(source)

        prop.prop.step(self.disp,
                       self.model_padded, self.dt, self.dx,
                       num_steps, self.nx_padded,
                       source_len, source, self.npad)

        return self.disp[self.npad, 2:]
