import os

def discover(initial_path):
    extensions = ['jpg', 'png','pdf']

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath,_file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                print(ext)
                yield absolute_path

# So é executado quando executa o modulo diretamente

if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)
