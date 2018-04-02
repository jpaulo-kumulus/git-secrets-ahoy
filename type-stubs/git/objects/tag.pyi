# Stubs for git.objects.tag (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import base
from typing import Any, Optional

class TagObject(base.Object):
    type: str = ...
    object: Any = ...
    tag: Any = ...
    tagger: Any = ...
    tagged_date: Any = ...
    tagger_tz_offset: Any = ...
    message: Any = ...
    def __init__(self, repo, binsha, object: Optional[Any] = ..., tag: Optional[Any] = ..., tagger: Optional[Any] = ..., tagged_date: Optional[Any] = ..., tagger_tz_offset: Optional[Any] = ..., message: Optional[Any] = ...) -> None: ...
