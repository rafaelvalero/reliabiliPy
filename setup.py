import setuptools
# Packages
base_packages = [
    "factor_analyzer"
]

# Load the long_description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OmegaPy",
    version="0.0.6",
    author="Rafael Valero-Fernandez",
    author_email="rafael.valero.fernandez@gmail.com",
    description="Simple implementation in Python of the reliability: "
                "Omega Total,Omega Hierarchical and Omega Hierarchical Total.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelvalero/OmegaPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=base_packages,)
