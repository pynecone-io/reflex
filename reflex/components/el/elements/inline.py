"""Element classes. This is an auto-generated file. Do not edit. See ../generate.py."""

from typing import Union

from reflex.ivars.base import ImmutableVar

from .base import BaseHTML


class A(BaseHTML):  # Inherits common attributes from BaseMeta
    """Display the 'a' element."""

    tag = "a"

    # Specifies that the target (the file specified in the href attribute) will be downloaded when a user clicks on the hyperlink.
    download: ImmutableVar[Union[str, int, bool]]

    # Specifies the URL of the page the link goes to
    href: ImmutableVar[Union[str, int, bool]]

    # Specifies the language of the linked document
    href_lang: ImmutableVar[Union[str, int, bool]]

    # Specifies what media/device the linked document is optimized for
    media: ImmutableVar[Union[str, int, bool]]

    # Specifies which referrer is sent when fetching the resource
    ping: ImmutableVar[Union[str, int, bool]]

    # Specifies the relationship between the current document and the linked document
    referrer_policy: ImmutableVar[Union[str, int, bool]]

    # Specifies the relationship between the linked document and the current document
    rel: ImmutableVar[Union[str, int, bool]]

    # Specifies the shape of the area
    shape: ImmutableVar[Union[str, int, bool]]

    # Specifies where to open the linked document
    target: ImmutableVar[Union[str, int, bool]]


class Abbr(BaseHTML):
    """Display the abbr element."""

    tag = "abbr"


class B(BaseHTML):
    """Display the b element."""

    tag = "b"


class Bdi(BaseHTML):
    """Display the bdi element."""

    tag = "bdi"


class Bdo(BaseHTML):
    """Display the bdo element."""

    tag = "bdo"


class Br(BaseHTML):
    """Display the br element."""

    tag = "br"


class Cite(BaseHTML):
    """Display the cite element."""

    tag = "cite"


class Code(BaseHTML):
    """Display the code element."""

    tag = "code"


class Data(BaseHTML):
    """Display the data element."""

    tag = "data"

    # Specifies the machine-readable translation of the data element.
    value: ImmutableVar[Union[str, int, bool]]


class Dfn(BaseHTML):
    """Display the dfn element."""

    tag = "dfn"


class Em(BaseHTML):
    """Display the em element."""

    tag = "em"


class I(BaseHTML):  # noqa: E742
    """Display the i element."""

    tag = "i"


class Kbd(BaseHTML):
    """Display the kbd element."""

    tag = "kbd"


class Mark(BaseHTML):
    """Display the mark element."""

    tag = "mark"


class Q(BaseHTML):
    """Display the q element."""

    tag = "q"

    # Specifies the source URL of the quote.
    cite: ImmutableVar[Union[str, int, bool]]


class Rp(BaseHTML):
    """Display the rp element."""

    tag = "rp"


class Rt(BaseHTML):
    """Display the rt element."""

    tag = "rt"


class Ruby(BaseHTML):
    """Display the ruby element."""

    tag = "ruby"


class S(BaseHTML):
    """Display the s element."""

    tag = "s"


class Samp(BaseHTML):
    """Display the samp element."""

    tag = "samp"


class Small(BaseHTML):
    """Display the small element."""

    tag = "small"


class Span(BaseHTML):
    """Display the span element."""

    tag = "span"


class Strong(BaseHTML):
    """Display the strong element."""

    tag = "strong"


class Sub(BaseHTML):
    """Display the sub element."""

    tag = "sub"


class Sup(BaseHTML):
    """Display the sup element."""

    tag = "sup"


class Time(BaseHTML):
    """Display the time element."""

    tag = "time"

    # Specifies the date and/or time of the element.
    date_time: ImmutableVar[Union[str, int, bool]]


class U(BaseHTML):
    """Display the u element."""

    tag = "u"


class Wbr(BaseHTML):
    """Display the wbr element."""

    tag = "wbr"


a = A.create
abbr = Abbr.create
b = B.create
bdi = Bdi.create
bdo = Bdo.create
br = Br.create
cite = Cite.create
code = Code.create
data = Data.create
dfn = Dfn.create
em = Em.create
i = I.create
kbd = Kbd.create
mark = Mark.create
q = Q.create
rp = Rp.create
rt = Rt.create
ruby = Ruby.create
s = S.create
samp = Samp.create
small = Small.create
span = Span.create
strong = Strong.create
sub = Sub.create
sup = Sup.create
time = Time.create
u = U.create
wbr = Wbr.create
