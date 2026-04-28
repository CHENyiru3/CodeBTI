from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts import validate_repo  # noqa: E402


OPENING_PROMPT_SNIPPET = "compact SPEC-style brief"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_repository_validation_passes() -> None:
    assert validate_repo.collect_errors() == []


def test_fixed_question_ids_are_unique_and_scoped() -> None:
    seen: dict[str, str] = {}
    for path, meta in validate_repo.QUESTION_FILES.items():
        text = read(path)
        sections = [
            (qid, section)
            for qid, section in validate_repo.question_sections(text)
            if qid.startswith(meta["prefix"])
        ]
        assert len(sections) == meta["expected_count"]
        for qid, section in sections:
            question_id = validate_repo.field_first_value(section, "Question ID:")
            scope = validate_repo.field_first_value(section, "Scope:")
            assert question_id.startswith(meta["id_prefix"]), f"{path} {qid}"
            assert scope == meta["expected_scope"], f"{path} {qid}"
            assert question_id not in seen, f"{question_id} used by {seen.get(question_id)} and {path}"
            seen[question_id] = path


def test_choices_have_matching_hidden_signal_labels() -> None:
    for path, meta in validate_repo.QUESTION_FILES.items():
        text = read(path)
        sections = [
            (qid, section)
            for qid, section in validate_repo.question_sections(text)
            if qid.startswith(meta["prefix"])
        ]
        for qid, section in sections:
            choices = validate_repo.option_labels(validate_repo.field_block(section, "Choices:"))
            scoring = validate_repo.option_labels(validate_repo.field_block(section, "Agent scoring:"))
            signals = validate_repo.option_labels(validate_repo.field_block(section, "Pattern signals:"))
            assert choices == scoring, f"{path} {qid}"
            assert choices == signals, f"{path} {qid}"


def test_templates_include_required_sections() -> None:
    assert "shared/templates/SKILL.template.md" in validate_repo.REQUIRED_TEMPLATE_SECTIONS
    assert "shared/templates/SPEC.template.md" in validate_repo.REQUIRED_TEMPLATE_SECTIONS
    for path, headings in validate_repo.REQUIRED_TEMPLATE_SECTIONS.items():
        text = read(path)
        for heading in headings:
            assert heading in text, f"{path} missing {heading}"


def test_manifest_inventory_is_file_based() -> None:
    paths = validate_repo.manifest_paths()

    assert Path("docs") not in paths
    assert Path("docs/golden-path.md") in paths
    assert Path("tests") not in paths
    assert Path("tests/test_validate_repo.py") in paths

    listed_dirs = {path for path in paths if (ROOT / path).is_dir()}
    assert listed_dirs <= validate_repo.MANIFEST_DIRECTORY_ALLOWLIST


def test_release_hardening_docs_are_linked() -> None:
    readme = read("README.md")
    agent = read("AGENT.md")
    changelog = read("CHANGELOG.md")
    golden_path = read("docs/golden-path.md")
    pyproject = read("pyproject.toml")

    assert "docs/golden-path.md" in readme
    assert "CHANGELOG.md" in readme
    assert "docs/golden-path.md" in agent
    assert "0.2.0 - 2026-04-28" in changelog
    assert 'version = "0.2.0"' in pyproject
    assert "python3 scripts/validate_repo.py" in golden_path
    assert "python3 -m pytest" in golden_path


def test_opening_prompt_is_spec_style_and_recorded() -> None:
    skill = read("SKILL.md")
    golden_path = read("docs/golden-path.md")
    record_template = read("shared/records/session-record.template.md")
    spec_template = read("shared/templates/SPEC.template.md")

    for text in (skill, golden_path, record_template):
        assert OPENING_PROMPT_SNIPPET in text
        assert "mission, goals, target audience, constraints" in text
        assert "roadmap intent, non-goals, and open questions" in text

    for heading in (
        "## Mission",
        "## Goals",
        "## Target Audience",
        "## Constraints",
        "## Non-Goals",
        "## Tech Stack",
        "## Roadmap",
        "## Open Questions",
    ):
        assert heading in spec_template


def test_multilanguage_fixture_is_complete() -> None:
    recording = read("tests/fixtures/multilang/Recording.md")
    code_style = read("tests/fixtures/multilang/CodeStyle.md")
    spec = read("tests/fixtures/multilang/SPEC.md")

    assert "## Opening SPEC Intake" in recording
    assert "[SPEC.md](SPEC.md)" in recording
    assert "Roadmap intent" in recording
    assert "Open questions" in recording
    for question in [f"P{i}" for i in range(1, 7)]:
        assert question in recording
    for language in ("Python", "TypeScript"):
        assert f"Language:{language}" in recording
        for question in [f"Q{i}" for i in range(1, 11)]:
            assert question in recording
    for question in [f"A{i}" for i in range(1, 6)]:
        assert question in recording

    for heading in (
        "## Shared Project Rules",
        "## Evidence Summary",
        "## Python Style Rules",
        "## TypeScript Style Rules",
        "## Pattern Guidance",
        "## References",
        "## Testing Policy",
        "## Agent Behavior",
    ):
        assert heading in code_style

    for heading in ("## Mission", "## Goals", "## Tech Stack", "## Roadmap", "## Open Questions"):
        assert heading in spec
