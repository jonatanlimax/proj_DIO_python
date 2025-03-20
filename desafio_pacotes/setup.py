from setuptools import setup, find_packages

setup(
    name="farmacia_saramorreu",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'farmacia_saramorreu = farmacia_saramorreu.farmacia:iniciar',  
        ],
    },
    author="JonatanLima",
    author_email="jonatanrobertodl@gmail.com",
    description="Farmácia virtual para compra de medicamentos.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/username/farmacia_saramorreu",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
