from setuptools import setup, find_packages

# setup(
#     name="python_example",
#     package_dir={
#         "package1": "src/package1",
#         "package2": "src/package2",
#     },
#     packages=["package1", "package2"],
# )


setup(
    name="python_example",
    package_dir={
        "": "src",
    },
    packages=find_packages(
        where="src"
    ),  # find_namespace_packages()  accepts packages without a __init__.py
)
