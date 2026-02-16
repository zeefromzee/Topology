# Topological Characterization of Access Structures in Secret Sharing via Simplicial Homology

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![SageMath 9.0+](https://img.shields.io/badge/SageMath-9.0%2B-blue.svg)](https://www.sagemath.org/)

## Abstract

Secret sharing schemes (SSS) are a foundational cryptographic primitive enabling the partitioning of a sensitive datum among a group of participants such that only predetermined authorized subsets can reconstruct the original secret. This repository contains the complete implementation of a topology-based diagnostic pipeline that evaluates the feasibility, efficiency, and structural security of secret sharing access structures using tools from algebraic topology. Given an access structure as input, the pipeline constructs its associated unauthorized simplicial complex, computes topological invariants (Betti numbers, Euler characteristic, simplicial homology groups), and outputs a feasibility and security assessment without requiring explicit scheme construction.

## Table of Contents

- [Abstract](#abstract)
- [Motivation](#motivation)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Access Structure Input Format](#access-structure-input-format)
  - [Running the Full Pipeline](#running-the-full-pipeline)
  - [Individual Module Usage](#individual-module-usage)
- [Pipeline Overview](#pipeline-overview)
- [Output Format](#output-format)
- [Examples](#examples)
- [Testing](#testing)
- [Reproducing Paper Results](#reproducing-paper-results)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [Citation](#citation)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Motivation

A central challenge in the design of secret sharing schemes is determining, prior to construction, whether a given access structure can be realized efficiently or whether it inherently requires large, costly shares. Currently, this evaluation is performed through case-by-case algebraic analysis or brute-force search. No general-purpose diagnostic tool exists that assesses feasibility and cost directly from the access structure.

This project addresses that gap by leveraging the observation that the unauthorized subsets of any monotone access structure naturally form a simplicial complex. Topological invariants of this complex encode structural information about the access structure that is not captured by purely combinatorial analysis, including collusion resistance properties, share size lower bounds, critical participant identification, and ideal scheme existence.

## Features

- **Access Structure Enumeration**: Generate all distinct access structures for a given participant count (4 to 7 participants supported)
- **Simplicial Complex Construction**: Automatic conversion of unauthorized set families into simplicial complexes
- **Homology Computation**: Computation of simplicial homology groups, Betti numbers, and Euler characteristic via SageMath
- **Critical Participant Detection**: Topological identification of participants whose compromise disproportionately weakens the scheme
- **Share Size Bound Estimation**: Information-theoretic lower bound computation and correlation with topological invariants
- **Matroid Analysis**: Representability checking to determine ideal scheme existence
- **Visualization**: Generation of simplicial complex diagrams for small participant sets
- **Batch Processing**: Full pipeline execution across comprehensive datasets of access structures
- **Export**: Results exported as CSV, JSON, and LaTeX tables for direct inclusion in publications

## Repository Structure

```
.
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── config/
│   └── default.yaml              # Default pipeline configuration
├── src/
│   ├── __init__.py
│   ├── access_structure/
│   │   ├── __init__.py
│   │   ├── generator.py          # Access structure enumeration
│   │   ├── validator.py          # Monotonicity and consistency checks
│   │   └── converter.py          # Access structure to simplicial complex
│   ├── crypto/
│   │   ├── __init__.py
│   │   ├── shamir.py             # Shamir secret sharing implementation
│   │   ├── share_bounds.py       # Information-theoretic share size bounds
│   │   ├── ideality.py           # Ideal scheme detection via matroid ports
│   │   └── threat_analysis.py    # Combinatorial threat simulation
│   ├── topology/
│   │   ├── __init__.py
│   │   ├── complex_builder.py    # Simplicial complex construction
│   │   ├── homology.py           # Homology group computation
│   │   ├── betti.py              # Betti number computation
│   │   ├── euler.py              # Euler characteristic computation
│   │   ├── vertex_analysis.py    # Vertex removal and link computation
│   │   └── visualization.py     # Complex rendering and diagram export
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── runner.py             # End-to-end pipeline orchestration
│   │   ├── correlation.py        # Topological-cryptographic correlation
│   │   └── report.py             # Report generation (CSV, JSON, LaTeX)
│   └── utils/
│       ├── __init__.py
│       ├── sets.py               # Subset and power set utilities
│       └── formatting.py         # Output formatting helpers
├── tests/
│   ├── __init__.py
│   ├── test_access_structure.py
│   ├── test_shamir.py
│   ├── test_complex_builder.py
│   ├── test_homology.py
│   ├── test_vertex_analysis.py
│   ├── test_pipeline.py
│   └── fixtures/
│       ├── small_structures.json
│       └── expected_invariants.json
├── notebooks/
│   ├── 01_shamir_demo.ipynb           # Interactive Shamir scheme walkthrough
│   ├── 02_complex_construction.ipynb  # Step-by-step complex building
│   ├── 03_homology_computation.ipynb  # Homology computation examples
│   ├── 04_full_pipeline.ipynb         # Complete pipeline demonstration
│   └── 05_case_studies.ipynb          # Detailed case studies from the paper
├── data/
│   ├── input/
│   │   └── access_structures/         # Predefined access structure datasets
│   └── output/
│       ├── invariants/                # Computed topological invariants
│       ├── correlations/              # Correlation analysis results
│       ├── figures/                   # Generated diagrams and plots
│       └── tables/                    # LaTeX-formatted result tables
├── paper/
│   ├── main.tex                       # Paper source
│   ├── references.bib                 # Bibliography
│   └── figures/                       # Figures used in the paper
└── docs/
    ├── mathematical_background.md     # Detailed mathematical reference
    ├── pipeline_specification.md      # Pipeline technical specification
    └── api_reference.md               # Module-level API documentation
```

## Prerequisites

- **Python** 3.9 or higher
- **SageMath** 9.0 or higher (required for simplicial homology computation)
- **Git** for cloning the repository

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/topological-secret-sharing.git
cd topological-secret-sharing
```

### 2. Install SageMath

SageMath must be installed separately as it is not available via pip.

**Ubuntu/Debian:**
```bash
sudo apt install sagemath
```

**macOS (Homebrew):**
```bash
brew install --cask sage
```

**Windows:**
Download the installer from [https://www.sagemath.org/download.html](https://www.sagemath.org/download.html).

**Conda (all platforms):**
```bash
conda install -c conda-forge sage
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -m pytest tests/ -v
```

All tests should pass. If SageMath is not found, ensure it is on your system PATH.

## Usage

### Quick Start

```python
from src.access_structure.generator import AccessStructure
from src.pipeline.runner import Pipeline

# Define participants and minimal authorized sets
participants = ['A', 'B', 'C', 'D']
minimal_authorized = [{'A', 'B'}, {'A', 'C'}, {'A', 'D'}, {'B', 'C', 'D'}]

# Create access structure
access = AccessStructure(participants, minimal_authorized)

# Run diagnostic pipeline
pipeline = Pipeline(access)
report = pipeline.run()

# View results
report.summary()
```

### Access Structure Input Format

Access structures are defined by specifying participants and minimal authorized sets. The input can be provided programmatically or via JSON:

```json
{
    "participants": ["A", "B", "C", "D"],
    "minimal_authorized_sets": [
        ["A", "B"],
        ["A", "C"],
        ["A", "D"],
        ["B", "C", "D"]
    ],
    "description": "Hierarchical structure with participant A as senior authority"
}
```

### Running the Full Pipeline

**From the command line:**
```bash
python -m src.pipeline.runner --input data/input/access_structures/hierarchical_4.json --output data/output/
```

**Batch processing all structures for a given participant count:**
```bash
python -m src.pipeline.runner --enumerate --participants 5 --output data/output/
```

### Individual Module Usage

**Simplicial complex construction only:**
```python
from src.access_structure.converter import to_simplicial_complex

unauthorized_sets = [{'B','C'}, {'B','D'}, {'C','D'}, {'A'}, {'B'}, {'C'}, {'D'}]
delta = to_simplicial_complex(unauthorized_sets)
print(delta.facets())
```

**Homology computation only:**
```python
from src.topology.homology import compute_homology

results = compute_homology(delta)
print(results.betti_numbers)
print(results.euler_characteristic)
print(results.homology_groups)
```

**Critical participant analysis only:**
```python
from src.topology.vertex_analysis import critical_participants

critical = critical_participants(delta, participants)
for name, score in critical.items():
    print(f"{name}: impact score = {score}")
```

## Pipeline Overview

```
┌──────────────────────────────┐
│   Access Structure Input     │
│   (participants + policy)    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   Validation                 │
│   (monotonicity, consistency)│
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   Unauthorized Set           │
│   Identification             │
└──────────────┬───────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
┌──────────────┐ ┌──────────────┐
│  Simplicial  │ │  Share Size  │
│  Complex     │ │  Bound       │
│  Construction│ │  Computation │
└──────┬───────┘ └──────┬───────┘
       │                │
       ▼                │
┌──────────────┐        │
│  Topological │        │
│  Invariant   │        │
│  Computation │        │
├──────────────┤        │
│  - Betti     │        │
│  - Euler     │        │
│  - Homology  │        │
│  - Vertex    │        │
│    Analysis  │        │
└──────┬───────┘        │
       │                │
       └──────┬─────────┘
              │
              ▼
┌──────────────────────────────┐
│   Correlation Analysis       │
│   (topology vs. crypto)      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   Diagnostic Report          │
│   (CSV, JSON, LaTeX)         │
└──────────────────────────────┘
```

## Output Format

The pipeline produces a structured diagnostic report containing:

| Field | Description |
|-------|-------------|
| `betti_numbers` | List of Betti numbers [$\beta_0$, $\beta_1$, ...] |
| `euler_characteristic` | Integer-valued topological summary |
| `homology_groups` | Simplicial homology groups at each dimension |
| `share_size_lower_bound` | Information-theoretic minimum share size (bits) |
| `is_ideal` | Boolean indicating whether an ideal scheme exists |
| `critical_participants` | Ranked list of participants by topological impact score |
| `collusion_zones` | Number of independent unauthorized components ($\beta_0$) |
| `structural_holes` | Number of detected homological obstructions ($\beta_1$, ...) |

## Examples

Detailed worked examples are provided in the `notebooks/` directory:

| Notebook | Description |
|----------|-------------|
| `01_shamir_demo.ipynb` | Interactive walkthrough of Shamir's (t,n) threshold scheme |
| `02_complex_construction.ipynb` | Step-by-step construction of unauthorized simplicial complexes |
| `03_homology_computation.ipynb` | Computing and interpreting Betti numbers and homology groups |
| `04_full_pipeline.ipynb` | End-to-end pipeline execution on example access structures |
| `05_case_studies.ipynb` | Reproduction of all case studies presented in the paper |

## Testing

Run the complete test suite:

```bash
python -m pytest tests/ -v
```

Run tests for a specific module:

```bash
python -m pytest tests/test_homology.py -v
```

Run tests with coverage report:

```bash
python -m pytest tests/ --cov=src --cov-report=html
```

## Reproducing Paper Results

To reproduce all results presented in the accompanying paper:

```bash
# Step 1: Enumerate all access structures for 4 to 7 participants
python -m src.pipeline.runner --enumerate --participants 4 5 6 7 --output data/output/

# Step 2: Generate correlation tables
python -m src.pipeline.correlation --input data/output/invariants/ --output data/output/correlations/

# Step 3: Generate LaTeX tables for the paper
python -m src.pipeline.report --input data/output/correlations/ --format latex --output paper/tables/

# Step 4: Generate figures
python -m src.topology.visualization --input data/output/invariants/ --output paper/figures/
```

All generated tables and figures will be placed in the `paper/` directory and can be compiled directly with the provided `paper/main.tex`.

## Limitations

- **Scale**: Exhaustive enumeration is computationally feasible only for access structures involving up to approximately 10 to 12 participants due to the exponential growth of the power set.
- **Bound tightness**: Topological lower bounds on share size are necessary but not always tight. The gap between the topological bound and the actual optimal share size varies by structure.
- **Linear schemes only**: The matroid-based ideality analysis applies to linear secret sharing schemes. Non-linear schemes, which can occasionally be more efficient, fall outside this framework.
- **No direct construction**: The pipeline analyzes and predicts properties of access structures but does not output a ready-to-use secret sharing protocol.

## Future Work

- **Quantum Secret Sharing**: Extension of the simplicial framework to quantum access structures, where shares are quantum states and reconstruction involves quantum operations.
- **Machine Learning on Topological Features**: Training classifiers on topological invariants to predict optimal share size without explicit bound computation, enabling rapid evaluation of large access structures.
- **Persistent Homology**: Application of persistent homology to parameterized families of access structures to track topological phase transitions in scheme efficiency.
- **Dynamic Access Structures**: Analysis of how adding or removing participants affects the topology of the unauthorized complex in real-time membership change scenarios.

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes with clear, descriptive messages.
4. Ensure all existing tests pass: `python -m pytest tests/ -v`.
5. Add tests for any new functionality.
6. Submit a pull request with a description of your changes.

Please read the full [Contributing Guidelines](CONTRIBUTING.md) before submitting.

## Citation

If you use this software or methodology in your research, please cite our paper:

```bibtex
@inproceedings{yourname2026topological,
  author    = {Your Name and Co-Author Name},
  title     = {Topological Characterization of Access Structures in Secret Sharing via Simplicial Homology},
  booktitle = {Proceedings of [Conference Name]},
  year      = {2026},
  pages     = {XX--XX},
  doi       = {10.XXXX/XXXXXXX}
}
```

## Authors

- **[Zeel]** - Cryptographic analysis, threat modeling, share size bounds, pipeline integration
- **[Dhruvi]** - Topological analysis, simplicial homology computation, visualization

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This work utilizes [SageMath](https://www.sagemath.org/) for simplicial homology computation.
- The theoretical foundations build upon the work of Shamir, Beimel, Stinson, and Seymour in secret sharing theory and access structure analysis.
