import os
import sys

_path = __file__
_path = os.path.split(_path)[0]
_path = os.path.split(_path)[0]
_path = os.path.join(_path,"scripts")
sys.path.append(_path)

from circuits import Spice
import matplotlib.pyplot as plt
import numpy as np

"""****************************************************************************
*******************************************************************************
****************************************************************************"""
if __name__ == "__main__":

	_sim = Spice()

	_path = os.path.split(__file__)[0]
	_path = os.path.join(_path,"bridge_rectifier.asc")

	_data = _sim.run(_path)

	_time = _data.get_time()
	_v_out = _data.get_data("V(Vout)")

	plt.plot(_time, _vout)
	plt.show()