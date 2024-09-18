"""A code component."""

from __future__ import annotations

from typing import Any, Dict, Literal, Optional, Union

from typing_extensions import get_args

from reflex.components.component import Component, ComponentNamespace
from reflex.components.core.cond import color_mode_cond
from reflex.components.lucide.icon import Icon
from reflex.components.radix.themes.components.button import Button
from reflex.components.radix.themes.layout.box import Box
from reflex.constants.colors import Color
from reflex.event import set_clipboard
from reflex.style import Style
from reflex.utils import console, format
from reflex.utils.imports import ImportDict, ImportVar
from reflex.vars.base import LiteralVar, Var, VarData

LiteralCodeBlockTheme = Literal[
    "a11y-dark",
    "atom-dark",
    "cb",
    "coldark-cold",
    "coldark-dark",
    "coy",
    "coy-without-shadows",
    "darcula",
    "dark",
    "dracula",
    "duotone-dark",
    "duotone-earth",
    "duotone-forest",
    "duotone-light",
    "duotone-sea",
    "duotone-space",
    "funky",
    "ghcolors",
    "gruvbox-dark",
    "gruvbox-light",
    "holi-theme",
    "hopscotch",
    "light",  # not present in react-syntax-highlighter styles
    "lucario",
    "material-dark",
    "material-light",
    "material-oceanic",
    "night-owl",
    "nord",
    "okaidia",
    "one-dark",
    "one-light",
    "pojoaque",
    "prism",
    "shades-of-purple",
    "solarized-dark-atom",
    "solarizedlight",
    "synthwave84",
    "tomorrow",
    "twilight",
    "vs",
    "vs-dark",
    "vsc-dark-plus",
    "xonokai",
    "z-touch",
]


LiteralCodeLanguage = Literal[
    "abap",
    "abnf",
    "actionscript",
    "ada",
    "agda",
    "al",
    "antlr4",
    "apacheconf",
    "apex",
    "apl",
    "applescript",
    "aql",
    "arduino",
    "arff",
    "asciidoc",
    "asm6502",
    "asmatmel",
    "aspnet",
    "autohotkey",
    "autoit",
    "avisynth",
    "avro-idl",
    "bash",
    "basic",
    "batch",
    "bbcode",
    "bicep",
    "birb",
    "bison",
    "bnf",
    "brainfuck",
    "brightscript",
    "bro",
    "bsl",
    "c",
    "cfscript",
    "chaiscript",
    "cil",
    "clike",
    "clojure",
    "cmake",
    "cobol",
    "coffeescript",
    "concurnas",
    "coq",
    "core",
    "cpp",
    "crystal",
    "csharp",
    "cshtml",
    "csp",
    "css",
    "css-extras",
    "csv",
    "cypher",
    "d",
    "dart",
    "dataweave",
    "dax",
    "dhall",
    "diff",
    "django",
    "dns-zone-file",
    "docker",
    "dot",
    "ebnf",
    "editorconfig",
    "eiffel",
    "ejs",
    "elixir",
    "elm",
    "erb",
    "erlang",
    "etlua",
    "excel-formula",
    "factor",
    "false",
    "firestore-security-rules",
    "flow",
    "fortran",
    "fsharp",
    "ftl",
    "gap",
    "gcode",
    "gdscript",
    "gedcom",
    "gherkin",
    "git",
    "glsl",
    "gml",
    "gn",
    "go",
    "go-module",
    "graphql",
    "groovy",
    "haml",
    "handlebars",
    "haskell",
    "haxe",
    "hcl",
    "hlsl",
    "hoon",
    "hpkp",
    "hsts",
    "http",
    "ichigojam",
    "icon",
    "icu-message-format",
    "idris",
    "iecst",
    "ignore",
    "index",
    "inform7",
    "ini",
    "io",
    "j",
    "java",
    "javadoc",
    "javadoclike",
    "javascript",
    "javastacktrace",
    "jexl",
    "jolie",
    "jq",
    "js-extras",
    "js-templates",
    "jsdoc",
    "json",
    "json5",
    "jsonp",
    "jsstacktrace",
    "jsx",
    "julia",
    "keepalived",
    "keyman",
    "kotlin",
    "kumir",
    "kusto",
    "latex",
    "latte",
    "less",
    "lilypond",
    "liquid",
    "lisp",
    "livescript",
    "llvm",
    "log",
    "lolcode",
    "lua",
    "magma",
    "makefile",
    "markdown",
    "markup",
    "markup-templating",
    "matlab",
    "maxscript",
    "mel",
    "mermaid",
    "mizar",
    "mongodb",
    "monkey",
    "moonscript",
    "n1ql",
    "n4js",
    "nand2tetris-hdl",
    "naniscript",
    "nasm",
    "neon",
    "nevod",
    "nginx",
    "nim",
    "nix",
    "nsis",
    "objectivec",
    "ocaml",
    "opencl",
    "openqasm",
    "oz",
    "parigp",
    "parser",
    "pascal",
    "pascaligo",
    "pcaxis",
    "peoplecode",
    "perl",
    "php",
    "php-extras",
    "phpdoc",
    "plsql",
    "powerquery",
    "powershell",
    "processing",
    "prolog",
    "promql",
    "properties",
    "protobuf",
    "psl",
    "pug",
    "puppet",
    "pure",
    "purebasic",
    "purescript",
    "python",
    "q",
    "qml",
    "qore",
    "qsharp",
    "r",
    "racket",
    "reason",
    "regex",
    "rego",
    "renpy",
    "rest",
    "rip",
    "roboconf",
    "robotframework",
    "ruby",
    "rust",
    "sas",
    "sass",
    "scala",
    "scheme",
    "scss",
    "shell-session",
    "smali",
    "smalltalk",
    "smarty",
    "sml",
    "solidity",
    "solution-file",
    "soy",
    "sparql",
    "splunk-spl",
    "sqf",
    "sql",
    "squirrel",
    "stan",
    "stylus",
    "swift",
    "systemd",
    "t4-cs",
    "t4-templating",
    "t4-vb",
    "tap",
    "tcl",
    "textile",
    "toml",
    "tremor",
    "tsx",
    "tt2",
    "turtle",
    "twig",
    "typescript",
    "typoscript",
    "unrealscript",
    "uorazor",
    "uri",
    "v",
    "vala",
    "vbnet",
    "velocity",
    "verilog",
    "vhdl",
    "vim",
    "visual-basic",
    "warpscript",
    "wasm",
    "web-idl",
    "wiki",
    "wolfram",
    "wren",
    "xeora",
    "xml-doc",
    "xojo",
    "xquery",
    "yaml",
    "yang",
    "zig",
]


def replace_quotes_with_camel_case(value: str) -> str:
    """Replaces quotes in the given string with camel case format.

    Args:
        value (str): The string to be processed.

    Returns:
        str: The processed string with quotes replaced by camel case.
    """
    for theme in get_args(LiteralCodeBlockTheme):
        value = value.replace(f'"{theme}"', format.to_camel_case(theme))
    return value


class CodeBlock(Component):
    """A code block."""

    library = "react-syntax-highlighter@15.5.0"

    tag = "PrismAsyncLight"

    alias = "SyntaxHighlighter"

    # The theme to use ("light" or "dark").
    theme: Var[Any] = "one-light"  # type: ignore

    # The language to use.
    language: Var[LiteralCodeLanguage] = "python"  # type: ignore

    # The code to display.
    code: Var[str]

    # If this is enabled line numbers will be shown next to the code block.
    show_line_numbers: Var[bool]

    # The starting line number to use.
    starting_line_number: Var[int]

    # Whether to wrap long lines.
    wrap_long_lines: Var[bool]

    # A custom style for the code block.
    custom_style: Dict[str, Union[str, Var, Color]] = {}

    # Props passed down to the code tag.
    code_tag_props: Var[Dict[str, str]]

    def add_imports(self) -> ImportDict:
        """Add imports for the CodeBlock component.

        Returns:
            The import dict.
        """
        imports_: ImportDict = {}

        if (
            self.language is not None
            and (language_without_quotes := str(self.language).replace('"', ""))
            in LiteralCodeLanguage.__args__  # type: ignore
        ):
            imports_[
                f"react-syntax-highlighter/dist/cjs/languages/prism/{language_without_quotes}"
            ] = [
                ImportVar(
                    tag=format.to_camel_case(language_without_quotes),
                    is_default=True,
                    install=False,
                )
            ]

        return imports_

    def _get_custom_code(self) -> Optional[str]:
        if (
            self.language is not None
            and (language_without_quotes := str(self.language).replace('"', ""))
            in LiteralCodeLanguage.__args__  # type: ignore
        ):
            return f"{self.alias}.registerLanguage('{language_without_quotes}', {format.to_camel_case(language_without_quotes)})"

    @classmethod
    def create(
        cls,
        *children,
        can_copy: Optional[bool] = False,
        copy_button: Optional[Union[bool, Component]] = None,
        **props,
    ):
        """Create a text component.

        Args:
            *children: The children of the component.
            can_copy: Whether a copy button should appears.
            copy_button: A custom copy button to override the default one.
            **props: The props to pass to the component.

        Returns:
            The text component.
        """
        # This component handles style in a special prop.
        custom_style = props.pop("custom_style", {})

        if "theme" not in props:
            # Default color scheme responds to global color mode.
            props["theme"] = color_mode_cond(
                light=Themes.one_light,
                dark=Themes.one_dark,
            )

        # react-syntax-highlighter doesnt have an explicit "light" or "dark" theme so we use one-light and one-dark
        # themes respectively to ensure code compatibility.
        if "theme" in props and not isinstance(props["theme"], Var):
            props["theme"] = getattr(Themes, format.to_snake_case(props["theme"]))  # type: ignore
            console.deprecate(
                feature_name="theme prop as string",
                reason="Use code_block.themes instead.",
                deprecation_version="0.6.0",
                removal_version="0.7.0",
            )

        if can_copy:
            code = children[0]
            copy_button = (  # type: ignore
                copy_button
                if copy_button is not None
                else Button.create(
                    Icon.create(tag="copy"),
                    on_click=set_clipboard(code),
                    style=Style({"position": "absolute", "top": "0.5em", "right": "0"}),
                )
            )
            custom_style.update({"padding": "1em 3.2em 1em 1em"})
        else:
            copy_button = None

        # Transfer style props to the custom style prop.
        for key, value in props.items():
            if key not in cls.get_fields():
                custom_style[key] = value

        # Carry the children (code) via props
        if children:
            props["code"] = children[0]
            if not isinstance(props["code"], Var):
                props["code"] = LiteralVar.create(props["code"])

        # Create the component.
        code_block = super().create(
            **props,
            custom_style=Style(custom_style),
        )

        if copy_button:
            return Box.create(code_block, copy_button, position="relative")
        else:
            return code_block

    def add_style(self):
        """Add style to the component."""
        self.custom_style.update(self.style)

    def _render(self):
        out = super()._render()

        theme = self.theme

        out.add_props(style=theme).remove_props("theme", "code").add_props(
            children=self.code
        )

        return out

    @staticmethod
    def convert_theme_name(theme) -> str:
        """Convert theme names to appropriate names.

        Args:
            theme: The theme name.

        Returns:
            The right theme name.
        """
        if theme in ["light", "dark"]:
            return f"one-{theme}"
        return theme


def construct_theme_var(theme: str) -> Var:
    """Construct a theme var.

    Args:
        theme: The theme to construct.

    Returns:
        The constructed theme var.
    """
    return Var(
        theme,
        _var_data=VarData(
            imports={
                f"react-syntax-highlighter/dist/cjs/styles/prism/{format.to_kebab_case(theme)}": [
                    ImportVar(tag=theme, is_default=True, install=False)
                ]
            }
        ),
    )


class Themes:
    """Themes for the CodeBlock component."""

    a11y_dark = construct_theme_var("a11yDark")
    atom_dark = construct_theme_var("atomDark")
    cb = construct_theme_var("cb")
    coldark_cold = construct_theme_var("coldarkCold")
    coldark_dark = construct_theme_var("coldarkDark")
    coy = construct_theme_var("coy")
    coy_without_shadows = construct_theme_var("coyWithoutShadows")
    darcula = construct_theme_var("darcula")
    dark = construct_theme_var("dark")
    dracula = construct_theme_var("dracula")
    duotone_dark = construct_theme_var("duotoneDark")
    duotone_earth = construct_theme_var("duotoneEarth")
    duotone_forest = construct_theme_var("duotoneForest")
    duotone_light = construct_theme_var("duotoneLight")
    duotone_sea = construct_theme_var("duotoneSea")
    duotone_space = construct_theme_var("duotoneSpace")
    funky = construct_theme_var("funky")
    ghcolors = construct_theme_var("ghcolors")
    gruvbox_dark = construct_theme_var("gruvboxDark")
    gruvbox_light = construct_theme_var("gruvboxLight")
    holi_theme = construct_theme_var("holiTheme")
    hopscotch = construct_theme_var("hopscotch")
    light = construct_theme_var("light")
    lucario = construct_theme_var("lucario")
    material_dark = construct_theme_var("materialDark")
    material_light = construct_theme_var("materialLight")
    material_oceanic = construct_theme_var("materialOceanic")
    night_owl = construct_theme_var("nightOwl")
    nord = construct_theme_var("nord")
    okaidia = construct_theme_var("okaidia")
    one_dark = construct_theme_var("oneDark")
    one_light = construct_theme_var("oneLight")
    pojoaque = construct_theme_var("pojoaque")
    prism = construct_theme_var("prism")
    shades_of_purple = construct_theme_var("shadesOfPurple")
    solarized_dark_atom = construct_theme_var("solarizedDarkAtom")
    solarizedlight = construct_theme_var("solarizedlight")
    synthwave84 = construct_theme_var("synthwave84")
    tomorrow = construct_theme_var("tomorrow")
    twilight = construct_theme_var("twilight")
    vs = construct_theme_var("vs")
    vs_dark = construct_theme_var("vsDark")
    vsc_dark_plus = construct_theme_var("vscDarkPlus")
    xonokai = construct_theme_var("xonokai")
    z_touch = construct_theme_var("zTouch")


class CodeblockNamespace(ComponentNamespace):
    """Namespace for the CodeBlock component."""

    themes = Themes

    __call__ = CodeBlock.create


code_block = CodeblockNamespace()
