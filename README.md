# python-sdk

Interact with fQR Weave platform using a python <a href="https://pypi.org/project/fqrweaveSDK/0.0.1/">package</a>

<h1>Installation</h1>

In your terminal: <br>
`pip install fqrweaveSDK`
<h2>Connect your wallet:</h2>

`from fqrweaveSDK import Fqrweave, Tools` <br>
`jwk_path = '/path/to/your/file.json'` <br>
`connect = Fqrweave(jwk_path)` <br>
`connect.login()` <br>
