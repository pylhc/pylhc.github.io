# How to create a virtual python enviroment

Both for the development of python codes as well as running some of the existing codes,
the creation of a virtual python enviroment is recommended. This not only prevents
conflicts when installing multiple packages with different required versions of the same package,
but also allows to separate production and test scenarios. 

Python enviroments are created using the `venv` module, with the old `pyvenv` being deprecated
since `Python 3.6` and as such not recommened. The following description is a summary 
of the steps presented [here][venv_module]{target=_blank} and [here][pip_venv]{target=_blank},
specifically targetting Linux users.

Note that [Anaconda Python distribution][anaconda]{target=_blank} provides the `conda` tool, which also the
creation of python enviroments. However, due to the simplicity of the `venv` module,
only this module will be described in the following.



[venv_module]: https://docs.python.org/3/library/venv.html
[pip_venv]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
[anaconda]: https://www.anaconda.com/products/individual
