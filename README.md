# SEL0456 - 2022.2

## Índice
1. [Atividade 1](#a1)
    1. [Preparação](#st1)
    2. [Iniciar Instalador](#st2)
2. [Atividade 2](#a2)
    1. [Subtópico](#st3)
3. [Atividade 3](#a3)
4. [Seminário - Pandas](#s1)
5. [4 - Programação Funcional](#a4)
6. [Teste no Github](#a5)
X. [Tópico X](#aX)
    1. [Subtópico](#stX)

## <a id = "a1"></a>Tutorial: Instalação Debian 11 em Dual Boot

### <a id = "st1"></a>Preparação
#### Baixar Debian e ferramentas necessárias:
- [Debian](https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/) (Link redireciona para versão live para processador 64 bits, pode ser usado o Gnome ou outro de sua preferência)
- [BalenaEtcher](https://www.balena.io/etcher/) (Gravador de imagens no USB)
#### Gravar imagem ISO do Debian em um pendrive com 4GB+
- Abrir BalenaEtcher
- Selecionar imagem baixada
- Selecionar dispositivo USB
- Clicar em Flash!
- Aguardar até concluir
#### Iniciar computador pelo pendrive
- Usar "Boot Menu" ou configurar BIOS para iniciar pelo pendrive
- Realizar configuração inicial de idioma e teclado
#### Redimensionar Partição do Windows
- Verificar conexão com internet
- Clicar com botão direito do mouse, "Resize" e diminuir para ter espaço suficiente para instalação do Linux
- Clicar com botão direito no espaço não alocado e criar nova partição:
	- Usar filesystem EXT4
	- Deixar com 16GB livre (ou o tamanho da memória RAM do PC)
- Clicar com botão direito no espaço não alocado e criar nova partição:
	- Usar filesystem swap
	- Usar espaço livre restante
- SE NÃO PERMITIR A CRIAÇÃO POR LIMITE DE NÚMERO DE PARTIÇÃO
	- Criar uma partição estendida com o tamanho total do espaço disponível para o Linux, e depois voltar para passos de criar partições EXT4 e swap

### <a id = "st2"></a>Iniciar Instalador
- Prosseguir com configurações:
	- Localização (São Paulo)
	- Teclado (Portuguese (BR))
	- Particionamento: Caso existam dados no HD que você quer preservar, é necessário se fazer a partição manualmente, caso não existam dados, pode-se escolher as opções que particionrão o HD automaticamente. Para a partição manual, deve-se verificar se existe espaço disponível para a instalação. Caso não exista, vai ser nbecessário ou apagar uma partição ou encolher uma partição.
		- Caso necessite encolher uma partição, deve-se editar essa partição, podendo escolher o novo tamanho. Com o encolhimento, irá sobrar espaço disponível para as novas partições.
		- Deve-se verificar se existe já uma partição `swap`, caso não exista, é necessário criar uma com o tamanho da RAM do computador, no mínimo.
		- Caso o número de partições finais excedam 4, que é o máximo de partições primárias possíveis, é necessário criar uma partição estendida com tamanho igual ao espaço livre e então, as novas partições devem ser criadas dentro dela.
		- Para a partição com o sistema Debian GNU/Linux, esta deve-se ser criada com o tipo ext4, assinalar opção de formatar e escolher o ponto de montagem em `/`.
		- Ao final do particionamento, deve-se verificar instalação do bootloader (GRUB) na MBR do disco principal (usualmente /dev/sda)
	- Usuário (Criar novo usuário e senha)
	- Sumário (Confirmar informações)
- Aguardar a conclusão da instalação

#### Reiniciar o PC e aproveitar o novo SO.

## <a id = "a2"></a>Atividade 2

O Trabalho número 2 consiste na criação de um repositório no github ou gitlab onde o aluno deverá elaborar um programa para o cálculo do número de Fibonacci de duas maneiras distintas: uma usando um laço (for) e outra utilizando a técnica de recursividade. A técnica de recursividade, de preferência, deverá ser implementada em um branch à parte. O aluno deverá então passar o link do branch para que possa ser avaliado.

-[Atividade 2](https://github.com/matheusvivasr/SEL0456/blob/master/Atividade%202/README.md)
-[Repo Atividade 2](https://github.com/matheusvivasr/sel0456-fibo)

## <a id = "a3"></a>Atividade 3

Programa que troca as vírgulas por ';' em um arquivo de dados.

-[Atividade 3](https://github.com/matheusvivasr/SEL0456/tree/master/Atividade%203)

## <a id = "a4"></a>4 - Programação Funcional

Programa que lê um arquivo com pares de números separados por espaço ou vírgula e produza um arquivo de saída denominado por "output.dat" no format:

Linha n: Fib(x)=X Fact(y)=Y

-[4 - Programação Funcional](https://github.com/matheusvivasr/SEL0456/tree/master/Atividade%203)

## <a id = "a5"></a>Teste no Github
Faça um programa em python para calcular o número de Fibonacci e o fatorial de um número. Elabore um teste automatizado para ler um arquivo com alguns números já pré calculados e comparar com o calculado pelas funções do seu programa Python. O aquivo é o seguinte:

```# fact Fib
1 1 1
2 2 1
4 24 3
9 362880 34
7 5040 13```

Crie um repositório no Github (ou Gitlab) com README.md e LICENSE.txt. Forneça o link do repositório.
Faça o teste em um outro arquivo, logo abaixo, mostrando as linhas com erro:

```# fact Fib
1 1 1
2 2 1
4 30 3
9 362880 32
7 5040 1```

-[Atividade 3](https://github.com/matheusvivasr/SEL0456/tree/master/Atividade%203)
