<p align="left">
  <picture>
    <source srcset="docs/images/dissig_logo_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/dissig_logo_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/dissig_logo_dark.jpg" alt="tonnetzB" width="1000">
  </picture>
</p>

# **Tonal Structures**<br><small>*for*</small> **Harmonic Motion**<br><small>*between*</small> **Discrete Signals**
- **§0.** [Welcome](#tonal-structures)
- **§1.** [Harmonic movement between discrete signals](#harmonic-movement-between-discrete-signals)
- **§2.** [Installation and Setup](#-installation-and-setup)

Welcome to `disig`, a Python package for exploring the tonal geometry of discrete periodic audio signals.

Inspired by Euler’s original Tonnetz and its modern reinterpretations, disig extends these structures to the digital domain—where time is sampled, frequencies are modular, and multiplication replaces dilation.

At the core of this project is a categorical and signal-theoretic perspective on harmony, treating musical intervals as modular rescalings and organizing them into richly structured networks. These discrete tonnetze visualize the harmonic motion between audio signals under arithmetic transformations, revealing patterns that echo deep number-theoretic symmetries.

The underlying structure is a manifestation of a category of representations, where signals transform functorially under modular arithmetic operations. Tonnetz are diagrams of morphisms in this category that encode how spectral content behaves under group actions. This representation-theoretic framing situates tonal motion within a broader categorical picture: musical intervals and harmonic movement, and larger tonal structures all emerge from group actions on spectral data.

The library includes:
  - Tools for generating and analyzing Tonnetz diagrams over arbitrary moduli
  - Visualizers for arithmetic and geometric clusters in signal space
  - Audio synthesis utilities for testing tonal structures directly via WAV playback

Whether you're a theorist, signal processing researcher, or just curious about how number theory meets timbre, disig provides an experimental playground for navigating the space of harmonic motion in modular time.

## *TODO*s
- Finish `./README.md`
- separate visualization into two cases, one that can cluster and one that's `"neato"`
- Generate examples with accompanying diagrams
- Analyze FT and STFT of step-realization of discrete audio signals
## 

# 1. Harmonic movement between discrete signals
- **1.1** [Tonnetze for continuous signals](##tonnetez-for-continuous-signals)
  - **1.1.1** [Euler's *tonnetz*](###eulers-tonnetz)
  - **1.1.2** [Modern tonnetze](###modern-tonnetz)
- **1.2** [*Tonality* for discrete audio signals](##tonality-for-discrete-audio-signals)
  - **1.2.1** [Musical intervals for discrete audio signals](###musical-intervals-for-discrete-audio-signals)
  - **1.2.2** [Tonnetze for discrete audio signals](###tonnetze-for-discrete-audio-signals)
- **1.3** [Large-scale structure of discrete tonnetze](##large-scale-structure-of-discrete-tonnetze)
  - **1.3.1** [Orbits under the unit group from natural clusters](###orbits-under-the-unit-group-from-natural-clusters)

## Tonnetze for continuous signals

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
  A modernized version of Euler's tonnetz.
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
  Major and minor triads appear in our tonnetz as wedges (∧) and vees (∨), respectively
</p>

### Modern tonnetze
Tonnetze became an important tool to developments in [(musical) set theory](https://en.wikipedia.org/wiki/Set_theory_(music)) and in [neo-Riemann theory](https://en.wikipedia.org/wiki/Neo-Riemannian_theory). For exemplary use of tonnetz in musical analysis, see:
- Dmitri Tymoczko. *A Geometry of Music: Harmony and Counterpoint in the Extended Common Practice*. Oxford Studies in Music Theory. Oxford University Press, March 2011. 480 pages.
- Richard Cohn. *Audacious Euphony: Chromatic Harmony and the Triad’s Second Nature.* Oxford Studies in Music Theory. Oxford University Press, January 2012. 256 pages.
- Edward Gollin and Alexander Rehding, editors. *The Oxford Handbook of Neo-Riemannian Music Theories*. Oxford Handbooks. Oxford University Press, May 2014. 632 pages.

The general pattern in all of this work is a partial import, into music theory, of category theoretical diagrams coming from representation theory. Musical intervals, harmonic movement, and larger tonal structures all emerge from the action of the multiplicative monoid of integers $\mathbb{Z}$ on representations of the circle group $\mathbb{S}^{1}$.

Neo-Riemannian theory generalizies tonnetze so that they model transformations between not just pitches, but between chords and more general musical datastructures. This use of tonnetze abstracts away from [common practice](https://en.wikipedia.org/wiki/Common_practice_period) tonal function and voice-leading, and some reject this development as overly formal and historically detached. But much of this suspicion stems from a misunderstanding of the depth of insight these tools offer. Far from being mere abstractions, tonnetze reveal profound geometries underlying harmonic motion — geometries that remain relevant even beyond traditional tonal music.

Embracing this perspective, we explore the tonnetz not as a historical artifact or static diagram, but as a dynamic analytic and generative tool for navigating the musical content of signals themselves.

## *Tonality* for discrete audio signals

### Musical intervals for discrete audio signals

We can understand the edges in our modernized version of Euler's tonnetz as *multiplication* operations. Indeed, moving up a perfect fifth corresponds to rescaling playback speed of a continuous audio signal $f(t)$ by a factor of 3/2, i.e., $f(t)\mapsto f(3t/2)$. Likewise, moving up a major third corresponds to rescaling the playback speed of our continuous audio signal by a factor of 5/4, i.e., $f(t)\mapsto f(5t/4)$.

 If we impose [octave equivalence](https://en.wikipedia.org/wiki/Octave#Equivalence), then we ignore all factors of 2 when we rescale playback speed. Up to octave equivalence, movement up a perfect fifth amounts to rescaling the playback speed by any factor of 3, and movement up a major third amounts to rescaling the playback speed by a factor of 5, i.e., $f(t)\mapsto f(3t)$ and $f(t)\mapsto f(5t)$, respectively.

 In this way, tonnetz-centric musical analysis can be derived from a theory of rescaling the playback speed of continous, periodic audio signals by integer factors:

<p align="center">
  <picture>
    <source srcset="docs/images/scaling_signals_continuous_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/scaling_signals_continuous_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/scaling_signals_continuous_dark.jpg" alt="tonnetzB" width="700">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Moving a continuous periodic audio signal f(t) up two octaves via f(t) ↦ f(2t) ↦ f(4t)
</p>

Not all audio signals are continuous though. [Discrete audio signals](https://en.wikipedia.org/wiki/Discrete_time_and_continuous_time) have played and continue to play an important role in music production and in signal processing.

- 🔊 ***Audio Example***: <a href="docs/sounds/test_signal_11.wav"> 🔗 A discrete periodic audio signal</a>

For a discrete periodic audio signal, that is, for a periodic audio signal $s(i)$ that samples time at regular discrete intervals, so $i=0,1,2,\dots,\ell-1$ for some positive integer $\ell$, the notion of "re*scaling* times" doesn't quite make sense. We can still multiply the sample index $i$ by any integer $m$ to obtain a new signal: $s(i)\mapsto s(mi)$. However, the manner in which these sample indices $i$ transform under multiplication by an integer follows the rules of [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic), not the rules of continuous dilation:

<p align="center">
  <picture>
    <source srcset="docs/images/scaling_signals_discrete_dark.jpg" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/scaling_signals_discrete_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/scaling_signals_discrete_dark.jpg" alt="tonnetzB" width="700">
  </picture>
</p>
<p align="center" style="font-size: 80%;">
  Moving a discrete periodic audio signal s(i) "up two octaves" via s(i) ↦ s(2i) ↦ s(4i)
</p>

These modular, multiplicative transformations $s(i)\mapsto s(mi)$ of sample-index $i$ for discrete audio signals $s(i)$ become natural candidates for the *musical intervals* possible between discrete audio signals.

If we take this proposal seriously, we arrive at the following:
- ***Question:*** How is movement along all these "*discrete musical intervals*" interelated?

### Tonnetze for discrete audio signals
If you've played with 8-bit tones, you may already have a sense that for discrete periodic audio signals, movement along musical intervals doesn't work in exactly the same way as it does for continous periodic audio signals. Discrete audio signals have complex timbres that seem to have mysterious relationships to one another.

A lot of this mystery can be calrified by modeling the signals as vertices in a directed graph $\text{Ton}_{\ast}\big(\mathbb{Z}/\ell\mathbb{Z},\ [m_1,\dots,m_k]\big)$, or just $\text{Ton}_{\ast}$ for short, where edges represent multiplication by fixed integers modulo the sample count. The set of nodes in this graph is $\text{Ton}_{0}:=\mathbb{Z}/\ell\mathbb{Z}$ and the set of edges is $\text{Ton}_{1}:=\mathbb{Z}/\ell\mathbb{Z}\times[m_1,\dots,m_k]$,
with source and target maps $\partial_0,\partial_1:\text{Ton}_{1}\longrightarrow\text{Ton}_{0}$ that identify each pair $(n,m)$ with the edge $$n\xrightarrow{m}mn\ (\text{mod}\ \ell)$$

This graph captures how *discrete* spectral energy shifts under modular scaling, and reveals surprising orbit structures tied to the arithmetic of the modulus. However, if you pass this graph naively into a graph visualization library like `networkx.drawing`, the result is nearly unreadable — cluttered, asymmetric, and blind to the underlying modular symmetries that actually organize the space:

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

## Large-scale structure of discrete tonnetze

[...]

### Orbits under the unit group from natural clusters

[...]

```python
>>> from dissig.tonnetze.networks import Tonnetz
>>> from dissig.tonnetze.visualizers import nx_viz
```

[...]

```python
>>> modulus = 36
>>> integer_list = [2, 3, 5]
```

[...]

```python
>>> tonnetz = Tonnetz(modulus, integer_list)
>>> nx_viz(tonnetz, "test_viz", mode='dot')
```

[...]

<p align="center">
  <picture>
    <source srcset="docs/images/36_with_clusters_dark.png" media="(prefers-color-scheme: dark)">
    <source srcset="docs/images/36_with_clusters_light.jpg" media="(prefers-color-scheme: light)">
    <img src="docs/images/36_with_clusters_dark.jpg" alt="tonnetzB" width="750">
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

```python
>>> from dissig.tonnetze.networks import Tonnetz
>>> from dissig.tonnetze.visualizers import nx_viz
```

[...]

```python
>>> modulus = 36
>>> integer_list = [2, 3, 5, 7]
>>> tonnetz = Tonnetz(modulus, integer_list)
```

[...]

```python
>>> nx_viz(tonnetz, "test_viz", mode='neato', appearance_theme='dark')
```

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

```python
>>> modulus = 35 # Change modulus to 35
>>> tonnetz = Tonnetz(modulus, integer_list) # Use previous integer_list
>>> nx_viz(tonnetz, "test_viz", mode='neato', appearance_theme='dark')
```

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

```python
>>> modulus = 216 # Change modulus to 216 == 2**3 * 3**3
>>> integer_list = [2, 3, 5, 11, 13] # New integer_list
>>> tonnetz = Tonnetz(modulus, integer_list)
>>> nx_viz(tonnetz, "test_viz", mode='neato', appearance_theme='dark')
```

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

# Installation and Setup
- [🚀 Installation](##-installation)
- [🔧 Usage](##-usage)
- [🧪 Running Tests](##-running-tests)
- [📄 Documentation](##-documentation)
- [📦 Project Structure](##-project-structure)
- [🛠 Development](##-development)
- [📝 License](##-license)

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
>>> from dissig.tonnetze.networks import Tonnetz
>>> from dissig.tonnetze.visualizers import nx_viz
...
>>> modulus = 2**3 * 3**3
>>> integer_list = [2, 3, 5, 11, 13]
...
>>> tonnetz = Tonnetz(modulus, integer_list)
>>> nx_viz(tonnetz, "file_name")
```

[...]

```python
>>> from dissig.signals.discrete import character_signal
>>> from dissig.tonnetze.networks import SignalTonnetz
>>> from dissig.io.print_wav import tonnetz_to_wav
...
>>> modulus = 2**2 * 3**2
>>> integer_list = [2, 3, 5]
...
>>> signal = character_signal(1, modulus)
>>> signal_tonnetz = SignalTonnetz(signal, integer_list)
>>> tonnetz_to_wav(signal_tonnetz, 440.0, 1.0)
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

## 📦 Project Structure
```bash
.
├── docs  # Project documentation and resources
│   ├── external
│   ├── images
│   └── tex
├── results # Output files generated by the code
│   ├── tonnetze_visuals
│   └── wav_files
├── src
│   └── dissig  # Core project package
│       ├── __init__.py
│       ├── core.py  # High-level pipeline functions and orchestration
│       ├── io  # Input/output utilities
│       │   ├── __init__.py
│       │   └── print_wav.py  # Functions for saving audio to WAV
│       │       ├── signal_to_wav()
│       │       └── tonnetz_to_wav()
│       ├── signals # Signal representations and processing
│       │   ├── __init__.py
│       │   └── discrete.py # Discrete-time signal processing tools
│       │       ├── Signal  # Main Signal class
│       │       │   ├── scale_time_by()
│       │       │   ├── extract_real()
│       │       │   ├── __len__()
│       │       │   └── forward()
│       │       ├── character_signal() # Creates a character signal
│       │       └── signal_from_real() # Wraps real data as Signal
│       ├── tonnetze  # Tonnetz network structures and visualizers
│       │   ├── __init__.py
│       │   ├── networks.py # Builds Tonnetz graph structures
│       │   │   ├── Tonnetz # Main Tonnetz class
│       │   │   │   ├── generate_weighted_edges()
│       │   │   │   └── generate_network()
│       │   │   └── SignalTonnetz # Tonnetz decorated with signals
│       │   │       ├── generate_weighted_edges()
│       │   │       ├── generate_network()
│       │   │       └── propogate_signal()
│       │   └── visualizers.py  # Graph rendering functions
│       │       ├── nx_viz_cluster() # Clustered node visualization
│       │       └── nx_viz_neat() # Clean layout visualization
│       └── utils # Math utility functions
│           ├── __init__.py
│           ├── arithmetic.py # Number theoretic functions
│           │   ├── all_divisors()
│           │   ├── multiplicative_units()
│           │   └── unit_clusters()
│           └── primes.py # Prime-related functions
│               ├── primes_below()
│               ├── prime_divisors()
│               └── prime_powers()
├── tests # Unit tests for all modules
│   ├── io
│   ├── signals
│   ├── tonnetze
│   └── utils
├── LICENSE # License file (MIT License)
├── README.md # Top-level project overview and instructions
├── pdm.lock  # PDM lock file for reproducible installs
├── pyproject.toml  # Project configuration (dependencies, metadata)
├── pytest.ini  # Pytest configuration file
└── requirements.txt  # Optional: basic dependency list for pip users
```

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