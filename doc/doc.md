# Documentação do DevFlow

## Arquitetura Geral
O DevFlow é um sistema modular que oferece diversas funcionalidades, como gerenciamento de projetos, execução de inteligência artificial local, formatação de dispositivos USB para boot e organização de arquivos. A seguir, está a explicação detalhada de cada módulo e suas funções.

---

### Arquivo Principal - `index.py`
Este é o ponto de entrada do programa. Aqui, o DevFlow exibe o menu principal e direciona o usuário para a funcionalidade desejada.

#### Funções no `index.py`
- **Start()**
  - Exibe o menu principal para o usuário, permitindo escolher uma função.
  - Utiliza um loop para capturar a entrada do usuário e chamar as funções adequadas com base na opção selecionada.

- **Run_IA()**
  - Configura e executa a IA. Chama a função `Config_IA` ou `Ollaama_Run_IA` do módulo `IA`.
  - Exibe um menu adicional se o usuário precisar configurar a IA antes de rodá-la.

- **Formart_Boot_Disk()**
  - Formata um dispositivo USB como um disco de boot, chamando `formart()` do módulo `Format_Script.py`.
  - Verifica o número do disco para garantir que o dispositivo correto será formatado.

- **Start_Progect()**
  - Inicializa a seção de gerenciamento de projetos, chamando as funções em `Manege_Progect`.
  - Apresenta opções como criar, carregar ou gerenciar projetos.

---

### Ferramentas Auxiliares - `tool.py`
Este módulo fornece funções utilitárias que facilitam a manipulação de arquivos e pastas, limpeza do sistema e outras operações.

#### Funções no `tool.py`
- **clear_screen()**
  - Limpa a tela do terminal.
  - No Windows, usa o comando `cls`; em outros sistemas, usa `clear`.

- **Organizador_De_Arquivo()**
  - Organiza os arquivos em pastas, movendo-os com base em suas extensões.
  - Usa o dicionário `paths` de `data.py` para decidir a pasta de destino para cada extensão de arquivo.

- **Clear_Temp()**
  - Limpa a pasta de arquivos temporários do sistema.
  - Usa `os.environ` para localizar o diretório de arquivos temporários e exclui os arquivos e subpastas nele contidos.

- **Create_Folder(directory_path, folder_name)**
  - Cria uma nova pasta no diretório especificado.
  - Checa se a pasta já existe antes de criá-la para evitar duplicação.

- **Windows_Verify()**
  - Verifica e repara arquivos corrompidos do sistema no Windows, usando o comando `sfc /scannow`.
  - Executa um comando do terminal e aguarda a conclusão, útil para corrigir problemas de integridade do sistema.

- **is_admin()**
  - Verifica se o script está sendo executado com privilégios administrativos.
  - Usa `ctypes` para verificar as permissões e retorna `True` se for administrador, `False` caso contrário.

- **Retun_reponse(url)**
  - Envia uma solicitação GET para uma URL e retorna a resposta.
  - Pode ser usado para verificar a conectividade ou obter dados de uma API externa.

---

### Configurações e Dados Globais - `data.py`
Este módulo armazena as variáveis globais usadas no projeto, principalmente em uma `dataclass`.

#### `dataclass` no `data.py`
- **Classe data**
  - **paths**: Dicionário que define onde cada tipo de arquivo deve ser armazenado com base em sua extensão.
  - **Projetcs**: Lista de projetos atualmente carregados ou criados no DevFlow.
  - **OS_client**: Armazena informações sobre o sistema operacional do cliente, ajudando a adaptar funções específicas do sistema.

---

### Inteligência Artificial - `IA.py`
Este módulo gerencia a execução e configuração da IA local, permitindo ajustar a memória usada.

#### Funções no `IA.py`
- **Ollaama_Run_IA()**
  - Executa a IA local "Llama 3".
  - Checa se a IA está instalada corretamente antes de iniciar a execução.

- **Config_IA(memory_usage)**
  - Permite ao usuário definir a quantidade de memória RAM a ser utilizada pela IA.
  - Ajusta a configuração com base nos recursos do computador, evitando sobrecarregar o sistema.

---

### Formatação de Pendrive para Boot - `Format_Script.py`
Esse módulo contém uma função para formatação de um dispositivo USB como um disco de boot.

#### Funções no `Format_Script.py`
- **formart(nun_disk)**
  - Cria um arquivo de script temporário com comandos `diskpart`.
  - Limpa o dispositivo e o formata com o sistema de arquivos FAT32, configurando-o para ser um dispositivo de boot.

---

### Gerenciamento de Projetos - `Manege_Progect`
Este diretório contém arquivos para a criação e manipulação de projetos. As funções permitem adicionar, carregar e gerenciar listas de tarefas associadas a cada projeto.

#### Funções em `Manege_Progect`
- **mange_project_main.py**:
  - Função principal que orquestra o gerenciamento de projetos e interage com `projectclass.py`.
  - Exibe um menu com opções para criar, carregar ou gerenciar projetos.

- **projectclass.py**:
  - Define a classe `Project`, que representa um projeto individual no DevFlow.

#### Atributos da Classe `Project`
- **name**: Nome do projeto.
- **description**: Descrição breve do projeto.
- **start_time**: Data/hora de início do projeto.
- **task_list**: Lista de tarefas associadas ao projeto.
- **language**: Linguagem de programação ou tecnologia principal usada no projeto.

#### Métodos da Classe `Project`
- **Add_Task(task_name, task_description)**: Adiciona uma nova tarefa ao `task_list` do projeto.
- **Complete_Task(task_id)**: Marca uma tarefa específica como concluída.

---

### Fluxo Geral do Código
O fluxo de execução no DevFlow segue a seguinte ordem:

1. `index.py` executa o `Start()` para exibir o menu principal e capturar a entrada do usuário.
2. Dependendo da escolha do usuário:
   - Organização de Arquivos (`tool.Organizador_De_Arquivo`).
   - Limpeza de Diretórios Temporários (`tool.Clear_Temp`).
   - Execução da IA (`IA.Ollaama_Run_IA`).
   - Formatação de Pendrive (`Format_Script.formart`).
   - Gerenciamento de Projetos (`Manege_Progect.mange_project_main`).
3. **Retorno ao Menu**: Após cada operação, o DevFlow retorna ao menu principal (`Start()`), permitindo ao usuário escolher outra função ou encerrar o programa.
