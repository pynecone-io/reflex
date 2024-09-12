"""Element classes. This is an auto-generated file. Do not edit. See ../generate.py."""

from typing import Any, Union

from reflex import Component, ComponentNamespace
from reflex.constants.colors import Color
from reflex.ivars.base import ImmutableVar
from reflex.vars import Var as Var

from .base import BaseHTML


class Area(BaseHTML):
    """Display the area element."""

    tag = "area"

    # Alternate text for the area, used for accessibility
    alt: ImmutableVar[Union[str, int, bool]]

    # Coordinates to define the shape of the area
    coords: ImmutableVar[Union[str, int, bool]]

    # Specifies that the target will be downloaded when clicked
    download: ImmutableVar[Union[str, int, bool]]

    # Hyperlink reference for the area
    href: ImmutableVar[Union[str, int, bool]]

    # Language of the linked resource
    href_lang: ImmutableVar[Union[str, int, bool]]

    # Specifies what media/device the linked resource is optimized for
    media: ImmutableVar[Union[str, int, bool]]

    # A list of URLs to be notified if the user follows the hyperlink
    ping: ImmutableVar[Union[str, int, bool]]

    # Specifies which referrer information to send with the link
    referrer_policy: ImmutableVar[Union[str, int, bool]]

    # Specifies the relationship of the target object to the link object
    rel: ImmutableVar[Union[str, int, bool]]

    # Defines the shape of the area (rectangle, circle, polygon)
    shape: ImmutableVar[Union[str, int, bool]]

    # Specifies where to open the linked document
    target: ImmutableVar[Union[str, int, bool]]


class Audio(BaseHTML):
    """Display the audio element."""

    tag = "audio"

    # Specifies that the audio will start playing as soon as it is ready
    auto_play: ImmutableVar[Union[str, int, bool]]

    # Represents the time range of the buffered media
    buffered: ImmutableVar[Union[str, int, bool]]

    # Displays the standard audio controls
    controls: ImmutableVar[Union[str, int, bool]]

    # Configures the CORS requests for the element
    cross_origin: ImmutableVar[Union[str, int, bool]]

    # Specifies that the audio will loop
    loop: ImmutableVar[Union[str, int, bool]]

    # Indicates whether the audio is muted by default
    muted: ImmutableVar[Union[str, int, bool]]

    # Specifies how the audio file should be preloaded
    preload: ImmutableVar[Union[str, int, bool]]

    # URL of the audio to play
    src: ImmutableVar[Union[str, int, bool]]


class Img(BaseHTML):
    """Display the img element."""

    tag = "img"

    # Image alignment with respect to its surrounding elements
    align: ImmutableVar[Union[str, int, bool]]

    # Alternative text for the image
    alt: ImmutableVar[Union[str, int, bool]]

    # Configures the CORS requests for the image
    cross_origin: ImmutableVar[Union[str, int, bool]]

    # How the image should be decoded
    decoding: ImmutableVar[Union[str, int, bool]]

    # Specifies an intrinsic size for the image
    intrinsicsize: ImmutableVar[Union[str, int, bool]]

    # Whether the image is a server-side image map
    ismap: ImmutableVar[Union[str, int, bool]]

    # Specifies the loading behavior of the image
    loading: ImmutableVar[Union[str, int, bool]]

    # Referrer policy for the image
    referrer_policy: ImmutableVar[Union[str, int, bool]]

    # Sizes of the image for different layouts
    sizes: ImmutableVar[Union[str, int, bool]]

    # URL of the image to display
    src: ImmutableVar[Any]

    # A set of source sizes and URLs for responsive images
    src_set: ImmutableVar[Union[str, int, bool]]

    # The name of the map to use with the image
    use_map: ImmutableVar[Union[str, int, bool]]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Override create method to apply source attribute to value if user fails to pass in attribute.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        """
        return (
            super().create(src=children[0], **props)
            if children
            else super().create(*children, **props)
        )


class Map(BaseHTML):
    """Display the map element."""

    tag = "map"

    # Name of the map, referenced by the 'usemap' attribute in 'img' and 'object' elements
    name: ImmutableVar[Union[str, int, bool]]


class Track(BaseHTML):
    """Display the track element."""

    tag = "track"

    # Indicates that the track should be enabled unless the user's preferences indicate otherwise
    default: ImmutableVar[Union[str, int, bool]]

    # Specifies the kind of text track
    kind: ImmutableVar[Union[str, int, bool]]

    # Title of the text track, used by the browser when listing available text tracks
    label: ImmutableVar[Union[str, int, bool]]

    # URL of the track file
    src: ImmutableVar[Union[str, int, bool]]

    # Language of the track text data
    src_lang: ImmutableVar[Union[str, int, bool]]


class Video(BaseHTML):
    """Display the video element."""

    tag = "video"

    # Specifies that the video will start playing as soon as it is ready
    auto_play: ImmutableVar[Union[str, int, bool]]

    # Represents the time range of the buffered media
    buffered: ImmutableVar[Union[str, int, bool]]

    # Displays the standard video controls
    controls: ImmutableVar[Union[str, int, bool]]

    # Configures the CORS requests for the video
    cross_origin: ImmutableVar[Union[str, int, bool]]

    # Specifies that the video will loop
    loop: ImmutableVar[Union[str, int, bool]]

    # Indicates whether the video is muted by default
    muted: ImmutableVar[Union[str, int, bool]]

    # Indicates that the video should play 'inline', inside its element's playback area
    plays_inline: ImmutableVar[Union[str, int, bool]]

    # URL of an image to show while the video is downloading, or until the user hits the play button
    poster: ImmutableVar[Union[str, int, bool]]

    # Specifies how the video file should be preloaded
    preload: ImmutableVar[Union[str, int, bool]]

    # URL of the video to play
    src: ImmutableVar[Union[str, int, bool]]


class Embed(BaseHTML):
    """Display the embed element."""

    tag = "embed"

    # URL of the embedded content
    src: ImmutableVar[Union[str, int, bool]]

    # Media type of the embedded content
    type: ImmutableVar[Union[str, int, bool]]


class Iframe(BaseHTML):
    """Display the iframe element."""

    tag = "iframe"

    # Alignment of the iframe within the page or surrounding elements
    align: ImmutableVar[Union[str, int, bool]]

    # Permissions policy for the iframe
    allow: ImmutableVar[Union[str, int, bool]]

    # Content Security Policy to apply to the iframe's content
    csp: ImmutableVar[Union[str, int, bool]]

    # Specifies the loading behavior of the iframe
    loading: ImmutableVar[Union[str, int, bool]]

    # Name of the iframe, used as a target for hyperlinks and forms
    name: ImmutableVar[Union[str, int, bool]]

    # Referrer policy for the iframe
    referrer_policy: ImmutableVar[Union[str, int, bool]]

    # Security restrictions for the content in the iframe
    sandbox: ImmutableVar[Union[str, int, bool]]

    # URL of the document to display in the iframe
    src: ImmutableVar[Union[str, int, bool]]

    # HTML content to embed directly within the iframe
    src_doc: ImmutableVar[Union[str, int, bool]]


class Object(BaseHTML):
    """Display the object element."""

    tag = "object"

    # URL of the data to be used by the object
    data: ImmutableVar[Union[str, int, bool]]

    # Associates the object with a form element
    form: ImmutableVar[Union[str, int, bool]]

    # Name of the object, used for scripting or as a target for forms and links
    name: ImmutableVar[Union[str, int, bool]]

    # Media type of the data specified in the data attribute
    type: ImmutableVar[Union[str, int, bool]]

    # Name of an image map to use with the object
    use_map: ImmutableVar[Union[str, int, bool]]


class Picture(BaseHTML):
    """Display the picture element."""

    tag = "picture"
    # No unique attributes, only common ones are inherited


class Portal(BaseHTML):
    """Display the portal element."""

    tag = "portal"
    # No unique attributes, only common ones are inherited


class Source(BaseHTML):
    """Display the source element."""

    tag = "source"

    # Media query indicating what device the linked resource is optimized for
    media: ImmutableVar[Union[str, int, bool]]

    # Sizes of the source for different layouts
    sizes: ImmutableVar[Union[str, int, bool]]

    # URL of the media file or an image for the element to use
    src: ImmutableVar[Union[str, int, bool]]

    # A set of source sizes and URLs for responsive images
    src_set: ImmutableVar[Union[str, int, bool]]

    # Media type of the source
    type: ImmutableVar[Union[str, int, bool]]


class Svg(BaseHTML):
    """Display the svg element."""

    tag = "svg"
    # The width of the svg.
    width: ImmutableVar[Union[str, int]]
    # The height of the svg.
    height: ImmutableVar[Union[str, int]]
    # The XML namespace declaration.
    xmlns: ImmutableVar[str]


class Circle(BaseHTML):
    """The SVG circle component."""

    tag = "circle"
    # The x-axis coordinate of the center of the circle.
    cx: ImmutableVar[Union[str, int]]
    # The y-axis coordinate of the center of the circle.
    cy: ImmutableVar[Union[str, int]]
    # The radius of the circle.
    r: ImmutableVar[Union[str, int]]
    # The total length for the circle's circumference, in user units.
    path_length: ImmutableVar[int]


class Rect(BaseHTML):
    """The SVG rect component."""

    tag = "rect"
    # The x coordinate of the rect.
    x: ImmutableVar[Union[str, int]]
    # The y coordinate of the rect.
    y: ImmutableVar[Union[str, int]]
    # The width of the rect
    width: ImmutableVar[Union[str, int]]
    # The height of the rect.
    height: ImmutableVar[Union[str, int]]
    # The horizontal corner radius of the rect. Defaults to ry if it is specified.
    rx: ImmutableVar[Union[str, int]]
    # The vertical corner radius of the rect. Defaults to rx if it is specified.
    ry: ImmutableVar[Union[str, int]]
    # The total length of the rectangle's perimeter, in user units.
    path_length: ImmutableVar[int]


class Polygon(BaseHTML):
    """The SVG polygon component."""

    tag = "polygon"
    # defines the list of points (pairs of x,y absolute coordinates) required to draw the polygon.
    points: ImmutableVar[str]
    # This prop lets specify the total length for the path, in user units.
    path_length: ImmutableVar[int]


class Defs(BaseHTML):
    """Display the defs element."""

    tag = "defs"


class LinearGradient(BaseHTML):
    """Display the linearGradient element."""

    tag = "linearGradient"

    # Units for the gradient.
    gradient_units: ImmutableVar[Union[str, bool]]

    # Transform applied to the gradient.
    gradient_transform: ImmutableVar[Union[str, bool]]

    # Method used to spread the gradient.
    spread_method: ImmutableVar[Union[str, bool]]

    # X coordinate of the starting point of the gradient.
    x1: ImmutableVar[Union[str, int, bool]]

    # X coordinate of the ending point of the gradient.
    x2: ImmutableVar[Union[str, int, bool]]

    # Y coordinate of the starting point of the gradient.
    y1: ImmutableVar[Union[str, int, bool]]

    # Y coordinate of the ending point of the gradient.
    y2: ImmutableVar[Union[str, int, bool]]


class Stop(BaseHTML):
    """Display the stop element."""

    tag = "stop"

    # Offset of the gradient stop.
    offset: ImmutableVar[Union[str, float, int]]

    # Color of the gradient stop.
    stop_color: ImmutableVar[Union[str, Color, bool]]

    # Opacity of the gradient stop.
    stop_opacity: ImmutableVar[Union[str, float, int, bool]]


class Path(BaseHTML):
    """Display the path element."""

    tag = "path"

    # Defines the shape of the path.
    d: ImmutableVar[Union[str, int, bool]]


class SVG(ComponentNamespace):
    """SVG component namespace."""

    circle = staticmethod(Circle.create)
    rect = staticmethod(Rect.create)
    polygon = staticmethod(Polygon.create)
    path = staticmethod(Path.create)
    stop = staticmethod(Stop.create)
    linear_gradient = staticmethod(LinearGradient.create)
    defs = staticmethod(Defs.create)
    __call__ = staticmethod(Svg.create)


area = Area.create
audio = Audio.create
image = img = Img.create
map = Map.create
track = Track.create
video = Video.create
embed = Embed.create
iframe = Iframe.create
object = Object.create
picture = Picture.create
portal = Portal.create
source = Source.create
svg = SVG()
