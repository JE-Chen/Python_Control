import setuptools

with open("README.md", "r") as README:
    long_description = README.read()

setuptools.setup(
    name="je_auto_control",
    version="0.0.5",
    author="JE-Chen",
    author_email="zenmailman@gmail.com",
    description="auto control alpha 0.0.3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JE-Chen/Python_AutoControl",
    packages=setuptools.find_packages(),
    install_requires=["je_open_cv", "pillow", "numpy"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Traditional)",
        "Operating System :: Microsoft"
    ]
)

# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
