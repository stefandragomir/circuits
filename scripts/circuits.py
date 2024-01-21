import os 
import sys
import ltspice
from subprocess import Popen

"""****************************************************************************
*******************************************************************************
****************************************************************************"""
class Spice():

	def __init__(self):

		self.path_lt  = r'c:\Program Files\ADI\LTspice\LTspice.exe'

	def get_raw_data_path(self,path_sim):

		_file_sim = os.path.split(path_sim)[1]
		_file_raw = "{}.raw".format(os.path.splitext(_file_sim)[0])

		_path_data = os.path.split(path_sim)[0]
		_path_data = os.path.join(_path_data,_file_raw)

		return _path_data

	def run(self,path_sim):

		_cmd = '"{}" -b -run "{}"'.format(self.path_lt,path_sim)

		_proc = Popen(_cmd, shell=False)

		_path_data = self.get_raw_data_path(path_sim)

		_data = ltspice.Ltspice(_path_data)

		return _data.parse()



