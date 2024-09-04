from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter.simpledialog import askinteger
from tkinter.messagebox import showinfo, showerror
from rembg import remove
from PIL import Image
import sys, glob, os

def imagem_unica():
    try:
        input_path = askopenfilename(title="Escolha a imagem para remover o fundo",
                                    filetypes=[('Imagens', ('*.jpg', '*.jpeg', '*.png', '*.tiff', '*.webp')), ("Outras", "*.*")])

        output_path = asksaveasfilename(title="Escolha onde salvar sua imagem",
                                        filetypes=[('Imagens', ('*.png')), ("Outras", "*.*")])

        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)
        showinfo("Sucesso!", f"Fundo da imagem removido com sucesso.")
    except Exception as e:
        showerror(f"Erro", "Erros encontrados:\n{e}")

def imagem_lote():
    try:
        diretorio = askdirectory(title="Diretório dom as imagens pra remover bg")    
        arquivos = glob.glob(f'{diretorio}/*.*')
        
        for arq in arquivos:
            if  '*.jpg' or '*.jpeg' or '*.png' or '*.tiff' or '*.webp' in arq:
                output = remove(Image.open(arq))
                caminho_sem_extensao, extensao = os.path.splitext(arq)
                output.save(caminho_sem_extensao+'.png')            
            showinfo("Sucesso!", f"Todas as imagens com bg removido.")
    except Exception as e:
        showerror(f"Erro", "Erros encontrados:\n{e}")

def main():

    if len(sys.argv) == 3:
        try:            
            output = remove(Image.open(sys.argv[1]))
            output.save(sys.argv[2])
            print(f'Fundo da imagem {sys.argv[1]} removido com sucesso!')
        except Exception as e:
            print(f'Argumentos Inválidos.\nErros: {e}')


    else:
        escolha = askinteger("Escolha como quer usar a ferramenta", 
                                        "Digite 1 para remover o fundo de uma única imagem\n"
                                        "Digite 2 para remover o fundo de várias imagens")
        
        
        if escolha == 1:
            imagem_unica()
        elif escolha == 2:
            imagem_lote()
        else:
            showinfo("Opção inválida.",  "Por favor, escolha 1 ou 2.")
        

if __name__ == "__main__":
    main()

