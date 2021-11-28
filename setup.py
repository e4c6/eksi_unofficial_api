import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eksisozluk",
    version="1.0.2",
    author="Mahir Tüzel",
    author_email="e4c6@dataso.me",
    description="Ekşisözlük API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/e4c6/eksi_unofficial_api",
    project_urls={
        "Bug Tracker": "https://github.com/e4c6/eksi_unofficial_api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=["requests", "python-dateutil"],
    python_requires=">=3.6",
)
