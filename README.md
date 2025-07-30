# 💬 Gemini Chatbot with Chainlit

This is a conversational chatbot built using [Chainlit](https://docs.chainlit.io/) and Google’s Gemini 2.0 Flash model. It supports session-based memory and optionally OAuth for user authentication. This project is ready for deployment and can be easily customized or extended.

---

## 📂 Project Files

| File | Description |
|------|-------------|
| `.python-version` | Specifies the Python version for tools like `pyenv` or `uv`. |
| `chainlit.md` | Markdown documentation or description of your Chainlit app (used by Chainlit). |
| `chainlit.yaml` | Configuration file for Chainlit (e.g. app title, theming, OAuth setup, etc). |
| `main.py` | Main application logic: handles chat events, model integration, session handling. |
| `pyproject.toml` | Python project metadata and dependency declarations (used by `uv`, `pip`, etc). |
| `uv.lock` | Lock file for the `uv` package manager, ensuring consistent dependency installs. |
| `README.md` | Project documentation and instructions (you’re reading it!). |

---

## 🧪 Requirements

- Python 3.10+
- [Chainlit](https://docs.chainlit.io/)
- `google-generativeai`
- `python-dotenv`
- `uv` (if you're using the `uv.lock` file for package management)

Install dependencies with `uv`:

```bash
uv pip install -r requirements.txt
