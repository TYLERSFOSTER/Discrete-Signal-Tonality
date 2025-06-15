<p align="left">
  <picture>
    <source srcset="docs/images/dissig_logo_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/dissig_logo_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/dissig_logo_dark.jpg" alt="tonnetzB" width="1000">
  </picture>
</p>

# **Tonal Structures**<br><small>*for*</small> **Harmonic Motion**<br><small>*between*</small> **Discrete Signals**

Welcome to `disig`, a Python package that allows users to compute and manipulate [...]

## *TODO*s
- Finish `./README.md`
- Generate examples with accompanying diagrams
- pylint `./tests`
- Finish TeX documentation
## 

## Harmonic movement between discrete signals

### Euler's *tonnetz*
A [*tonnetz*](https://en.wikipedia.org/wiki/Tonnetz) (German for "*tone network*," with plural *tonnetze*) is a type of diagram that depicts the intervalic inte-relationship between a collection of pitches, pitch classes, or even chords. One of the first known examples of a tonnetz is a drawing that the mathematician [Leonard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) included in a 1739 treatise on music theory.

<p align="center">
  <picture>
    <source srcset="docs/images/euler_tonnetz_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/euler_tonnetz_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/euler_tonnetz_dark.jpg" alt="tonnetzB" width="350">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Euler's tonnetz
</p>

Today, we tend to depict this same tonnetze as a grid network. This tonnetz depicts the relationship between the 12 pitch classes in a 12-tone equaltempered tuning when we move along the two important diatonic intervals P5 (a *perfect fifth*) and M3 (m *major third*):

<p align="center">
  <picture>
    <source srcset="docs/images/euler_modern_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/euler_modern_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/euler_modern_dark.jpg" alt="tonnetzB" width="550">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Our modernized version of Euler's tonnetz.
</p>

Here, we depict the tonnetz as a grid network, instead of Euler's original system of cascading brackets, but the content is essentially identical. We've added dotted arrows along the bottom edges of the diagram to indicate how it loops back along itself along P5 and M3 intervals.

The diagram is interesting from a music theoretical perspecitive because to exhibits lots of important diatonic-based musical phenomena in striking and often quite suggestive geometric patterns. To give just one example, all major and minor triads appear in this tonnetz as [span or cospan diagrams](https://en.wikipedia.org/wiki/Span_(category_theory)):

<p align="center">
  <picture>
    <source srcset="docs/images/triads_in_tonnetz_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/triads_in_tonnetz_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/triads_in_tonnetz_dark.jpg" alt="tonnetzB" width="550">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Major and minor triads appear in Euler's tonnetz as spans and copsans
</p>

### Modern tonnetze

[...]
## *Tonality* for discrete audio signals

### Tonnetze for discrete audio signals

[...Play example...]

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/scaling_signals_continuous_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/scaling_signals_continuous_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/scaling_signals_continuous_dark.jpg" alt="tonnetzB" width="600">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Tonnetz for discrete audio signals with 36 samples
</p>

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/scaling_signals_discrete_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/scaling_signals_discrete_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/scaling_signals_discrete_dark.jpg" alt="tonnetzB" width="700">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Tonnetz for discrete audio signals with 36 samples
</p>

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/tonnetz_36_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/tonnetz_36_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/tonnetz_36_dark.jpg" alt="tonnetzB" width="700">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Tonnetz for discrete audio signals with 36 samples
</p>

[...]

## Large-scale structure of discrete tonnetze

[...]

### Orbits under the unit group from natural clusters

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/36_with_clusters_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/36_with_clusters_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/36_with_clusters_dark.jpg" alt="tonnetzB" width="650">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
    [...CAPTION...]
</p>

[...]

### Orbit cluster are arranged along divisor lattice

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

<p align="center">
  <picture>
    <source srcset="docs/images/2-3-5-7_in_35_dark.png" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/2-3-5-7_in_35_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/2-3-5-7_in_35_dark.png" alt="tonnetzB" width="530">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
    [...CAPTION...]
</p>

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/2-3-5-7_in_36_dark.png" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/2-3-5-7_in_36_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/2-3-5-7_in_36_dark.png" alt="tonnetzB" width="490">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
    [...CAPTION...]
</p>

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/2-3-5-11-13_in_216_dark.png" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/2-3-5-11-13_in_216_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/2-3-5-11-13_in_216_dark.png" alt="tonnetzQ" width="800">
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