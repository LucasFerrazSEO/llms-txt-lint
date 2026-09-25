[English](README.md) · **Português (Brasil)**

# llms-txt-lint

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`llms-txt-lint` é uma ferramenta de linha de comando gratuita e de código
aberto que valida a estrutura de um arquivo `llms.txt` contra a convenção
que vem se firmando como padrão do setor ([llmstxt.org](https://llmstxt.org)):
título em H1, resumo curto em blockquote, seções em H2 com listas de links
markdown. Roda localmente, só com a biblioteca padrão do Python.

## Sumário

- [Contexto](#contexto)
- [O que a ferramenta verifica](#o-que-a-ferramenta-verifica)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Perguntas frequentes](#perguntas-frequentes)
- [Limitações](#limitações)
- [Como contribuir](#como-contribuir)
- [Autor](#autor)
- [Licença](#licença)

## Contexto

`llms.txt` é um arquivo na raiz do site pensado para dar a um agente de IA
um mapa direto do conteúdo, em markdown, sem o ruído de navegação e
interface de uma página HTML normal. Como o formato ainda não é uma
especificação única e obrigatória, arquivos reais divergem bastante. Esta
ferramenta confere a estrutura contra a convenção mais citada.

## O que a ferramenta verifica

1. A primeira linha não vazia é um H1 (`# Título`).
2. Existe um bloco de resumo em blockquote (`> ...`) logo depois do
   título.
3. O arquivo tem ao menos uma seção H2 (`## Nome`).
4. Itens de lista que parecem link seguem o formato
   `- [texto](url): descrição opcional`.
5. Nenhum link markdown com URL vazia.

## Requisitos

Python 3.9 ou mais recente. Só biblioteca padrão, sem dependência externa.

## Instalação

```bash
git clone https://github.com/LucasFerrazSEO/llms-txt-lint.git
cd llms-txt-lint
```

## Uso

**1. Rode contra o seu arquivo `llms.txt`.**

```bash
python llms_txt_lint.py llms.txt
```

**2. Leia o relatório.** Exemplo real, de um `llms.txt` bem formado:

```
=== llms-txt-lint: llms.txt ===
OK 3 | ATENÇÃO 0

  ok       H1 de título presente na primeira linha
  ok       bloco de resumo em blockquote presente logo após o título
  ok       1 seção/seções H2 encontrada(s)

  Estrutura dentro do padrão esperado.
```

Quando um item de lista parece link mas não bate o formato esperado, ou um
link markdown tem URL vazia, a ferramenta aponta a linha exata do
problema. A falta do blockquote de resumo aparece como alerta, sem número
de linha.

**3. Baixe o `llms.txt` de qualquer site e teste direto**, se quiser
comparar com o seu:

```bash
curl -s https://exemplo.com/llms.txt -o llms-exemplo.txt
python llms_txt_lint.py llms-exemplo.txt
```

**4. Use `--strict` em CI/CD**, para bloquear publicação de um `llms.txt`
fora do padrão. Com `--strict`, o código de saída é 1 se houver qualquer
alerta:

```bash
python llms_txt_lint.py llms.txt --strict
```

## Perguntas frequentes

**llms-txt-lint é realmente grátis?**
Sim, código aberto sob licença MIT.

**A ferramenta confirma se meus links funcionam?**
Não. Confere a forma do arquivo (sintaxe markdown, estrutura de seção),
não se os links listados existem de fato ou apontam para o lugar certo.

**Meu site precisa de um llms.txt?**
Não existe hoje uma confirmação oficial de que llms.txt afeta ranqueamento
ou citação. É uma convenção adotada por parte do setor como sinalização
adicional, não uma exigência documentada por nenhum provedor de IA.

## Limitações

Confere a forma do arquivo, não se os links listados existem de fato ou
apontam para o lugar certo. O padrão llms.txt não é uma especificação
formal única em 2026. Esta ferramenta segue a convenção mais citada, que
pode mudar.

## Como contribuir

Relatos de erro e sugestões são bem-vindos pelas [Issues do GitHub](https://github.com/LucasFerrazSEO/llms-txt-lint/issues).

## Autor

[Lucas Ferraz](https://lucasferraz.com) é especialista em SEO, criação de sites e Generative Engine Optimization e fundador da [Lucas Ferraz SEO](https://lucasferrazseo.com).

## Licença

MIT. Veja o arquivo [LICENSE](LICENSE).
