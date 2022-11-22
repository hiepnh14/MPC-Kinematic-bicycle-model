<<<<<<< HEAD
import numpy as np
from casadi import *
from casadi.tools import *
import pdb
import sys
sys.path.append('../')
import do_mpc


""
# def template_mpc(model):
#     # Obtain an instance of the do-mpc MPC class
#     # and initiate it with the model:
#     mpc = do_mpc.controller.MPC(model)
#
#     # Set parameters:
#     setup_mpc = {
#         'n_horizon': 20,
#         'n_robust': 1,
#         't_step': 0.005,
#         'store_full-solution':True,
#     }
#     mpc.set_param(**setup_mpc)
#
#     # Configure objective function:
#     mterm = (_x['C_b'] - 0.6)**2    # Setpoint tracking
#     lterm = (_x['C_b'] - 0.6)**2    # Setpoint tracking
#
#     mpc.set_objective(mterm=mterm, lterm=lterm)
#     mpc.set_rterm(F=0.1, Q_dot = 1e-3) # Scaling for quad. cost.
#
#     # State and input bounds:
#     mpc.bounds['lower', '_x', 'C_b'] = 0.1
#     mpc.bounds['upper', '_x', 'C_b'] = 2.0
#     ...
#
#     mpc.setup()
#
#     return mpc
def template_mpc(model):
    """
    --------------------------------------------------------------------------
    template_mpc: tuning parameters
    --------------------------------------------------------------------------
    """
    mpc = do_mpc.controller.MPC(model)

    setup_mpc = {
        'n_robust': 0,
        'n_horizon': 7,
        't_step': 0.5,
        'store_full_solution':True,
    }

    mpc.set_param(**setup_mpc)

    mterm = model.aux['cost']
    lterm = model.aux['cost'] # terminal cost

    mpc.set_objective(mterm=mterm, lterm=lterm)
    mpc.set_rterm(u=1e-4)

    max_x = np.array([[10.0], [10.0], [np.pi], [10.0], [2], [1]])
    max_u = np.array([[2], [1]])
    mpc.bounds['lower','_x','x'] = -max_x
    mpc.bounds['upper','_x','x'] =  max_x

    mpc.bounds['lower','_u','u'] = -max_u
    mpc.bounds['upper','_u','u'] =  max_u


    mpc.setup()

    return mpc
=======
import numpy as np
from casadi import *
from casadi.tools import *
import pdb
import sys
sys.path.append('../')
import do_mpc


""
# def template_mpc(model):
#     # Obtain an instance of the do-mpc MPC class
#     # and initiate it with the model:
#     mpc = do_mpc.controller.MPC(model)
#
#     # Set parameters:
#     setup_mpc = {
#         'n_horizon': 20,
#         'n_robust': 1,
#         't_step': 0.005,
#         'store_full-solution':True,
#     }
#     mpc.set_param(**setup_mpc)
#
#     # Configure objective function:
#     mterm = (_x['C_b'] - 0.6)**2    # Setpoint tracking
#     lterm = (_x['C_b'] - 0.6)**2    # Setpoint tracking
#
#     mpc.set_objective(mterm=mterm, lterm=lterm)
#     mpc.set_rterm(F=0.1, Q_dot = 1e-3) # Scaling for quad. cost.
#
#     # State and input bounds:
#     mpc.bounds['lower', '_x', 'C_b'] = 0.1
#     mpc.bounds['upper', '_x', 'C_b'] = 2.0
#     ...
#
#     mpc.setup()
#
#     return mpc
def template_mpc(model):
    """
    --------------------------------------------------------------------------
    template_mpc: tuning parameters
    --------------------------------------------------------------------------
    """
    mpc = do_mpc.controller.MPC(model)

    setup_mpc = {
        'n_robust': 0,
        'n_horizon': 7,
        't_step': 0.5,
        'store_full_solution':True,
    }

    mpc.set_param(**setup_mpc)

    mterm = model.aux['cost']
    lterm = model.aux['cost'] # terminal cost

    mpc.set_objective(mterm=mterm, lterm=lterm)
    mpc.set_rterm(u=1e-4)

    max_x = np.array([[10.0], [10.0], [np.pi], [10.0], [2], [1]])
    max_u = np.array([[2], [1]])
    mpc.bounds['lower','_x','x'] = -max_x
    mpc.bounds['upper','_x','x'] =  max_x

    mpc.bounds['lower','_u','u'] = -max_u
    mpc.bounds['upper','_u','u'] =  max_u


    mpc.setup()

    return mpc
>>>>>>> 2a19200d1d826db7ef0dbd185f888e3c94ea8957
