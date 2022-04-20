import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gender-gap-in-iran",
    version="0.0.2",
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
    package_data={'gender-gap-in-iran': ["data/*.zip"]},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
)
