from fqrweaveSDK import Fqrweave, Tools

fqrweave = Fqrweave('path to your keyfile.json')
fqrweave.login() #link your keyfile

for n in range(0, 10):
    gen_fqr = Tools().batch_generator('arweave.net/tx_ID or tx_ID of your generator instance ',
                                      'array of your gen instance input field(labels) ',
                                      'path to the directory where you want to save the .png QRs')

    # example: gen_fqr = Tools().batch_generator('https://arweave.net/hQoxFXZ2r-Vb04dMaNeaf7teFFQV4vuERB-MfGUO610',
    #                                      ['test1', 10, None, '10-10-2020'],
    #                                      'C:/.../.../Somewhere/qrs_dir')

    print(gen_fqr)


