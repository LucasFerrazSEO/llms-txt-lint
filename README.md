**English** · [Português (Brasil)](README.pt-BR.md)

# llms-txt-lint

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`llms-txt-lint` is a free, open source command-line tool that validates the
structure of an `llms.txt` file against the convention that is becoming the
industry default ([llmstxt.org](https://llmstxt.org)): an H1 title, a short
summary in a blockquote, and H2 sections with lists of markdown links. It
runs locally with the Python standard library only.

## Contents

- [Background](#background)
- [What it checks](#what-it-checks)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [FAQ](#faq)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Background

`llms.txt` is a file at the site root meant to give an AI agent a direct
map of the content, in markdown, without the navigation and interface
noise of a normal HTML page. The format is not yet a single, mandatory
specification, so real-world files vary a lot. This tool checks the
structure against the most cited convention.

## What it checks

1. The first non-empty line is an H1 (`# Title`).
2. A summary block in a blockquote (`> ...`) comes right after the title.
3. The file has at least one H2 section (`## Name`).
4. List items that look like links follow the format
   `- [text](url): optional description`.
5. No markdown link has an empty URL.

## Requirements

Python 3.9 or newer. Standard library only, no external dependencies.

## Installation

```bash
git clone https://github.com/LucasFerrazSEO/llms-txt-lint.git
cd llms-txt-lint
```

## Usage

The tool prints its report in Brazilian Portuguese.

**1. Run it against your `llms.txt` file.**

```bash
python llms_txt_lint.py llms.txt
```

**2. Read the report.** Real sample output from a well-formed `llms.txt`:

```
=== llms-txt-lint: llms.txt ===
OK 3 | ATENÇÃO 0

  ok       H1 de título presente na primeira linha
  ok       bloco de resumo em blockquote presente logo após o título
  ok       1 seção/seções H2 encontrada(s)

  Estrutura dentro do padrão esperado.
```

When a list item looks like a link but does not match the expected format,
or a markdown link has an empty URL, the tool points to the exact line. A
missing summary blockquote is reported as a warning without a line number.

**3. Download any site's `llms.txt` and test it**, if you want to compare
it with yours:

```bash
curl -s https://exemplo.com/llms.txt -o llms-exemplo.txt
python llms_txt_lint.py llms-exemplo.txt
```

**4. Use `--strict` in CI/CD** to block publishing an `llms.txt` that is
off the convention. With `--strict`, the exit code is 1 if there is any
warning:

```bash
python llms_txt_lint.py llms.txt --strict
```

## FAQ

**Is llms-txt-lint really free?**
Yes. It is open source under the MIT license.

**Does the tool confirm that my links work?**
No. It checks the shape of the file (markdown syntax, section structure),
not whether the listed links exist or point to the right place.

**Does my site need an llms.txt?**
There is no official confirmation today that llms.txt affects rankings or
citations. It is a convention adopted by part of the industry as an extra
signal, not a requirement documented by any AI provider.

## Limitations

It checks the shape of the file, not whether the listed links exist or
point to the right place. The llms.txt standard is not a single formal
specification in 2026. This tool follows the most cited convention, which
may change.

## Contributing

Bug reports and suggestions are welcome through [GitHub Issues](https://github.com/LucasFerrazSEO/llms-txt-lint/issues).

## Author

[Lucas Ferraz](https://lucasferraz.com) is an SEO, website development and Generative Engine Optimization specialist and the founder of [Lucas Ferraz SEO](https://lucasferrazseo.com).

## License

MIT. See [LICENSE](LICENSE).
