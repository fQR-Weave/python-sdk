# python-sdk

Interact with fQR Weave platform using a python <a href="https://pypi.org/project/fqrweaveSDK/0.0.1/">package</a>

<h1>Installation</h1>

In your terminal: <br>

`pip install fqrweaveSDK` or `pip install git+https://github.com/fQR-Weave/python-sdk.git`

<h2>Connect your wallet:</h2>


```
  from fqrweaveSDK import Fqrweave, Tools
  
  jwk_path = '/path/to/your/file.json'
  connect = Fqrweave(jwk_path)
  connect.login() # to keep your keyfile path connected in the current instance
  
```

<h2>Example:</h2>

after importing the package and get connected:
```
  generators_list = Tools().get_n_generators()
  print(generators_list)
```
This method, `.get_n_generators()` return a list of `jwk['n']` of verified generators. 

The actual number of generators is `len ( Tools().get_n_generators() - 1 )` because there is a wallet which belong to fQR Weave is added to the list in intention of testing.

You can anytime check how many generators fQR Weave have by calling this method. The scanner does not read any transaction generated by a wallet not included in this list.

<h2>Build</h2>
To make your own package according to your needs, fork the repository, do the changes then follow the following steps.<br>
<h3>1) Make your files meet PyPi needs</h3>
On your end, add the repository files in a directory/folder according to the following:

```
  yourFolder
        |
        --------------- fqrweaveSDK
        |                    |
        |                    ------------ __init__.py
        |                    |
        |                     ------------ client.py
        |
        ------------- setup.py
        |
        |---------------setup.cfg
        |
        ---------------------LICENSE.txt
        |
        ----------------------- README.md (optional)
         
```
<h3>2) Edit setup.py </h3>

To publish your own package, you have to edit `setup.py` :

```
  from distutils.core import setup

  setup(
    name="AS SAME AS YOU RE-NAMED fqrweaveSDK",
    packages=["AS SAME AS name"],
    version="0.0.1",
    description="...",
    url="https://github.com/fQR-Weave/fqrweaveSDK",
    author="...",
    author_email="xyz@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",

    ],

    include_package_data=True,
    install_requires=[
        "arweave-python-client" # external libraries required to run the sdk. more libraries
                                # to be added within the next releases
    ]
)
```
<h3>3) Upload your package to Pypi</h3>

Requirements:

`pip install twine `

Open the terminal in `yourFolder` then tap the following commands:

```
  >>> python setup.py sdist
  >>> twine upload dist/*
```

You can then find your package at https://pypi.org/project/YOURPACKAGENAME/ 
