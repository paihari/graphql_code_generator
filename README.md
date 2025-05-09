# ⚙️ GraphQL Code Generator

A lightweight Python tool to **automatically generate Python classes and data access code** from a GraphQL schema. Ideal for developers who want to streamline their integration with GraphQL APIs by reducing boilerplate code.
 
---

## 🚀 Features

- 🔧 Parse GraphQL schemas and generate Python classes
- 🧱 Generate typed query/mutation classes for robust client-side development
- 📦 Simple command-line execution
- ✨ Lightweight and dependency-free (no GraphQL client library needed)

---

## 📁 Project Structure
```
graphql_code_generator/
├── generate_code.py # Core logic for parsing GraphQL schema and generating code
├── setup.py # Package metadata for installation (optional)
├── init.py # Marks this directory as a Python module
├── README.md # You're reading it!
├── steps.txt # Example usage instructions

```
---

## 📦 Installation

Clone this repository and optionally install it as a Python module:

```bash
git clone https://github.com/your-org/graphql_code_generator.git
cd graphql_code_generator
pip install .

```

---

⚙️ Usage
Prepare a GraphQL schema file (e.g., schema.graphql) and run:

```bash
python generate_code.py --input schema.graphql --output generated_code.py
```

This will generate Python classes for each type, query, and mutation found in the schema.

You can also refer to steps.txt for step-by-step usage guidance.

🛠 Example
Given this schema.graphql:

```bash
type Book {
  id: ID!
  title: String!
  author: String!
}
```

The tool generates:

```bash
class Book:
    def __init__(self, id: str, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author

```

📚 How It Works
The script uses regex and simple parsing logic to:

Read a GraphQL schema file

Identify type, query, and mutation blocks

Generate equivalent Python classes with type hints

No external GraphQL libraries required!


