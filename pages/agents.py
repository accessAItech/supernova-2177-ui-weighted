# pages/agents.py
from __future__ import annotations
import os
import streamlit as st

PAGE = "agents"  # prefix so all widget keys on this page are unique


def _default_openai_key() -> str:
    """Prefer session -> secrets -> env, but never crash if secrets.toml is absent."""
    # 1) session
    val = st.session_state.get("openai_api_key")
    if isinstance(val, str) and val.strip():
        return val.strip()

    # 2) secrets (guarded so it doesn't raise when file doesn't exist)
    try:
        secret = st.secrets["openai_api_key"]  # type: ignore[index]
        if isinstance(secret, str) and secret.strip():
            return secret.strip()
    except Exception:
        pass

    # 3) environment
    return os.environ.get("OPENAI_API_KEY", "").strip()


def render() -> None:
    st.title("🤖 Agents")

    with st.form(f"{PAGE}_api_form"):
        key_input = st.text_input(
            "OpenAI API key",
            value=_default_openai_key(),
            type="password",
            placeholder="sk-...",
            key=f"{PAGE}_openai_api_key",  # ONE unique key only
        )
        saved = st.form_submit_button("Save")

    if saved:
        st.session_state["openai_api_key"] = key_input.strip()
        os.environ["OPENAI_API_KEY"] = st.session_state["openai_api_key"]
        st.success("Saved. Agents will use this key.")

    st.caption(
        "Tip: you can also set this in `.streamlit/secrets.toml` as "
        '`openai_api_key = "sk-..."`'
    )


def main() -> None:
    render()


if __name__ == "__main__":
    main()
