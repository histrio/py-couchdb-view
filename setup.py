from setuptools import setup

description = "Python view server for CouchDB"

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py


setup(
    name="pycouchdbview",
    url="https://github.com/histrio/py-couchdb-view",
    author="Andrey Antukh",
    author_email="niwi@niwi.be",
    maintainer='Rinat Sabitov',
    maintainer_email='rinat.sabitov@gmail.com',
    version='0.0.1',
    packages=[".", ],
    package_dir={'': 'src'},
    description=description.strip(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    cmdclass={"build_py": build_py},
    install_requires=["pycouchdb"],

    test_suite='test',
    tests_require=['mock', 'nose', 'responses'],
)
