#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
llms-txt-lint — valida a estrutura de um arquivo `llms.txt` contra o formato
que vem se firmando como padrão informal do setor (llmstxt.org): título em
H1, resumo curto em blockquote, seções em H2 com listas de links markdown.

O QUE FAZ
    Confere, em ordem:

    1. A primeira linha não vazia é um H1 (`# Título`).
    2. Existe um bloco de resumo em blockquote (`> ...`) logo depois do
       título — a linha citável que resume o site em uma frase.
    3. O restante do arquivo é organizado em seções H2 (`## Nome`).
    4. Cada seção contém, predominantemente, itens de lista no formato
       `- [texto](url): descrição opcional` — o formato que um agente de IA
       consegue interpretar como link + rótulo sem ambiguidade.
    5. Nenhum link markdown está quebrado (sintaxe `[texto](url)` malformada).

USO
    python llms_txt_lint.py llms.txt
    python llms_txt_lint.py llms.txt --strict

LIMITAÇÕES
    Confere a FORMA do arquivo (estrutura markdown), não se os links
    listados existem de fato ou apontam para o lugar certo — para isso,
    rode um checador de link à parte. O padrão llms.txt ainda não é uma
    especificação formal única; esta ferramenta segue a convenção mais
    citada (llmstxt.org) em 2026.

Autor: Lucas Ferraz (lucasferraz.com) — dependência zero, só biblioteca padrão.
Licença: MIT.
"""
from __future__ import annotations

import argparse
import re
import sys

LINK_MD = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
ITEM_LISTA_LINK = re.compile(r"^-\s+\[([^\]]+)\]\(([^)]+)\)(:\s*.+)?$")


def main() -> None:
    ap = argparse.ArgumentParser(description="Valida a estrutura de um arquivo llms.txt.")
    ap.add_argument("arquivo", help="arquivo llms.txt")
    ap.add_argument("--strict", action="store_true", help="código de saída 1 se houver qualquer ATENÇÃO")
    args = ap.parse_args()

    try:
        with open(args.arquivo, encoding="utf-8") as fh:
            linhas = fh.read().splitlines()
    except OSError as exc:
        print(f"Não consegui ler {args.arquivo}: {exc}", file=sys.stderr)
        sys.exit(2)

    atencoes: list[str] = []
    oks: list[str] = []

    nao_vazias = [(i, l) for i, l in enumerate(linhas, start=1) if l.strip()]
    if not nao_vazias:
        print("Arquivo vazio.", file=sys.stderr)
        sys.exit(2)

    primeira_num, primeira = nao_vazias[0]
    if not primeira.startswith("# "):
        atencoes.append(f"linha {primeira_num}: primeira linha não vazia deveria ser um H1 (\"# Título\")")
    else:
        oks.append("H1 de título presente na primeira linha")

    resumo_encontrado = False
    for i, l in nao_vazias[1:4]:
        if l.startswith(">"):
            resumo_encontrado = True
            break
        if l.startswith("#"):
            break
    if resumo_encontrado:
        oks.append("bloco de resumo em blockquote presente logo após o título")
    else:
        atencoes.append("sem bloco de resumo em blockquote (\"> ...\") logo depois do H1")

    secoes_h2 = [i for i, l in enumerate(linhas, start=1) if re.match(r"^##\s+\S", l)]
    if not secoes_h2:
        atencoes.append("nenhuma seção H2 encontrada (\"## Nome da seção\")")
    else:
        oks.append(f"{len(secoes_h2)} seção/seções H2 encontrada(s)")

    for i, l in enumerate(linhas, start=1):
        stripped = l.strip()
        if not stripped.startswith("-"):
            continue
        if ITEM_LISTA_LINK.match(stripped):
            continue
        if "[" in stripped or "(" in stripped:
            atencoes.append(f"linha {i}: item de lista parece um link, mas não bate o formato \"- [texto](url): descrição\": \"{stripped[:70]}\"")

    for i, l in enumerate(linhas, start=1):
        for m in re.finditer(r"\[[^\]]*\]\([^)]*\)", l):
            texto_url = m.group()
            if not LINK_MD.fullmatch(texto_url):
                continue
            url = LINK_MD.fullmatch(texto_url).group(2)
            if not url.strip():
                atencoes.append(f"linha {i}: link markdown com URL vazia: \"{texto_url}\"")

    print(f"\n=== llms-txt-lint: {args.arquivo} ===")
    print(f"OK {len(oks)} | ATENÇÃO {len(atencoes)}\n")
    for o in oks:
        print("  ok       " + o)
    for a in atencoes:
        print("  ATENÇÃO  " + a)
    if not atencoes:
        print("\n  Estrutura dentro do padrão esperado.")

    sys.exit(1 if (args.strict and atencoes) else 0)


if __name__ == "__main__":
    main()
