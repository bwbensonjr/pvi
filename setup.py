import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    "pandas",
    ]
    
setuptools.setup(
    name="pvi",
    version="0.0.1",
    author="Brent Benson",
    author_email="bwbensonjr@gmail.com",
    maintainer="Brent Benson",
    maintainer_email="bwbensonjr@gmail.com",
    license="BSD",
    description="Calculate Partisan Voter Index (PVI)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bwbensonjr/pvi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.5',
)
