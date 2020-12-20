# python-sdk

Interact with fQR Weave platform using a python package

#Installation

In your terminal:
`pip install fqrweaveSDK`
<h2>Connect your wallet:</h2>

`from fqrweaveSDK import Fqrweave, Tools
jwk_path = '/path/to/your/file.json'
connect = Fqrweave(jwk_path)
connect.login()`
