import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gender_gap_3g",
    version="0.0.1",
    author="Kiarash Hosseini",
    author_email="k.hosseini1130@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k-hosseini?tab=repositories",
    project_urls={
        "Bug Tracker": "https://github.com/k-hosseini?tab=repositories",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    #python_requires=">=2.6",
)
