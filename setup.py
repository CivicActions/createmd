from setuptools import setup

setup(
    name='createmd',
    description='Use Secrender to create markdown files.',
    version='0.1',
    author='Tom Camp',
    author_email='tom.camp@civicactions.com',
    license='CC',
    packages=['createmd'],
    zip_safe=False,
    install_requires=[
        'pyyaml',
        'pyyaml-include',
        'click',
    ],
    entry_points = {
        'console_scripts': ['sspcreate=sspcreate.sspcreate:main']
    }
)
