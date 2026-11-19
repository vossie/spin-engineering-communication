#!/usr/bin/env python3
"""Lightweight repository checks for public-release hygiene and internal links."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".txt", ".css", ".js", ".svg"}
SKIP_DIRS = {".git", ".venv", "site", "__pycache__"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDERS_ALLOWED = {"OWNER"}


def files():
    for path in ROOT.rglob("*"):
        if path.is_file() and not any(part in SKIP_DIRS for part in path.parts):
            yield path


def check_links(errors: list[str]) -> None:
    for path in files():
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK.findall(text):
            target = raw.split("#", 1)[0].strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken link: {path.relative_to(ROOT)} -> {raw}")


def check_svg(errors: list[str]) -> None:
    for path in ROOT.rglob("*.svg"):
        try:
            root = ET.parse(path).getroot()
            if not root.tag.endswith("svg"):
                errors.append(f"not an SVG root: {path.relative_to(ROOT)}")
        except ET.ParseError as exc:
            errors.append(f"invalid SVG: {path.relative_to(ROOT)}: {exc}")


def check_public_hygiene(errors: list[str]) -> None:
    banned = [
        re.compile(r"caesars\s+digital", re.I),
        re.compile(r"caesarsdigital", re.I),
        re.compile(r"https?://[^\s)]+\.(?:internal|corp)(?:/|\b)", re.I),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    for path in files():
        if path.suffix not in TEXT_SUFFIXES or path.name == "validate.py":
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in banned:
            if pattern.search(text):
                errors.append(f"public-hygiene match in {path.relative_to(ROOT)}: {pattern.pattern}")


def check_framework_invariants(errors: list[str]) -> None:
    spec = (ROOT / "SPECIFICATION.md").read_text(encoding="utf-8")
    docs_spec = (ROOT / "docs" / "specification.md").read_text(encoding="utf-8")
    if spec != docs_spec:
        errors.append("docs/specification.md is not synchronized with SPECIFICATION.md")
    required_phrases = [
        "Subject and Priority are mandatory",
        "Impact and Note are optional",
        "Ownership is expressed in Subject",
    ]
    for phrase in required_phrases:
        if phrase not in spec:
            errors.append(f"specification invariant missing: {phrase}")

    examples = list((ROOT / "examples").glob("*.md"))
    for path in examples:
        text = path.read_text(encoding="utf-8")
        if "Subject:" not in text or "Priority:" not in text:
            errors.append(f"example missing Subject or Priority: {path.relative_to(ROOT)}")


def check_placeholders(errors: list[str]) -> None:
    for path in files():
        if path.suffix not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        for token in re.findall(r"\b[A-Z][A-Z0-9_]{4,}\b", text):
            if token.endswith("PLACEHOLDER") and token not in PLACEHOLDERS_ALLOWED:
                errors.append(f"unexpected placeholder {token} in {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    check_links(errors)
    check_svg(errors)
    check_public_hygiene(errors)
    check_framework_invariants(errors)
    check_placeholders(errors)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation passed: links, SVGs, public hygiene, and framework invariants.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

