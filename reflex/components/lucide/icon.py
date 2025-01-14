"""Lucide Icon component."""

from reflex.components.component import Component
from reflex.utils import format
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var


class LucideIconComponent(Component):
    """Lucide Icon Component."""

    library = "lucide-react@0.471.1"


class Icon(LucideIconComponent):
    """An Icon component."""

    tag = "None"

    # The size of the icon in pixels.
    size: Var[int]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Initialize the Icon component.

        Run some additional checks on Icon component.

        Args:
            *children: The positional arguments
            **props: The keyword arguments

        Raises:
            AttributeError: The errors tied to bad usage of the Icon component.
            ValueError: If the icon tag is invalid.

        Returns:
            The created component.
        """
        if children:
            if len(children) == 1 and isinstance(children[0], str):
                props["tag"] = children[0]
                children = []
            else:
                raise AttributeError(
                    f"Passing multiple children to Icon component is not allowed: remove positional arguments {children[1:]} to fix"
                )
        if "tag" not in props:
            raise AttributeError("Missing 'tag' keyword-argument for Icon")

        if isinstance(props["tag"], Var):
            icon_name = props.pop("tag")
            return DynamicIcon.create(name=icon_name, **props)

        if (
            not isinstance(props["tag"], str)
            or format.to_snake_case(props["tag"]) not in LUCIDE_ICON_LIST
        ):
            raise ValueError(
                f"Invalid icon tag: {props['tag']}. Please use one of the following: {', '.join(LUCIDE_ICON_LIST[0:25])}, ..."
                "\nSee full list at https://lucide.dev/icons."
            )

        if props["tag"] in LUCIDE_ICON_MAPPING_OVERRIDE:
            props["tag"] = LUCIDE_ICON_MAPPING_OVERRIDE[props["tag"]]
        else:
            props["tag"] = (
                format.to_title_case(format.to_snake_case(props["tag"])) + "Icon"
            )
        props["alias"] = f"Lucide{props['tag']}"
        props.setdefault("color", "var(--current-color)")
        return super().create(*children, **props)


class DynamicIcon(LucideIconComponent):
    """A DynamicIcon component."""

    tag = "DynamicIcon"

    name: Var[str]

    def _get_imports(self):
        _imports = super()._get_imports()
        if self.library:
            _imports.pop(self.library)
        _imports["lucide-react/dynamic"] = [ImportVar("DynamicIcon", install=False)]
        return _imports


LUCIDE_ICON_LIST = [
    "a_arrow_down",
    "a_arrow_up",
    "a_large_small",
    "accessibility",
    "activity",
    "air_vent",
    "airplay",
    "alarm_clock",
    "alarm_clock_check",
    "alarm_clock_minus",
    "alarm_clock_off",
    "alarm_clock_plus",
    "alarm_smoke",
    "album",
    "align_center",
    "align_center_horizontal",
    "align_center_vertical",
    "align_end_horizontal",
    "align_end_vertical",
    "align_horizontal_distribute_center",
    "align_horizontal_distribute_end",
    "align_horizontal_distribute_start",
    "align_horizontal_justify_center",
    "align_horizontal_justify_end",
    "align_horizontal_justify_start",
    "align_horizontal_space_around",
    "align_horizontal_space_between",
    "align_justify",
    "align_left",
    "align_right",
    "align_start_horizontal",
    "align_start_vertical",
    "align_vertical_distribute_center",
    "align_vertical_distribute_end",
    "align_vertical_distribute_start",
    "align_vertical_justify_center",
    "align_vertical_justify_end",
    "align_vertical_justify_start",
    "align_vertical_space_around",
    "align_vertical_space_between",
    "ambulance",
    "ampersand",
    "ampersands",
    "amphora",
    "anchor",
    "angry",
    "annoyed",
    "antenna",
    "anvil",
    "aperture",
    "app_window",
    "app_window_mac",
    "apple",
    "archive",
    "archive_restore",
    "archive_x",
    "area_chart",
    "armchair",
    "arrow_big_down",
    "arrow_big_down_dash",
    "arrow_big_left",
    "arrow_big_left_dash",
    "arrow_big_right",
    "arrow_big_right_dash",
    "arrow_big_up",
    "arrow_big_up_dash",
    "arrow_down",
    "arrow_down_0_1",
    "arrow_down_1_0",
    "arrow_down_a_z",
    "arrow_down_from_line",
    "arrow_down_left",
    "arrow_down_narrow_wide",
    "arrow_down_right",
    "arrow_down_to_dot",
    "arrow_down_to_line",
    "arrow_down_up",
    "arrow_down_wide_narrow",
    "arrow_down_z_a",
    "arrow_left",
    "arrow_left_from_line",
    "arrow_left_right",
    "arrow_left_to_line",
    "arrow_right",
    "arrow_right_from_line",
    "arrow_right_left",
    "arrow_right_to_line",
    "arrow_up",
    "arrow_up_0_1",
    "arrow_up_1_0",
    "arrow_up_a_z",
    "arrow_up_down",
    "arrow_up_from_dot",
    "arrow_up_from_line",
    "arrow_up_left",
    "arrow_up_narrow_wide",
    "arrow_up_right",
    "arrow_up_to_line",
    "arrow_up_wide_narrow",
    "arrow_up_z_a",
    "arrows_up_from_line",
    "asterisk",
    "at_sign",
    "atom",
    "audio_lines",
    "audio_waveform",
    "award",
    "axe",
    "axis_3d",
    "baby",
    "backpack",
    "badge",
    "badge_alert",
    "badge_cent",
    "badge_check",
    "badge_dollar_sign",
    "badge_euro",
    "badge_help",
    "badge_indian_rupee",
    "badge_info",
    "badge_japanese_yen",
    "badge_minus",
    "badge_percent",
    "badge_plus",
    "badge_pound_sterling",
    "badge_russian_ruble",
    "badge_swiss_franc",
    "badge_x",
    "baggage_claim",
    "ban",
    "banana",
    "bandage",
    "banknote",
    "bar_chart",
    "bar_chart_2",
    "bar_chart_3",
    "bar_chart_4",
    "bar_chart_big",
    "bar_chart_horizontal",
    "bar_chart_horizontal_big",
    "barcode",
    "baseline",
    "bath",
    "battery",
    "battery_charging",
    "battery_full",
    "battery_low",
    "battery_medium",
    "battery_warning",
    "beaker",
    "bean",
    "bean_off",
    "bed",
    "bed_double",
    "bed_single",
    "beef",
    "beer",
    "beer_off",
    "bell",
    "bell_dot",
    "bell_electric",
    "bell_minus",
    "bell_off",
    "bell_plus",
    "bell_ring",
    "between_horizontal_end",
    "between_horizontal_start",
    "between_vertical_end",
    "between_vertical_start",
    "biceps_flexed",
    "bike",
    "binary",
    "binoculars",
    "biohazard",
    "bird",
    "bitcoin",
    "blend",
    "blinds",
    "blocks",
    "bluetooth",
    "bluetooth_connected",
    "bluetooth_off",
    "bluetooth_searching",
    "bold",
    "bolt",
    "bomb",
    "bone",
    "book",
    "book_a",
    "book_audio",
    "book_check",
    "book_copy",
    "book_dashed",
    "book_down",
    "book_headphones",
    "book_heart",
    "book_image",
    "book_key",
    "book_lock",
    "book_marked",
    "book_minus",
    "book_open",
    "book_open_check",
    "book_open_text",
    "book_plus",
    "book_text",
    "book_type",
    "book_up",
    "book_up_2",
    "book_user",
    "book_x",
    "bookmark",
    "bookmark_check",
    "bookmark_minus",
    "bookmark_plus",
    "bookmark_x",
    "boom_box",
    "bot",
    "bot_message_square",
    "bot_off",
    "box",
    "box_select",
    "boxes",
    "braces",
    "brackets",
    "brain",
    "brain_circuit",
    "brain_cog",
    "brick_wall",
    "briefcase",
    "briefcase_business",
    "briefcase_conveyor_belt",
    "briefcase_medical",
    "bring_to_front",
    "brush",
    "bug",
    "bug_off",
    "bug_play",
    "building",
    "building_2",
    "bus",
    "bus_front",
    "cable",
    "cable_car",
    "cake",
    "cake_slice",
    "calculator",
    "calendar",
    "calendar_1",
    "calendar_arrow_down",
    "calendar_arrow_up",
    "calendar_check",
    "calendar_check_2",
    "calendar_clock",
    "calendar_cog",
    "calendar_days",
    "calendar_fold",
    "calendar_heart",
    "calendar_minus",
    "calendar_minus_2",
    "calendar_off",
    "calendar_plus",
    "calendar_plus_2",
    "calendar_range",
    "calendar_search",
    "calendar_sync",
    "calendar_x",
    "calendar_x_2",
    "camera",
    "camera_off",
    "candlestick_chart",
    "candy",
    "candy_cane",
    "candy_off",
    "cannabis",
    "captions",
    "captions_off",
    "car",
    "car_front",
    "car_taxi_front",
    "caravan",
    "carrot",
    "case_lower",
    "case_sensitive",
    "case_upper",
    "cassette_tape",
    "cast",
    "castle",
    "cat",
    "cctv",
    "chart_area",
    "chart_bar",
    "chart_bar_big",
    "chart_bar_decreasing",
    "chart_bar_increasing",
    "chart_bar_stacked",
    "chart_candlestick",
    "chart_column",
    "chart_column_big",
    "chart_column_decreasing",
    "chart_column_increasing",
    "chart_column_stacked",
    "chart_gantt",
    "chart_line",
    "chart_network",
    "chart_no_axes_column",
    "chart_no_axes_column_decreasing",
    "chart_no_axes_column_increasing",
    "chart_no_axes_combined",
    "chart_no_axes_gantt",
    "chart_pie",
    "chart_scatter",
    "chart_spline",
    "check",
    "check_check",
    "chef_hat",
    "cherry",
    "chevron_down",
    "chevron_first",
    "chevron_last",
    "chevron_left",
    "chevron_right",
    "chevron_up",
    "chevrons_down",
    "chevrons_down_up",
    "chevrons_left",
    "chevrons_left_right",
    "chevrons_left_right_ellipsis",
    "chevrons_right",
    "chevrons_right_left",
    "chevrons_up",
    "chevrons_up_down",
    "chrome",
    "church",
    "cigarette",
    "cigarette_off",
    "circle",
    "circle_alert",
    "circle_arrow_down",
    "circle_arrow_left",
    "circle_arrow_out_down_left",
    "circle_arrow_out_down_right",
    "circle_arrow_out_up_left",
    "circle_arrow_out_up_right",
    "circle_arrow_right",
    "circle_arrow_up",
    "circle_check",
    "circle_check_big",
    "circle_chevron_down",
    "circle_chevron_left",
    "circle_chevron_right",
    "circle_chevron_up",
    "circle_dashed",
    "circle_divide",
    "circle_dollar_sign",
    "circle_dot",
    "circle_dot_dashed",
    "circle_ellipsis",
    "circle_equal",
    "circle_fading_arrow_up",
    "circle_fading_plus",
    "circle_gauge",
    "circle_help",
    "circle_minus",
    "circle_off",
    "circle_parking",
    "circle_parking_off",
    "circle_pause",
    "circle_percent",
    "circle_play",
    "circle_plus",
    "circle_power",
    "circle_slash",
    "circle_slash_2",
    "circle_stop",
    "circle_user",
    "circle_user_round",
    "circle_x",
    "circuit_board",
    "citrus",
    "clapperboard",
    "clipboard",
    "clipboard_check",
    "clipboard_copy",
    "clipboard_list",
    "clipboard_minus",
    "clipboard_paste",
    "clipboard_pen",
    "clipboard_pen_line",
    "clipboard_plus",
    "clipboard_type",
    "clipboard_x",
    "clock",
    "clock_1",
    "clock_10",
    "clock_11",
    "clock_12",
    "clock_2",
    "clock_3",
    "clock_4",
    "clock_5",
    "clock_6",
    "clock_7",
    "clock_8",
    "clock_9",
    "clock_alert",
    "clock_arrow_down",
    "clock_arrow_up",
    "cloud",
    "cloud_alert",
    "cloud_cog",
    "cloud_download",
    "cloud_drizzle",
    "cloud_fog",
    "cloud_hail",
    "cloud_lightning",
    "cloud_moon",
    "cloud_moon_rain",
    "cloud_off",
    "cloud_rain",
    "cloud_rain_wind",
    "cloud_snow",
    "cloud_sun",
    "cloud_sun_rain",
    "cloud_upload",
    "cloudy",
    "clover",
    "club",
    "code",
    "code_xml",
    "codepen",
    "codesandbox",
    "coffee",
    "cog",
    "coins",
    "columns_2",
    "columns_3",
    "columns_4",
    "combine",
    "command",
    "compass",
    "component",
    "computer",
    "concierge_bell",
    "cone",
    "construction",
    "contact",
    "contact_round",
    "container",
    "contrast",
    "cookie",
    "cooking_pot",
    "copy",
    "copy_check",
    "copy_minus",
    "copy_plus",
    "copy_slash",
    "copy_x",
    "copyleft",
    "copyright",
    "corner_down_left",
    "corner_down_right",
    "corner_left_down",
    "corner_left_up",
    "corner_right_down",
    "corner_right_up",
    "corner_up_left",
    "corner_up_right",
    "cpu",
    "creative_commons",
    "credit_card",
    "croissant",
    "crop",
    "cross",
    "crosshair",
    "crown",
    "cuboid",
    "cup_soda",
    "currency",
    "cylinder",
    "dam",
    "database",
    "database_backup",
    "database_zap",
    "delete",
    "dessert",
    "diameter",
    "diamond",
    "diamond_minus",
    "diamond_percent",
    "diamond_plus",
    "dice_1",
    "dice_2",
    "dice_3",
    "dice_4",
    "dice_5",
    "dice_6",
    "dices",
    "diff",
    "disc",
    "disc_2",
    "disc_3",
    "disc_album",
    "divide",
    "dna",
    "dna_off",
    "dock",
    "dog",
    "dollar_sign",
    "donut",
    "door_closed",
    "door_open",
    "dot",
    "download",
    "drafting_compass",
    "drama",
    "dribbble",
    "drill",
    "droplet",
    "droplet_off",
    "droplets",
    "drum",
    "drumstick",
    "dumbbell",
    "ear",
    "ear_off",
    "earth",
    "earth_lock",
    "eclipse",
    "egg",
    "egg_fried",
    "egg_off",
    "ellipsis",
    "ellipsis_vertical",
    "equal",
    "equal_approximately",
    "equal_not",
    "eraser",
    "ethernet_port",
    "euro",
    "expand",
    "external_link",
    "eye",
    "eye_closed",
    "eye_off",
    "facebook",
    "factory",
    "fan",
    "fast_forward",
    "feather",
    "fence",
    "ferris_wheel",
    "figma",
    "file",
    "file_archive",
    "file_audio",
    "file_audio_2",
    "file_axis_3d",
    "file_badge",
    "file_badge_2",
    "file_bar_chart",
    "file_bar_chart_2",
    "file_box",
    "file_chart_column",
    "file_chart_column_increasing",
    "file_chart_line",
    "file_chart_pie",
    "file_check",
    "file_check_2",
    "file_clock",
    "file_code",
    "file_code_2",
    "file_cog",
    "file_diff",
    "file_digit",
    "file_down",
    "file_heart",
    "file_image",
    "file_input",
    "file_json",
    "file_json_2",
    "file_key",
    "file_key_2",
    "file_line_chart",
    "file_lock",
    "file_lock_2",
    "file_minus",
    "file_minus_2",
    "file_music",
    "file_output",
    "file_pen",
    "file_pen_line",
    "file_pie_chart",
    "file_plus",
    "file_plus_2",
    "file_question",
    "file_scan",
    "file_search",
    "file_search_2",
    "file_sliders",
    "file_spreadsheet",
    "file_stack",
    "file_symlink",
    "file_terminal",
    "file_text",
    "file_type",
    "file_type_2",
    "file_up",
    "file_user",
    "file_video",
    "file_video_2",
    "file_volume",
    "file_volume_2",
    "file_warning",
    "file_x",
    "file_x_2",
    "files",
    "film",
    "filter",
    "filter_x",
    "fingerprint",
    "fire_extinguisher",
    "fish",
    "fish_off",
    "fish_symbol",
    "flag",
    "flag_off",
    "flag_triangle_left",
    "flag_triangle_right",
    "flame",
    "flame_kindling",
    "flashlight",
    "flashlight_off",
    "flask_conical",
    "flask_conical_off",
    "flask_round",
    "flip_horizontal",
    "flip_horizontal_2",
    "flip_vertical",
    "flip_vertical_2",
    "flower",
    "flower_2",
    "focus",
    "fold_horizontal",
    "fold_vertical",
    "folder",
    "folder_archive",
    "folder_check",
    "folder_clock",
    "folder_closed",
    "folder_code",
    "folder_cog",
    "folder_dot",
    "folder_down",
    "folder_git",
    "folder_git_2",
    "folder_heart",
    "folder_input",
    "folder_kanban",
    "folder_key",
    "folder_lock",
    "folder_minus",
    "folder_open",
    "folder_open_dot",
    "folder_output",
    "folder_pen",
    "folder_plus",
    "folder_root",
    "folder_search",
    "folder_search_2",
    "folder_symlink",
    "folder_sync",
    "folder_tree",
    "folder_up",
    "folder_x",
    "folders",
    "footprints",
    "forklift",
    "forward",
    "frame",
    "framer",
    "frown",
    "fuel",
    "fullscreen",
    "gallery_horizontal",
    "gallery_horizontal_end",
    "gallery_thumbnails",
    "gallery_vertical",
    "gallery_vertical_end",
    "gamepad",
    "gamepad_2",
    "gantt_chart",
    "gauge",
    "gavel",
    "gem",
    "ghost",
    "gift",
    "git_branch",
    "git_branch_plus",
    "git_commit_horizontal",
    "git_commit_vertical",
    "git_compare",
    "git_compare_arrows",
    "git_fork",
    "git_graph",
    "git_merge",
    "git_pull_request",
    "git_pull_request_arrow",
    "git_pull_request_closed",
    "git_pull_request_create",
    "git_pull_request_create_arrow",
    "git_pull_request_draft",
    "github",
    "gitlab",
    "glass_water",
    "glasses",
    "globe",
    "globe_lock",
    "goal",
    "grab",
    "graduation_cap",
    "grape",
    "grid_2x2",
    "grid_2x_2",
    "grid_2x_2_check",
    "grid_2x_2_plus",
    "grid_2x_2_x",
    "grid_3x3",
    "grid_3x_3",
    "grip",
    "grip_horizontal",
    "grip_vertical",
    "group",
    "guitar",
    "ham",
    "hammer",
    "hand",
    "hand_coins",
    "hand_heart",
    "hand_helping",
    "hand_metal",
    "hand_platter",
    "handshake",
    "hard_drive",
    "hard_drive_download",
    "hard_drive_upload",
    "hard_hat",
    "hash",
    "haze",
    "hdmi_port",
    "heading",
    "heading_1",
    "heading_2",
    "heading_3",
    "heading_4",
    "heading_5",
    "heading_6",
    "headphone_off",
    "headphones",
    "headset",
    "heart",
    "heart_crack",
    "heart_handshake",
    "heart_off",
    "heart_pulse",
    "heater",
    "hexagon",
    "highlighter",
    "history",
    "home",
    "hop",
    "hop_off",
    "hospital",
    "hotel",
    "hourglass",
    "house",
    "house_plug",
    "house_plus",
    "house_wifi",
    "ice_cream_bowl",
    "ice_cream_cone",
    "id_card",
    "image",
    "image_down",
    "image_minus",
    "image_off",
    "image_play",
    "image_plus",
    "image_up",
    "image_upscale",
    "images",
    "import",
    "inbox",
    "indent_decrease",
    "indent_increase",
    "indian_rupee",
    "infinity",
    "info",
    "inspection_panel",
    "instagram",
    "italic",
    "iteration_ccw",
    "iteration_cw",
    "japanese_yen",
    "joystick",
    "kanban",
    "key",
    "key_round",
    "key_square",
    "keyboard",
    "keyboard_music",
    "keyboard_off",
    "lamp",
    "lamp_ceiling",
    "lamp_desk",
    "lamp_floor",
    "lamp_wall_down",
    "lamp_wall_up",
    "land_plot",
    "landmark",
    "languages",
    "laptop",
    "laptop_minimal",
    "laptop_minimal_check",
    "lasso",
    "lasso_select",
    "laugh",
    "layers",
    "layers_2",
    "layers_3",
    "layout_dashboard",
    "layout_grid",
    "layout_list",
    "layout_panel_left",
    "layout_panel_top",
    "layout_template",
    "leaf",
    "leafy_green",
    "lectern",
    "letter_text",
    "library",
    "library_big",
    "life_buoy",
    "ligature",
    "lightbulb",
    "lightbulb_off",
    "line_chart",
    "link",
    "link_2",
    "link_2_off",
    "linkedin",
    "list",
    "list_check",
    "list_checks",
    "list_collapse",
    "list_end",
    "list_filter",
    "list_filter_plus",
    "list_minus",
    "list_music",
    "list_ordered",
    "list_plus",
    "list_restart",
    "list_start",
    "list_todo",
    "list_tree",
    "list_video",
    "list_x",
    "loader",
    "loader_circle",
    "loader_pinwheel",
    "locate",
    "locate_fixed",
    "locate_off",
    "lock",
    "lock_keyhole",
    "lock_keyhole_open",
    "lock_open",
    "log_in",
    "log_out",
    "logs",
    "lollipop",
    "luggage",
    "magnet",
    "mail",
    "mail_check",
    "mail_minus",
    "mail_open",
    "mail_plus",
    "mail_question",
    "mail_search",
    "mail_warning",
    "mail_x",
    "mailbox",
    "mails",
    "map",
    "map_pin",
    "map_pin_check",
    "map_pin_check_inside",
    "map_pin_house",
    "map_pin_minus",
    "map_pin_minus_inside",
    "map_pin_off",
    "map_pin_plus",
    "map_pin_plus_inside",
    "map_pin_x",
    "map_pin_x_inside",
    "map_pinned",
    "martini",
    "maximize",
    "maximize_2",
    "medal",
    "megaphone",
    "megaphone_off",
    "meh",
    "memory_stick",
    "menu",
    "merge",
    "message_circle",
    "message_circle_code",
    "message_circle_dashed",
    "message_circle_heart",
    "message_circle_more",
    "message_circle_off",
    "message_circle_plus",
    "message_circle_question",
    "message_circle_reply",
    "message_circle_warning",
    "message_circle_x",
    "message_square",
    "message_square_code",
    "message_square_dashed",
    "message_square_diff",
    "message_square_dot",
    "message_square_heart",
    "message_square_lock",
    "message_square_more",
    "message_square_off",
    "message_square_plus",
    "message_square_quote",
    "message_square_reply",
    "message_square_share",
    "message_square_text",
    "message_square_warning",
    "message_square_x",
    "messages_square",
    "mic",
    "mic_off",
    "mic_vocal",
    "microchip",
    "microscope",
    "microwave",
    "milestone",
    "milk",
    "milk_off",
    "minimize",
    "minimize_2",
    "minus",
    "monitor",
    "monitor_check",
    "monitor_cog",
    "monitor_dot",
    "monitor_down",
    "monitor_off",
    "monitor_pause",
    "monitor_play",
    "monitor_smartphone",
    "monitor_speaker",
    "monitor_stop",
    "monitor_up",
    "monitor_x",
    "moon",
    "moon_star",
    "mountain",
    "mountain_snow",
    "mouse",
    "mouse_off",
    "mouse_pointer",
    "mouse_pointer_2",
    "mouse_pointer_ban",
    "mouse_pointer_click",
    "move",
    "move_3d",
    "move_diagonal",
    "move_diagonal_2",
    "move_down",
    "move_down_left",
    "move_down_right",
    "move_horizontal",
    "move_left",
    "move_right",
    "move_up",
    "move_up_left",
    "move_up_right",
    "move_vertical",
    "music",
    "music_2",
    "music_3",
    "music_4",
    "navigation",
    "navigation_2",
    "navigation_2_off",
    "navigation_off",
    "network",
    "newspaper",
    "nfc",
    "notebook",
    "notebook_pen",
    "notebook_tabs",
    "notebook_text",
    "notepad_text",
    "notepad_text_dashed",
    "nut",
    "nut_off",
    "octagon",
    "octagon_alert",
    "octagon_minus",
    "octagon_pause",
    "octagon_x",
    "omega",
    "option",
    "orbit",
    "origami",
    "package",
    "package_2",
    "package_check",
    "package_minus",
    "package_open",
    "package_plus",
    "package_search",
    "package_x",
    "paint_bucket",
    "paint_roller",
    "paintbrush",
    "paintbrush_2",
    "paintbrush_vertical",
    "palette",
    "panel_bottom",
    "panel_bottom_close",
    "panel_bottom_dashed",
    "panel_bottom_open",
    "panel_left",
    "panel_left_close",
    "panel_left_dashed",
    "panel_left_open",
    "panel_right",
    "panel_right_close",
    "panel_right_dashed",
    "panel_right_open",
    "panel_top",
    "panel_top_close",
    "panel_top_dashed",
    "panel_top_open",
    "panels_left_bottom",
    "panels_right_bottom",
    "panels_top_left",
    "paperclip",
    "parentheses",
    "parking_meter",
    "party_popper",
    "pause",
    "paw_print",
    "pc_case",
    "pen",
    "pen_line",
    "pen_off",
    "pen_tool",
    "pencil",
    "pencil_line",
    "pencil_off",
    "pencil_ruler",
    "pentagon",
    "percent",
    "person_standing",
    "philippine_peso",
    "phone",
    "phone_call",
    "phone_forwarded",
    "phone_incoming",
    "phone_missed",
    "phone_off",
    "phone_outgoing",
    "pi",
    "piano",
    "pickaxe",
    "picture_in_picture",
    "picture_in_picture_2",
    "pie_chart",
    "piggy_bank",
    "pilcrow",
    "pilcrow_left",
    "pilcrow_right",
    "pill",
    "pill_bottle",
    "pin",
    "pin_off",
    "pipette",
    "pizza",
    "plane",
    "plane_landing",
    "plane_takeoff",
    "play",
    "plug",
    "plug_2",
    "plug_zap",
    "plug_zap_2",
    "plus",
    "pocket",
    "pocket_knife",
    "podcast",
    "pointer",
    "pointer_off",
    "popcorn",
    "popsicle",
    "pound_sterling",
    "power",
    "power_off",
    "presentation",
    "printer",
    "printer_check",
    "projector",
    "proportions",
    "puzzle",
    "pyramid",
    "qr_code",
    "quote",
    "rabbit",
    "radar",
    "radiation",
    "radical",
    "radio",
    "radio_receiver",
    "radio_tower",
    "radius",
    "rail_symbol",
    "rainbow",
    "rat",
    "ratio",
    "receipt",
    "receipt_cent",
    "receipt_euro",
    "receipt_indian_rupee",
    "receipt_japanese_yen",
    "receipt_pound_sterling",
    "receipt_russian_ruble",
    "receipt_swiss_franc",
    "receipt_text",
    "rectangle_ellipsis",
    "rectangle_horizontal",
    "rectangle_vertical",
    "recycle",
    "redo",
    "redo_2",
    "redo_dot",
    "refresh_ccw",
    "refresh_ccw_dot",
    "refresh_cw",
    "refresh_cw_off",
    "refrigerator",
    "regex",
    "remove_formatting",
    "repeat",
    "repeat_1",
    "repeat_2",
    "replace",
    "replace_all",
    "reply",
    "reply_all",
    "rewind",
    "ribbon",
    "rocket",
    "rocking_chair",
    "roller_coaster",
    "rotate_3d",
    "rotate_ccw",
    "rotate_ccw_square",
    "rotate_cw",
    "rotate_cw_square",
    "route",
    "route_off",
    "router",
    "rows_2",
    "rows_3",
    "rows_4",
    "rss",
    "ruler",
    "russian_ruble",
    "sailboat",
    "salad",
    "sandwich",
    "satellite",
    "satellite_dish",
    "save",
    "save_all",
    "save_off",
    "scale",
    "scale_3d",
    "scaling",
    "scan",
    "scan_barcode",
    "scan_eye",
    "scan_face",
    "scan_heart",
    "scan_line",
    "scan_qr_code",
    "scan_search",
    "scan_text",
    "scatter_chart",
    "school",
    "scissors",
    "scissors_line_dashed",
    "screen_share",
    "screen_share_off",
    "scroll",
    "scroll_text",
    "search",
    "search_check",
    "search_code",
    "search_slash",
    "search_x",
    "section",
    "send",
    "send_horizontal",
    "send_to_back",
    "separator_horizontal",
    "separator_vertical",
    "server",
    "server_cog",
    "server_crash",
    "server_off",
    "settings",
    "settings_2",
    "shapes",
    "share",
    "share_2",
    "sheet",
    "shell",
    "shield",
    "shield_alert",
    "shield_ban",
    "shield_check",
    "shield_ellipsis",
    "shield_half",
    "shield_minus",
    "shield_off",
    "shield_plus",
    "shield_question",
    "shield_x",
    "ship",
    "ship_wheel",
    "shirt",
    "shopping_bag",
    "shopping_basket",
    "shopping_cart",
    "shovel",
    "shower_head",
    "shrink",
    "shrub",
    "shuffle",
    "sigma",
    "signal",
    "signal_high",
    "signal_low",
    "signal_medium",
    "signal_zero",
    "signature",
    "signpost",
    "signpost_big",
    "siren",
    "skip_back",
    "skip_forward",
    "skull",
    "slack",
    "slash",
    "slice",
    "sliders_horizontal",
    "sliders_vertical",
    "smartphone",
    "smartphone_charging",
    "smartphone_nfc",
    "smile",
    "smile_plus",
    "snail",
    "snowflake",
    "sofa",
    "soup",
    "space",
    "spade",
    "sparkle",
    "sparkles",
    "speaker",
    "speech",
    "spell_check",
    "spell_check_2",
    "spline",
    "split",
    "spray_can",
    "sprout",
    "square",
    "square_activity",
    "square_arrow_down",
    "square_arrow_down_left",
    "square_arrow_down_right",
    "square_arrow_left",
    "square_arrow_out_down_left",
    "square_arrow_out_down_right",
    "square_arrow_out_up_left",
    "square_arrow_out_up_right",
    "square_arrow_right",
    "square_arrow_up",
    "square_arrow_up_left",
    "square_arrow_up_right",
    "square_asterisk",
    "square_bottom_dashed_scissors",
    "square_chart_gantt",
    "square_check",
    "square_check_big",
    "square_chevron_down",
    "square_chevron_left",
    "square_chevron_right",
    "square_chevron_up",
    "square_code",
    "square_dashed",
    "square_dashed_bottom",
    "square_dashed_bottom_code",
    "square_dashed_kanban",
    "square_dashed_mouse_pointer",
    "square_divide",
    "square_dot",
    "square_equal",
    "square_function",
    "square_gantt_chart",
    "square_kanban",
    "square_library",
    "square_m",
    "square_menu",
    "square_minus",
    "square_mouse_pointer",
    "square_parking",
    "square_parking_off",
    "square_pen",
    "square_percent",
    "square_pi",
    "square_pilcrow",
    "square_play",
    "square_plus",
    "square_power",
    "square_radical",
    "square_scissors",
    "square_sigma",
    "square_slash",
    "square_split_horizontal",
    "square_split_vertical",
    "square_square",
    "square_stack",
    "square_terminal",
    "square_user",
    "square_user_round",
    "square_x",
    "squircle",
    "squirrel",
    "stamp",
    "star",
    "star_half",
    "star_off",
    "step_back",
    "step_forward",
    "stethoscope",
    "sticker",
    "sticky_note",
    "store",
    "stretch_horizontal",
    "stretch_vertical",
    "strikethrough",
    "subscript",
    "sun",
    "sun_dim",
    "sun_medium",
    "sun_moon",
    "sun_snow",
    "sunrise",
    "sunset",
    "superscript",
    "swatch_book",
    "swiss_franc",
    "switch_camera",
    "sword",
    "swords",
    "syringe",
    "table",
    "table_2",
    "table_cells_merge",
    "table_cells_split",
    "table_columns_split",
    "table_of_contents",
    "table_properties",
    "table_rows_split",
    "tablet",
    "tablet_smartphone",
    "tablets",
    "tag",
    "tags",
    "tally_1",
    "tally_2",
    "tally_3",
    "tally_4",
    "tally_5",
    "tangent",
    "target",
    "telescope",
    "tent",
    "tent_tree",
    "terminal",
    "test_tube",
    "test_tube_diagonal",
    "test_tubes",
    "text",
    "text_cursor",
    "text_cursor_input",
    "text_quote",
    "text_search",
    "text_select",
    "theater",
    "thermometer",
    "thermometer_snowflake",
    "thermometer_sun",
    "thumbs_down",
    "thumbs_up",
    "ticket",
    "ticket_check",
    "ticket_minus",
    "ticket_percent",
    "ticket_plus",
    "ticket_slash",
    "ticket_x",
    "tickets",
    "tickets_plane",
    "timer",
    "timer_off",
    "timer_reset",
    "toggle_left",
    "toggle_right",
    "toilet",
    "tornado",
    "torus",
    "touchpad",
    "touchpad_off",
    "tower_control",
    "toy_brick",
    "tractor",
    "traffic_cone",
    "train_front",
    "train_front_tunnel",
    "train_track",
    "tram_front",
    "trash",
    "trash_2",
    "tree_deciduous",
    "tree_palm",
    "tree_pine",
    "trees",
    "trello",
    "trending_down",
    "trending_up",
    "trending_up_down",
    "triangle",
    "triangle_alert",
    "triangle_dashed",
    "triangle_right",
    "trophy",
    "truck",
    "turtle",
    "tv",
    "tv_2",
    "tv_minimal",
    "tv_minimal_play",
    "twitch",
    "twitter",
    "type",
    "type_outline",
    "umbrella",
    "umbrella_off",
    "underline",
    "undo",
    "undo_2",
    "undo_dot",
    "unfold_horizontal",
    "unfold_vertical",
    "ungroup",
    "university",
    "unlink",
    "unlink_2",
    "unplug",
    "upload",
    "usb",
    "user",
    "user_check",
    "user_cog",
    "user_minus",
    "user_pen",
    "user_plus",
    "user_round",
    "user_round_check",
    "user_round_cog",
    "user_round_minus",
    "user_round_pen",
    "user_round_plus",
    "user_round_search",
    "user_round_x",
    "user_search",
    "user_x",
    "users",
    "users_round",
    "utensils",
    "utensils_crossed",
    "utility_pole",
    "variable",
    "vault",
    "vegan",
    "venetian_mask",
    "vibrate",
    "vibrate_off",
    "video",
    "video_off",
    "videotape",
    "view",
    "voicemail",
    "volleyball",
    "volume",
    "volume_1",
    "volume_2",
    "volume_off",
    "volume_x",
    "vote",
    "wallet",
    "wallet_cards",
    "wallet_minimal",
    "wallpaper",
    "wand",
    "wand_sparkles",
    "warehouse",
    "washing_machine",
    "watch",
    "waves",
    "waves_ladder",
    "waypoints",
    "webcam",
    "webhook",
    "webhook_off",
    "weight",
    "wheat",
    "wheat_off",
    "whole_word",
    "wifi",
    "wifi_high",
    "wifi_low",
    "wifi_off",
    "wifi_zero",
    "wind",
    "wind_arrow_down",
    "wine",
    "wine_off",
    "workflow",
    "worm",
    "wrap_text",
    "wrench",
    "x",
    "youtube",
    "zap",
    "zap_off",
    "zoom_in",
    "zoom_out",
]

# The default transformation of some icon names doesn't match how the
# icons are exported from Lucide. Manual overrides can go here.
LUCIDE_ICON_MAPPING_OVERRIDE = {
    "grid_2x_2_check": "Grid2x2Check",
    "grid_2x_2_x": "Grid2x2X",
}
