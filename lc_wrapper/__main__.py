from ipykernel.kernelapp import IPKernelApp
from .ipython import PythonKernelBuffered

IPKernelApp.launch_instance(kernel_class=PythonKernelBuffered)
