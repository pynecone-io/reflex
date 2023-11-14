"""Import all classes and functions the end user will need to make an app.

Anything imported here will be available in the default Reflex import as `rx.*`.
To signal to typecheckers that something should be reexported,
we use the Flask "import name as name" syntax.
"""
import importlib
from typing import Type

from reflex.utils.format import to_snake_case

_ALL_COMPONENTS = [
    "Accordion",
    "AccordionButton",
    "AccordionIcon",
    "AccordionItem",
    "AccordionPanel",
    "Alert",
    "AlertDescription",
    "AlertDialog",
    "AlertDialogBody",
    "AlertDialogContent",
    "AlertDialogFooter",
    "AlertDialogHeader",
    "AlertDialogOverlay",
    "AlertIcon",
    "AlertTitle",
    "AspectRatio",
    "Audio",
    "Avatar",
    "AvatarBadge",
    "AvatarGroup",
    "Badge",
    "Box",
    "Breadcrumb",
    "BreadcrumbItem",
    "BreadcrumbLink",
    "BreadcrumbSeparator",
    "Button",
    "ButtonGroup",
    "Card",
    "CardBody",
    "CardFooter",
    "CardHeader",
    "Center",
    "Checkbox",
    "CheckboxGroup",
    "CircularProgress",
    "CircularProgressLabel",
    "Circle",
    "Code",
    "CodeBlock",
    "Collapse",
    "ColorModeButton",
    "ColorModeIcon",
    "ColorModeSwitch",
    "Component",
    "Cond",
    "Container",
    "DataTable",
    "DataEditor",
    "DebounceInput",
    "Divider",
    "Drawer",
    "DrawerBody",
    "DrawerCloseButton",
    "DrawerContent",
    "DrawerFooter",
    "DrawerHeader",
    "DrawerOverlay",
    "Editable",
    "EditableInput",
    "EditablePreview",
    "EditableTextarea",
    "Editor",
    "Email",
    "Fade",
    "Flex",
    "Foreach",
    "Form",
    "FormControl",
    "FormErrorMessage",
    "FormHelperText",
    "FormLabel",
    "Fragment",
    "Grid",
    "GridItem",
    "Heading",
    "Highlight",
    "Hstack",
    "Html",
    "Icon",
    "IconButton",
    "Image",
    "Input",
    "InputGroup",
    "InputLeftAddon",
    "InputLeftElement",
    "InputRightAddon",
    "InputRightElement",
    "Kbd",
    "Link",
    "LinkBox",
    "LinkOverlay",
    "List",
    "ListItem",
    "Markdown",
    "Menu",
    "MenuButton",
    "MenuDivider",
    "MenuGroup",
    "MenuItem",
    "MenuItemOption",
    "MenuList",
    "MenuOptionGroup",
    "Modal",
    "ModalBody",
    "ModalCloseButton",
    "ModalContent",
    "ModalFooter",
    "ModalHeader",
    "ModalOverlay",
    "Moment",
    "MultiSelect",
    "MultiSelectOption",
    "NextLink",
    "NumberDecrementStepper",
    "NumberIncrementStepper",
    "NumberInput",
    "NumberInputField",
    "NumberInputStepper",
    "Option",
    "OrderedList",
    "Password",
    "PinInput",
    "PinInputField",
    "Plotly",
    "Popover",
    "PopoverAnchor",
    "PopoverArrow",
    "PopoverBody",
    "PopoverCloseButton",
    "PopoverContent",
    "PopoverFooter",
    "PopoverHeader",
    "PopoverTrigger",
    "Progress",
    "Radio",
    "RadioGroup",
    "RangeSlider",
    "RangeSliderFilledTrack",
    "RangeSliderThumb",
    "RangeSliderTrack",
    "ResponsiveGrid",
    "ScaleFade",
    "Script",
    "Select",
    "Skeleton",
    "SkeletonCircle",
    "SkeletonText",
    "Slide",
    "SlideFade",
    "Slider",
    "SliderFilledTrack",
    "SliderMark",
    "SliderThumb",
    "SliderTrack",
    "Spacer",
    "Span",
    "Spinner",
    "Square",
    "Stack",
    "Stat",
    "StatArrow",
    "StatGroup",
    "StatHelpText",
    "StatLabel",
    "StatArrow",
    "StatGroup",
    "StatHelpText",
    "StatLabel",
    "StatNumber",
    "Step",
    "StepDescription",
    "StepIcon",
    "StepIndicator",
    "StepNumber",
    "StepSeparator",
    "StepStatus",
    "StepTitle",
    "Stepper",
    "Switch",
    "Tab",
    "TabList",
    "TabPanel",
    "TabPanels",
    "Table",
    "TableCaption",
    "TableContainer",
    "Tabs",
    "Tag",
    "TagCloseButton",
    "TagLabel",
    "TagLeftIcon",
    "TagRightIcon",
    "Tbody",
    "Td",
    "Text",
    "TextArea",
    "Tfoot",
    "Th",
    "Thead",
    "Tooltip",
    "Tr",
    "UnorderedList",
    "Upload",
    "Video",
    "VisuallyHidden",
    "Vstack",
    "Wrap",
    "WrapItem",
]

_ALL_COMPONENTS += [to_snake_case(component) for component in _ALL_COMPONENTS]
_ALL_COMPONENTS += [
    "components",
    "desktop_only",
    "mobile_only",
    "tablet_only",
    "mobile_and_tablet",
    "tablet_and_desktop",
    "selected_files",
    "clear_selected_files",
    "EditorOptions",
]

_MAPPING = {
    "reflex.admin": ["admin", "AdminDash"],
    "reflex.app": ["app", "App", "UploadFile"],
    "reflex.base": ["base", "Base"],
    "reflex.compiler": ["compiler"],
    "reflex.compiler.utils": ["get_asset_path"],
    "reflex.components": _ALL_COMPONENTS,
    "reflex.components.component": ["memo"],
    "reflex.components.graphing": ["recharts"],
    "reflex.config": ["config", "Config", "DBConfig"],
    "reflex.constants": ["constants", "Env"],
    "reflex.el": ["el"],
    "reflex.event": [
        "event",
        "EventChain",
        "background",
        "call_script",
        "clear_local_storage",
        "console_log",
        "download",
        "prevent_default",
        "redirect",
        "remove_cookie",
        "remove_local_storage",
        "set_clipboard",
        "set_focus",
        "set_value",
        "stop_propagation",
        "upload_files",
        "window_alert",
    ],
    "reflex.middleware": ["middleware", "Middleware"],
    "reflex.model": ["model", "session", "Model"],
    "reflex.page": ["page"],
    "reflex.route": ["route"],
    "reflex.state": ["state", "var", "Cookie", "LocalStorage", "State"],
    "reflex.style": ["style", "color_mode", "toggle_color_mode"],
    "reflex.testing": ["testing"],
    "reflex.utils": ["utils"],
    "reflex.vars": ["vars", "cached_var", "Var"],
}
_MAPPING = {value: key for key, values in _MAPPING.items() for value in values}


def _removeprefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix) :]


__all__ = [_removeprefix(mod, "reflex.") for mod in _MAPPING]


def __getattr__(name: str) -> Type:
    """Lazy load all modules.

    Args:
        name: name of the module to load.

    Returns:
        The module or the attribute of the module.

    Raises:
        AttributeError: If the module or the attribute does not exist.
    """
    try:
        # Check for import of a module that is not in the mapping.
        if name not in _MAPPING:
            # If the name does not start with reflex, add it.
            if not name.startswith("reflex") and name != "__all__":
                name = f"reflex.{name}"
            return importlib.import_module(name)

        # Import the module.
        module = importlib.import_module(_MAPPING[name])

        # Special case for page.
        if name == "page":
            globals()["page"] = module.page
            return module.page

        # Get the attribute from the module if the name is not the module itself.
        return (
            getattr(module, name) if name != _MAPPING[name].rsplit(".")[-1] else module
        )
    except ModuleNotFoundError:
        raise AttributeError(f"module 'reflex' has no attribute {name}") from None
