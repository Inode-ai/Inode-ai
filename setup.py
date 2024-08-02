import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as rqf:
    reqs = [line.strip() for line in rqf if line.strip()]

setuptools.setup(
    
    name="inodeai",
    version="0.0.1",
    author="IndoeAi.com",
    author_email="support@inode-ai.com",
    description="The IndoeAi.com helper package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Inode-ai/Inode-ai",
    packages=setuptools.find_packages(where="./explainability_interface"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.10',
    license='MIT',
    install_requires=reqs,
)
