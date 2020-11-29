import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


	
setuptools.setup(
    name="niths_juvini", # Replace with your own username
    version="0.0.3",
    author="Niths",
    author_email="nitinmn@gmail.com",
    description="EDA for dummies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niths4u/juvini",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=['pandas','itertools','matplotlib','seaborn','warnings'],
    python_requires='>=3.6',
	include_package_data=True
)