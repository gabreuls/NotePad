# Bloco de Notas Customizado em Python

Este é um simples **Bloco de Notas** criado em Python usando **Tkinter**. Ele permite que você digite apenas letras do alfabeto, espaço, enter e backspace, bloqueando todas as outras teclas. O bloco de notas também permite salvar o conteúdo em arquivos de texto.
P.S.: A finalidade por trás dessa aplicação é porque tenho 2 sobrinho pequenos que gostam de mexer no computador.(hehe).

## Funcionalidades
- Aceita apenas letras do alfabeto, espaço, enter e backspace.
- Bloqueia todas as outras teclas.
- Permite salvar o conteúdo em arquivos `.txt` com o atalho `Ctrl + S`.

## Pré-requisitos

Para executar o código Python ou gerar o executável, você precisará do seguinte:

- **Python 3.x** instalado no sistema.
- As bibliotecas Python:
  - `tkinter` (instalado por padrão com Python).
  - `PyInstaller` (para gerar o executável).

### Instalando o PyInstaller

Se você ainda não tem o **PyInstaller** instalado, execute o seguinte comando no terminal:

```bash
pip install pyinstaller
Como Executar a Aplicação Python
1. Executando o Script Python
Você pode executar diretamente o script Python utilizando o seguinte comando:

bash
Sempre exibir os detalhes

Copiar código
python notepad.py
2. Gerando um Executável
Caso você queira criar um executável para rodar o programa sem precisar abrir o código, siga os passos abaixo:

Navegue até o diretório do projeto:

bash
Sempre exibir os detalhes

Copiar código
cd caminho/para/o/diretorio
Utilize o PyInstaller para gerar um executável:

bash
Sempre exibir os detalhes

Copiar código
pyinstaller --onefile notepad.py
O executável será gerado na pasta dist, dentro do diretório do projeto.

Para rodar o executável:

Windows: Dê um duplo clique no arquivo notepad.exe na pasta dist.
Linux/macOS: Execute o comando:
bash
Sempre exibir os detalhes

Copiar código
./dist/notepad
Atalhos de Teclado
Ctrl + S: Salvar o conteúdo em um arquivo .txt. 