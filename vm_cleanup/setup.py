from setuptools import setup, find_packages

setup(
    name='vm_cleanup',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'vm-cleanup=gemfury.main:main',  # Use vm_cleanup.main here
        ],
    },
    author='Aakash',
    description='CLI tool for cleaning up Docker images safely.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
)
