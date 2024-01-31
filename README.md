# Sentence Scrabbler

Sentence Scrabbler is a Python program that takes a user-input sentence and rearranges its words using a list of English words obtained from a specified URL. The goal is to create a fun and scrambled version of the original sentence.

## Navigation

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Clone the Repository](#clone-the-repository)
    - [Install Dependencies](#install-dependencies)
    - [Run the Program](#run-the-program)
- [Usage](#usage)
  - [Enter Your Sentence](#enter-your-sentence)
  - [Scramble the Sentence](#scramble-the-sentence)
  - [Scramble Again (or Exit)](#scramble-again-or-exit)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you set up and run the Sentence Scrabbler on your local machine.

### Prerequisites

Make sure you have Python and pip installed on your machine.

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

#### Clone the Repository

Open your terminal or command prompt and run the following commands:

```bash
git clone https://github.com/your-username/sentence-scrabbler.git
cd sentence-scrabbler

#### Install Dependencies:
pip install spacy requests

#### Run the Program:
python -m spacy download en_core_web_md
python sentence_scrabbler.py

### Usage
Enter Your Sentence
You will be prompted to enter a sentence that you want to scramble.

#### Scramble the Sentence
Press Enter, and the program will display the original and scrambled sentences.

#### Scramble Again (or Exit)
Press Enter again to scramble the original sentence differently. If the scrambled sentence becomes the same as the original, the program will exit.

#### Configuration
The program uses the spaCy medium English language model for Natural Language Processing.
The English word list is downloaded from dwyl/english-words.
The scrambling process involves selecting words of the same length and starting with the same letter, creating a playful and entertaining result.



