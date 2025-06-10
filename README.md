<p style="font-size: 1pt;">
  <picture style="font-size: 12em;">
    <source srcset="docs/images/dissig_logo_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/dissig_logo_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/dissig_logo_dark.jpg" alt="DisSig Logo"
    style="height: 16em;">
  </picture>
</p>

# **Tonal Structures**<br><small>*of*</small> **Harmonic Motion**<br><small>*between*</small> **Discrete Signals**

## Harmonic movement between discrete signals

### Euler's *tonnetz*
[...]

<figure style="font-size: 1pt; text-align: center;">
  <picture style="font-size: 12em;">
    <source srcset="docs/images/euler_tonnetz_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/euler_tonnetz_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/euler_tonnetz_dark.jpg" alt="Euler tonnetz" style="height: 11em;">
  </picture>
  <figcaption style="font-size: 12pt; margin-top: 0.5em;">Euler's tone network ("tonnetz") diagram</figcaption>
</figure>



[...]

### Tonnetze

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