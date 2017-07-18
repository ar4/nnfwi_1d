from setuptools import setup, Extension
import numpy.distutils.core

prop = numpy.distutils.core.Extension(name='nnfwi_1d.prop', sources=['nnfwi_1d/prop.f90'], extra_f90_compile_args=['-O3', '-g', '-march=native', '-W', '-Wall', '-Wextra', '-pedantic'])#, '-fbounds-check'])

numpy.distutils.core.setup(
        name='nnfwi_1d',
        version='0.0.1',
        description='1D FWI using neural network',
        url='https://github.com/ar4/nnfwi_1d',
        author='Alan Richardson',
        author_email='alan@ausargeo.com',
        license='MIT',
        packages=['nnfwi_1d'],
        install_requires=['numpy', 'tensorflow'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
        ext_modules=[prop]
)
