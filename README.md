<p align="left">
  <picture>
    <source srcset="docs/images/dissig_logo_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/dissig_logo_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/dissig_logo_dark.jpg" alt="tonnetzB" width="1000">
  </picture>
</p>

# **Tonal Structures**<br><small>*for*</small> **Harmonic Motion**<br><small>*between*</small> **Discrete Signals**

Welcome to `disig`, a Python package that allows users to compute and manipulate [...]

## Harmonic movement between discrete signals

### Euler's *tonnetz*
[...]

<p align="center">
  <picture>
    <source srcset="docs/images/euler_tonnetz_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/euler_tonnetz_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/euler_tonnetz_dark.jpg" alt="tonnetzB" width="350">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Tonnetz for discrete audio signals with 36 samples
</p>

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/euler_modern_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/euler_modern_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/euler_modern_dark.jpg" alt="tonnetzB" width="300">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Tonnetz for discrete audio signals with 36 samples
</p>

[...]

### Modern tonnetze

[...]

### Tonnetze for discrete audio signals

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/tonnetz_36_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/tonnetz_36_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/tonnetz_36_dark.jpg" alt="tonnetzB" width="600">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Tonnetz for discrete audio signals with 36 samples
</p>



[...]

### Large-scale structure of discrete tonnetze

In any setting where we have a monoid $M$ actiong on a set $S$, and a subset $X\subset M$, we can form the graph $[S/\!/X]_{\bullet}$ with $$[S/\!/X]_{0}:=\ S\text{\ \ \ \ \ \ and\ \ \ \ \ \ }[S/\!/X]_{1}:=\ X\times S,$$ where the *source* and *target* maps $$\partial^{1}_0,\partial^{1}_1:\ [S/\!/X]_1\!\!\longrightarrow[S/\!/X]_{0}$$ that interpret each pair $(\chi,\ s)\in X\times S=[S/\!/X]_1$ as the arrow $$s\ \!\xrightarrow{\ \ \ \chi\ \ \ }\ \!\chi s.$$

In general, it's hard to "*zoom out from* $[S/\!/X]_{\bullet}$" to say anything substantuve about the large-scale structure of this graph. That said, there are many special casses where we can say a lot about the strucutre of this graph. In the special case that 
- $S=\mathbb{Z}/\ell\mathbb{Z}$, the set of integers modulo some positive integer $\ell$,
- $M=\mathbb{Z}/\ell\mathbb{Z}$ equipped with its mutliplicative structure,

we can say quite a bit about the strucutre of $[S/\!/M]_{\bullet}$. The positive integer $\ell$ has unique prime factorization $$\ell\ =\ p_{1}^{e_1}p_{2}^{e_2}\cdots p_{r}^{e_r}$$ The graph $[S/\!/M]_{\bullet}$ contains a subgraph $\text{Div}(\ell)_{\bullet}$ with $$\text{Div}(\ell)_{0}:=\{d\in\mathbb{Z}_{>0}:d\text{\ divides\ }\ell\}$$ and $$\text{Div}(\ell)_{1}:=\ \{d\xrightarrow{\ \ \ p\ \ }pd:\ pd\text{\ divides\ }\ell,\ p\text{\ prime}\}$$

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/1_to_16_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/1_to_16_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/1_to_16_dark.jpg" alt="tonnetzB" width="420">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
    [...CAPTION...]
</p>

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/1_to_36_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/1_to_36_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/1_to_36_dark.jpg" alt="tonnetzB" width="230">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
    [...CAPTION...]
</p>

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/1_to_60_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/1_to_60_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/1_to_60_dark.jpg" alt="tonnetzB" width="300">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
    [...CAPTION...]
</p>

[...]


## 📦 Project Structure
```bash
.
├── docs/ # External references, images, and LaTeX sources
├── src/dissig/ # Python package source code
├── tests/ # Unit tests
├── pyproject.toml # Project configuration for PDM
├── requirements.txt # Compatibility requirements (optional)
└── README.md # This file
```

## 🚀 Installation

Using [PDM](https://pdm.fming.dev):

```bash
pdm install
```
Or using pip (if necessary):
```bash
pip install -e .
```

## 🔧 Usage
Example usage:

```python
from dissig.core import run_pipeline

data = ...         # Load your input
config = {...}     # Define configuration
result = run_pipeline(data, config)
```

## 🧪 Running Tests
```bash
pdm run pytest
```

## 📄 Documentation
[...]
- Images: docs/images/
- LaTeX files: docs/tex/
- External references: docs/external/

## 🛠 Development
Set up your development environment:
```bash
pdm install --dev
```
To enable import resolution in VSCode:

```jsonc
// .vscode/settings.json
{
  "python.analysis.extraPaths": ["./src"]
}
```

## 📝 License
This project is licensed under the terms of the MIT License.