#!/usr/bin/env python3
"""Validate CodeBTI repository structure.

This script intentionally uses only the Python standard library so the Markdown
skill can be checked without installing project dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
QUESTION_HEADING_RE = re.compile(r"^##\s+([A-Z]\d+)\.\s+", re.MULTILINE)

EXCLUDED_DIRS = {".git", ".claude", ".pytest_cache", "__pycache__", "build", "dist"}
EXCLUDED_FILES = {".DS_Store"}
MANIFEST_DIRECTORY_ALLOWLIST = {
    Path("zh/python/patterns/gof"),
    Path("zh/typescript/patterns/gof"),
}

REQUIRED_QUESTION_FIELDS = (
    "Question ID:",
    "Scope:",
    "Dimension:",
    "User-facing scenario:",
    "User-facing instruction:",
    "Code example:",
    "Choices:",
    "Agent scoring:",
    "Pattern signals:",
    "CodeStyle output implications:",
)

REQUIRED_PACK_FILES = {
    "project": (
        "project/questions/README.md",
        "project/questions/fixed-project.md",
        "project/profiles/README.md",
        "project/profiles/project-profile-taxonomy.md",
        "project/templates/ProjectStyle.template.md",
    ),
    "python": (
        "python/questions/README.md",
        "python/questions/fixed-python.md",
        "python/profiles/README.md",
        "python/profiles/python-profile-taxonomy.md",
        "python/patterns/README.md",
        "python/patterns/gof/README.md",
        "python/templates/README.md",
        "python/templates/CodeStyle.template.md",
        "python/records/README.md",
    ),
    "typescript": (
        "typescript/questions/README.md",
        "typescript/questions/fixed-typescript.md",
        "typescript/profiles/README.md",
        "typescript/profiles/typescript-profile-taxonomy.md",
        "typescript/patterns/README.md",
        "typescript/patterns/gof/README.md",
        "typescript/templates/README.md",
        "typescript/templates/CodeStyle.template.md",
        "typescript/records/README.md",
    ),
}

QUESTION_FILES = {
    "project/questions/fixed-project.md": {
        "prefix": "P",
        "expected_count": 6,
        "expected_scope": "Project",
        "id_prefix": "project.",
    },
    "python/questions/fixed-python.md": {
        "prefix": "Q",
        "expected_count": 10,
        "expected_scope": "Language:Python",
        "id_prefix": "python.",
    },
    "typescript/questions/fixed-typescript.md": {
        "prefix": "Q",
        "expected_count": 10,
        "expected_scope": "Language:TypeScript",
        "id_prefix": "typescript.",
    },
}

TRANSLATED_QUESTION_FILES = {
    "zh/python/questions/fixed-python.md": ("Q", 10),
    "zh/typescript/questions/fixed-typescript.md": ("Q", 10),
}

VALID_FIXED_SCOPES = {"Project", "Language:Python", "Language:TypeScript"}

REQUIRED_TEMPLATE_SECTIONS = {
    "project/templates/ProjectStyle.template.md": (
        "## Project Intent",
        "## Evidence Summary",
        "## Collaboration Workflow",
        "## Shared Rules",
        "## Language Sections",
        "## Generated Output Policy",
        "## References",
        "## Open Assumptions",
    ),
    "python/templates/CodeStyle.template.md": (
        "## Project Intent",
        "## Evidence Summary",
        "## Shared Project Rules",
        "## Default Code Shape",
        "## Python Style Rules",
        "## Pattern Guidance",
        "## References",
        "## Testing Policy",
        "## Git and Collaboration",
        "## Agent Behavior",
        "## Examples",
        "## Open Assumptions",
    ),
    "typescript/templates/CodeStyle.template.md": (
        "## Project Intent",
        "## Evidence Summary",
        "## Shared Project Rules",
        "## Default Code Shape",
        "## TypeScript Style Rules",
        "## Pattern Guidance",
        "## References",
        "## Testing Policy",
        "## Git and Collaboration",
        "## Agent Behavior",
        "## Examples",
        "## Open Assumptions",
    ),
    "shared/templates/SKILL.template.md": (
        "## Purpose",
        "## Source Evidence",
        "## Style Contract",
        "## Workflow",
        "## Agent Rules",
        "## Pattern Preferences",
    ),
    "shared/templates/SPEC.template.md": (
        "## Mission",
        "## Goals",
        "## Target Audience",
        "## Constraints",
        "## Non-Goals",
        "## Tech Stack",
        "## Roadmap",
        "## Summary",
        "## Requirements",
        "## Shared Project Rules",
        "## Architecture Rules",
        "## Interfaces and Data",
        "## Error Handling",
        "## Testing",
        "## Agent Implementation Notes",
        "## Open Questions",
    ),
}


def repo_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS or part.endswith(".egg-info") for part in rel.parts):
            continue
        if path.name in EXCLUDED_FILES:
            continue
        files.append(rel)
    return sorted(files)


def markdown_files() -> list[Path]:
    return [path for path in repo_files() if path.suffix == ".md"]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0]
    return target


def is_external_or_empty(target: str) -> bool:
    if not target:
        return True
    if target.startswith("#"):
        return True
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
        return True
    return False


def validate_links(errors: list[str]) -> None:
    for rel_path in markdown_files():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in MARKDOWN_LINK_RE.finditer(line):
                target = normalize_link_target(match.group(1))
                if is_external_or_empty(target):
                    continue
                candidate = (ROOT / rel_path).parent / target
                if not candidate.exists():
                    fail(errors, f"Broken link: {rel_path}:{line_number} -> {match.group(1)}")


def validate_required_pack_files(errors: list[str]) -> None:
    for pack, paths in REQUIRED_PACK_FILES.items():
        for path in paths:
            if not (ROOT / path).exists():
                fail(errors, f"Missing required {pack} pack file: {path}")


def question_sections(text: str) -> list[tuple[str, str]]:
    matches = list(QUESTION_HEADING_RE.finditer(text))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1), text[start:end]))
    return sections


def field_first_value(section: str, field: str) -> str:
    field_index = section.find(field)
    if field_index == -1:
        return ""
    rest = section[field_index + len(field):]
    for line in rest.splitlines():
        value = line.strip()
        if value:
            return value
    return ""


def field_block(section: str, field: str) -> str:
    field_index = section.find(field)
    if field_index == -1:
        return ""
    start = field_index + len(field)
    next_indexes = [
        section.find(next_field, start)
        for next_field in REQUIRED_QUESTION_FIELDS
        if next_field != field and section.find(next_field, start) != -1
    ]
    end = min(next_indexes) if next_indexes else len(section)
    return section[start:end].strip()


def option_labels(block: str) -> set[str]:
    return set(re.findall(r"^-\s*([A-E])(?:[.:])\s+", block, re.MULTILINE))


def validate_question_file(
    errors: list[str],
    path: str,
    prefix: str,
    expected_count: int,
    expected_scope: str | None = None,
    id_prefix: str | None = None,
) -> set[str]:
    full_path = ROOT / path
    if not full_path.exists():
        fail(errors, f"Missing question file: {path}")
        return set()

    text = full_path.read_text(encoding="utf-8")
    sections = [(qid, section) for qid, section in question_sections(text) if qid.startswith(prefix)]
    if len(sections) != expected_count:
        fail(errors, f"{path}: expected {expected_count} {prefix} questions, found {len(sections)}")
        return set()

    question_ids: set[str] = set()
    for qid, section in sections:
        for field in REQUIRED_QUESTION_FIELDS:
            if field not in section:
                fail(errors, f"{path}: {qid} missing required field {field}")
        question_id = field_first_value(section, "Question ID:")
        if question_id:
            question_ids.add(question_id)
            if id_prefix and not question_id.startswith(id_prefix):
                fail(errors, f"{path}: {qid} question id `{question_id}` should start with `{id_prefix}`")
        scope = field_first_value(section, "Scope:")
        if scope:
            if scope not in VALID_FIXED_SCOPES:
                fail(errors, f"{path}: {qid} has invalid scope `{scope}`")
            if expected_scope and scope != expected_scope:
                fail(errors, f"{path}: {qid} expected scope `{expected_scope}`, found `{scope}`")

        choices = option_labels(field_block(section, "Choices:"))
        scoring = option_labels(field_block(section, "Agent scoring:"))
        pattern_signals = option_labels(field_block(section, "Pattern signals:"))
        if choices and choices != scoring:
            fail(errors, f"{path}: {qid} choice labels {sorted(choices)} do not match agent scoring labels {sorted(scoring)}")
        if choices and choices != pattern_signals:
            fail(errors, f"{path}: {qid} choice labels {sorted(choices)} do not match pattern signal labels {sorted(pattern_signals)}")
        implication = field_block(section, "CodeStyle output implications:")
        if len(implication.split()) < 5:
            fail(errors, f"{path}: {qid} has too little CodeStyle output implication text")
    return question_ids


def validate_questions(errors: list[str]) -> None:
    seen_ids: dict[str, str] = {}
    for path, meta in QUESTION_FILES.items():
        ids = validate_question_file(
            errors,
            path,
            meta["prefix"],
            meta["expected_count"],
            meta["expected_scope"],
            meta["id_prefix"],
        )
        for question_id in ids:
            if question_id in seen_ids:
                fail(errors, f"Duplicate Question ID `{question_id}` in {seen_ids[question_id]} and {path}")
            seen_ids[question_id] = path
    for path, (prefix, expected_count) in TRANSLATED_QUESTION_FILES.items():
        full_path = ROOT / path
        if not full_path.exists():
            fail(errors, f"Missing translated question file: {path}")
            continue
        sections = [(qid, section) for qid, section in question_sections(full_path.read_text(encoding="utf-8")) if qid.startswith(prefix)]
        if len(sections) != expected_count:
            fail(errors, f"{path}: expected {expected_count} translated {prefix} questions, found {len(sections)}")


def validate_templates(errors: list[str]) -> None:
    for path, required_sections in REQUIRED_TEMPLATE_SECTIONS.items():
        full_path = ROOT / path
        if not full_path.exists():
            fail(errors, f"Missing template file: {path}")
            continue
        text = full_path.read_text(encoding="utf-8")
        for heading in required_sections:
            if heading not in text:
                fail(errors, f"{path}: missing template section {heading}")


def validate_shared_translation_mirror(errors: list[str]) -> None:
    shared_files = sorted(path.relative_to(ROOT / "shared") for path in (ROOT / "shared").rglob("*") if path.is_file())
    for rel_path in shared_files:
        mirror = ROOT / "zh" / "shared" / rel_path
        if not mirror.exists():
            fail(errors, f"Missing zh/shared mirror for shared/{rel_path}")


def manifest_paths() -> set[Path]:
    manifest = ROOT / "MANIFEST.md"
    if not manifest.exists():
        return set()
    text = manifest.read_text(encoding="utf-8")
    paths: set[Path] = set()
    for line in text.splitlines():
        match = re.match(r"^\|\s*`([^`]+)`\s*\|", line)
        if not match:
            continue
        candidate = Path(match.group(1))
        paths.add(candidate)
    return paths


def validate_manifest(errors: list[str]) -> None:
    listed = manifest_paths()
    listed_dirs = {path for path in listed if (ROOT / path).is_dir()}
    disallowed_dirs = sorted(path for path in listed_dirs if path not in MANIFEST_DIRECTORY_ALLOWLIST)
    if disallowed_dirs:
        preview = ", ".join(str(path) for path in disallowed_dirs)
        fail(errors, f"MANIFEST.md lists non-allowlisted directories instead of files: {preview}")
    listed_dirs = listed_dirs & MANIFEST_DIRECTORY_ALLOWLIST
    actual = {path for path in repo_files() if path.name != "MANIFEST.md"}
    missing = sorted(
        path
        for path in actual - listed
        if not any(str(path).startswith(f"{directory}/") for directory in listed_dirs)
    )
    if missing:
        preview = ", ".join(str(path) for path in missing[:20])
        if len(missing) > 20:
            preview += f", ... (+{len(missing) - 20} more)"
        fail(errors, f"MANIFEST.md missing repository files: {preview}")


def collect_errors() -> list[str]:
    errors: list[str] = []
    validate_links(errors)
    validate_required_pack_files(errors)
    validate_questions(errors)
    validate_templates(errors)
    validate_shared_translation_mirror(errors)
    validate_manifest(errors)
    return errors


def main() -> int:
    errors = collect_errors()

    if errors:
        print("CodeBTI validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("CodeBTI validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
