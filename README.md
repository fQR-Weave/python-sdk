# python-sdk

Interact with fQR Weave platform using a python <a href="https://pypi.org/project/fqrweaveSDK/0.0.1/">package</a>

<h1>Installation</h1>

In your terminal: <br>
`pip install fqrweaveSDK`
<h2>Connect your wallet:</h2>


```
  from fqrweaveSDK import Fqrweave, Tools
  
  jwk_path = '/path/to/your/file.json'
  connect = Fqrweave(jwk_path)
  connect.login() # to keep your keyfile path connected in the current instance
  
```

