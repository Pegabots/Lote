
# Contribuindo para o projeto

Olá! Obrigado pelo interesse em contribuir com essa Aplicação. Esse repositório implementa o Pegabot Lote, capaz de buscar dados por meio da API do Twitter e executar análise pelo Motor do Pegabot, retornando um resultado individual de cada perfil sobre sua chance de ser automatizado em um arquivo csv.

Reunimos aqui as diretrizes para ajudá-lo a descobrir onde você pode ser mais útil.

## Índice

0. [Tipos de contribuições que estamos procurando](#tipos-de-contribuições-que-procuramos)
0. [Regras básicas e expectativas](#regras-básicas-e-expectativas)
0. [Como contribuir](#como-contribuir)
0. [Configurando seu ambiente](#configurando-seu-ambiente)
0. [Comunidade](#comunidade)

## Tipos de contribuições que procuramos

O Pegabot Lote aceita contribuições que:
* Tornem sua execução mais eficiente
* Documente o funcionamento da ferramenta
* Corrijam possíveis bugs

Interessado em contribuir neste projeto? Leia!

## Regras básicas e expectativas

Antes de começarmos, aqui estão algumas coisas que esperamos de você (e que você deve esperar dos outros):

* Seja gentil e atencioso em suas conversas sobre este projeto. Todos nós viemos de diferentes origens e projetos, o que significa que provavelmente temos diferentes perspectivas sobre "como o código aberto é feito". Tente ouvir os outros em vez de convencê-los de que seu caminho está correto.
* Este projeto conta com um [Código de Conduta do Contribuidor](./CODE_OF_CONDUCT.md). Ao participar deste projeto, você concorda em cumprir seus termos.

## Como contribuir

Se você quiser contribuir, comece pesquisando em [issues](https://github.com/caminhodoprojeto/issues) e [pull requests](https://github.com/caminhodoprojeto/pulls) para ver se alguém levantou uma ideia ou pergunta semelhante.

Se você não vir sua ideia listada e achar que ela se encaixa nos objetivos deste guia, abra uma nova issue.

## Configurando seu ambiente

### Instalação
  
Este código foi executado com `python 3.9.4` e `pip 20.2.3`.

```sh
git clone https://github.com/Pegabots/Lote.git
```
  
### Entre na pasta do projeto:

```sh
cd Lote
```

### Crie seu ambiente virtual e entre nele:

```sh
python -m venv venv
source venv/bin/activate
```
***

Abra a pasta da instalação e coloque os dados de acesso da sua chave da API do twitter no arquivo 'example.env'. Depois renomeie esse arquivo para '.env' (somente a extensão).

***

### Instale as bibliotecas necessárias para a execução do projeto:

```sh
pip install -r requirements.txt
```

Insira o arquivo que contém os handles dos usuários a serem analisados na pasta Dados. Nesse arquivo, cada linha deve conter apenas o handle de um usuário. Nomeie o arquivo como 'handles_termo.csv' (onde termo pode ser qualquer termo que te ajude a identificar aquele arquivo).

### Por fim, execute utilizando o seguinte comando:

```sh
python main.py termo
```

Onde 'termo' é o termo que você colocou no nome do arquivo acima descrito.

***

Pronto! Agora é só aguardar. A execução leva cerca de 2 segundos para executar cada análise devido as limitações de acesso da API do Twitter. Sendo assim, em observações empíricas, é possível analisar cerca de 900 perfis por hora utilizando esse código.

***

## Comunidade

As discussões sobre o projeto ocorrem nas seções [Issues](https://github.com/caminhodoprojeto/issues) e [Pull Requests](https://github.com/caminhodoprojeto/pulls). Qualquer pessoa é bem-vinda para participar dessas conversas.

Sempre que possível, não leve essas conversas para canais privados, inclusive entrando em contato diretamente com os mantenedores. Manter a comunicação pública significa que todos podem se beneficiar e aprender com a conversa.

Esse arquivo foi elaborado com base [neste](https://github.com/github/opensource.guide/blob/main/CONTRIBUTING.md) repositório.
