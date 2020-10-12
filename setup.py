import setuptools

with open("JEAutoControl/README.md", "r") as README:
    long_description = README.read()

setuptools.setup(
    name="JEAutoControl",
    version="0.0.2",
    author="JE-Chen",
    author_email="zenmailman@gmail.com",
    description="Windows auto control alpha 0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JE-Chen/Python_Control",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Traditional)",
        "Operating System :: Microsoft"
    ]
)

#sdist bdist_wheel