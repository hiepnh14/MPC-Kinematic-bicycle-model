
import numpy as np
from casadi import *
from casadi.tools import *
import pdb
# from math.tools import *
import sys
sys.path.append('../')
import do_mpc
def template_model(symvar_type='SX'):
    """
    --------------------------------------------------------------------------
    template_model: Variables / RHS / AUX
    --------------------------------------------------------------------------
    """

    # Obtain an instance of the do-mpc model class
    # and select time discretization:
    model_type = 'discrete' # either 'discrete' or 'continuous'
    model = do_mpc.model.Model(model_type, symvar_type)
    dt = 0.05 #time step
    # Introduce new states, inputs and other variables to the model, e.g.:
    _x = model.set_variable(var_type='_x', var_name='x', shape=(6,1))
    # [x, y, theta, v, a, delta]
    _u = model.set_variable(var_type='_u', var_name='u', shape=(2,1))
    # [a, delta]
    #Set expression
    model.set_expression(expr_name='cost', expr=sum1(((_x[1]-2)**2 + (_x[3]- 0.1)**2)))
    # Set right-hand-side of ODE for all introduced states (_x).
    # Names are inherited from the state definition.
    A = np.array([[ 1, 0, 0,  dt*cos(_x[2]), 0, 0],
                  [ 0, 1, 0,  dt*sin(_x[2]), 0, 0],
                  [ 0, 0, 1,  dt*tan(_u[1])/3.0, 0, 0],
                  [ 0, 0, 0, 1, dt, 0],
                  [ 0, 0, 0, 0, 0, 0],
                  [ 0, 0, 0, 0, 0, 0]])

    B = np.array([[0, 0],
                  [0, 0],
                  [0, 0],
                  [0, 0],
                  [1, 0],
                  [0, 1]])

    x_next = A@_x+B@_u
    model.set_rhs('x', x_next)
    model.setup()


    return model