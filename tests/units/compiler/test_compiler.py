from pathlib import Path
from typing import List

import pytest

from reflex.compiler import compiler, utils
from reflex.utils.imports import ImportVar, ParsedImportDict


@pytest.mark.parametrize(
    "fields,test_default,test_rest",
    [
        (
            [ImportVar(tag="axios", is_default=True)],
            "axios",
            [],
        ),
        (
            [ImportVar(tag="foo"), ImportVar(tag="bar")],
            "",
            ["bar", "foo"],
        ),
        (
            [
                ImportVar(tag="axios", is_default=True),
                ImportVar(tag="foo"),
                ImportVar(tag="bar"),
            ],
            "axios",
            ["bar", "foo"],
        ),
    ],
)
def test_compile_import_statement(
    fields: List[ImportVar], test_default: str, test_rest: str
):
    """Test the compile_import_statement function.

    Args:
        fields: The fields to import.
        test_default: The expected output of default library.
        test_rest: The expected output rest libraries.
    """
    default, rest = utils.compile_import_statement(fields)
    assert default == test_default
    assert sorted(rest) == test_rest


@pytest.mark.parametrize(
    "import_dict,test_dicts",
    [
        ({}, []),
        (
            {"axios": [ImportVar(tag="axios", is_default=True)]},
            [{"lib": "axios", "default": "axios", "rest": []}],
        ),
        (
            {"axios": [ImportVar(tag="foo"), ImportVar(tag="bar")]},
            [{"lib": "axios", "default": "", "rest": ["bar", "foo"]}],
        ),
        (
            {
                "axios": [
                    ImportVar(tag="axios", is_default=True),
                    ImportVar(tag="foo"),
                    ImportVar(tag="bar"),
                ],
                "react": [ImportVar(tag="react", is_default=True)],
            },
            [
                {"lib": "axios", "default": "axios", "rest": ["bar", "foo"]},
                {"lib": "react", "default": "react", "rest": []},
            ],
        ),
        (
            {"": [ImportVar(tag="lib1.js"), ImportVar(tag="lib2.js")]},
            [
                {"lib": "lib1.js", "default": "", "rest": []},
                {"lib": "lib2.js", "default": "", "rest": []},
            ],
        ),
        (
            {
                "": [ImportVar(tag="lib1.js"), ImportVar(tag="lib2.js")],
                "axios": [ImportVar(tag="axios", is_default=True)],
            },
            [
                {"lib": "lib1.js", "default": "", "rest": []},
                {"lib": "lib2.js", "default": "", "rest": []},
                {"lib": "axios", "default": "axios", "rest": []},
            ],
        ),
    ],
)
def test_compile_imports(import_dict: ParsedImportDict, test_dicts: List[dict]):
    """Test the compile_imports function.

    Args:
        import_dict: The import dictionary.
        test_dicts: The expected output.
    """
    imports = utils.compile_imports(import_dict)
    for import_dict, test_dict in zip(imports, test_dicts):
        assert import_dict["lib"] == test_dict["lib"]
        assert import_dict["default"] == test_dict["default"]
        assert sorted(import_dict["rest"]) == test_dict["rest"]  # type: ignore


def test_compile_stylesheets(tmp_path: Path, mocker):
    """Test that stylesheets compile correctly.

    Args:
        tmp_path: The test directory.
        mocker: Pytest mocker object.
    """
    project = tmp_path / "test_project"
    project.mkdir()

    assets_dir = project / "assets"
    assets_dir.mkdir()

    (assets_dir / "styles.css").write_text(
        "button.rt-Button {\n\tborder-radius:unset !important;\n}"
    )
    mocker.patch("reflex.compiler.compiler.Path.cwd", return_value=project)

    stylesheets = [
        "https://fonts.googleapis.com/css?family=Sofia&effect=neon|outline|emboss|shadow-multiple",
        "https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css",
        "/styles.css",
        "https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css",
    ]

    assert compiler.compile_root_stylesheet(stylesheets) == (
        str(Path(".web") / "styles" / "styles.css"),
        "@import url('./tailwind.css'); \n"
        "@import url('https://fonts.googleapis.com/css?family=Sofia&effect=neon|outline|emboss|shadow-multiple'); \n"
        "@import url('https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css'); \n"
        "@import url('./styles.css'); \n"
        "@import url('https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css'); \n",
    )

    assert (project / ".web" / "styles" / "styles.css").read_text() == (
        assets_dir / "styles.css"
    ).read_text()


def test_compile_stylesheets_scss_sass(tmp_path: Path, mocker):
    try:
        import sass  # noqa: F401
    except ImportError:
        pytest.skip(
            'The `libsass` package is required to compile sass/scss stylesheet files. Run `pip install "libsass>=0.23.0"`.'
        )

    project = tmp_path / "test_project"
    project.mkdir()

    assets_dir = project / "assets"
    assets_dir.mkdir()

    assets_preprocess_dir = assets_dir / "preprocess"
    assets_preprocess_dir.mkdir()

    (assets_dir / "styles.css").write_text(
        "button.rt-Button {\n\tborder-radius:unset !important;\n}"
    )
    (assets_preprocess_dir / "styles_a.sass").write_text(
        "button.rt-Button\n\tborder-radius:unset !important"
    )
    (assets_preprocess_dir / "styles_b.scss").write_text(
        "button.rt-Button {\n\tborder-radius:unset !important;\n}"
    )
    mocker.patch("reflex.compiler.compiler.Path.cwd", return_value=project)

    stylesheets = [
        "/styles.css",
        "/preprocess/styles_a.sass",
        "/preprocess/styles_b.scss",
    ]

    assert compiler.compile_root_stylesheet(stylesheets) == (
        str(Path(".web") / "styles" / "styles.css"),
        "@import url('./tailwind.css'); \n"
        "@import url('./styles.css'); \n"
        "@import url('./preprocess/styles_a.css'); \n"
        "@import url('./preprocess/styles_b.css'); \n",
    )

    stylesheets = [
        "/styles.css",
        "/preprocess",  # this is a folder containing "styles_a.sass" and "styles_b.scss"
    ]

    assert compiler.compile_root_stylesheet(stylesheets) == (
        str(Path(".web") / "styles" / "styles.css"),
        "@import url('./tailwind.css'); \n"
        "@import url('./styles.css'); \n"
        "@import url('./preprocess/styles_b.css'); \n"
        "@import url('./preprocess/styles_a.css'); \n",
    )

    assert (project / ".web" / "styles" / "styles.css").read_text() == (
        assets_dir / "styles.css"
    ).read_text()

    expected_result = "button.rt-Button{border-radius:unset !important}\n"
    assert (
        project / ".web" / "styles" / "preprocess" / "styles_a.css"
    ).read_text() == expected_result
    assert (
        project / ".web" / "styles" / "preprocess" / "styles_b.css"
    ).read_text() == expected_result


def test_compile_stylesheets_exclude_tailwind(tmp_path, mocker):
    """Test that Tailwind is excluded if tailwind config is explicitly set to None.

    Args:
        tmp_path: The test directory.
        mocker: Pytest mocker object.
    """
    project = tmp_path / "test_project"
    project.mkdir()

    assets_dir = project / "assets"
    assets_dir.mkdir()
    mock = mocker.Mock()

    mocker.patch.object(mock, "tailwind", None)
    mocker.patch("reflex.compiler.compiler.get_config", return_value=mock)

    (assets_dir / "styles.css").touch()
    mocker.patch("reflex.compiler.compiler.Path.cwd", return_value=project)

    stylesheets = [
        "/styles.css",
    ]

    assert compiler.compile_root_stylesheet(stylesheets) == (
        str(Path(".web") / "styles" / "styles.css"),
        "@import url('./styles.css'); \n",
    )


def test_compile_nonexistent_stylesheet(tmp_path, mocker):
    """Test that an error is thrown for non-existent stylesheets.

    Args:
        tmp_path: The test directory.
        mocker: Pytest mocker object.
    """
    project = tmp_path / "test_project"
    project.mkdir()

    assets_dir = project / "assets"
    assets_dir.mkdir()

    mocker.patch("reflex.compiler.compiler.Path.cwd", return_value=project)

    stylesheets = ["/styles.css"]

    with pytest.raises(FileNotFoundError):
        compiler.compile_root_stylesheet(stylesheets)


def test_create_document_root():
    """Test that the document root is created correctly."""
    # Test with no components.
    root = utils.create_document_root()
    root.render()
    assert isinstance(root, utils.Html)
    assert isinstance(root.children[0], utils.DocumentHead)
    # Default language.
    assert root.lang == "en"  # type: ignore
    # No children in head.
    assert len(root.children[0].children) == 0

    # Test with components.
    comps = [
        utils.NextScript.create(src="foo.js"),
        utils.NextScript.create(src="bar.js"),
    ]
    root = utils.create_document_root(
        head_components=comps,  # type: ignore
        html_lang="rx",
        html_custom_attrs={"project": "reflex"},
    )
    # Two children in head.
    assert isinstance(root, utils.Html)
    assert len(root.children[0].children) == 2
    assert root.lang == "rx"  # type: ignore
    assert isinstance(root.custom_attrs, dict)
    assert root.custom_attrs == {"project": "reflex"}
