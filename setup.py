import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="torchdistlog",
    version="0.0.0",
    author="Borui Zhang",
    author_email="zhang-br21@mails.tsinghua.edu.cn",
    description="Logging for distributed PyTorch training.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zbr17/torchdistlog",
    project_urls={
        "Docs": "https://github.com/zbr17/torchdistlog",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "torch >= 1.7.0"
    ]
)