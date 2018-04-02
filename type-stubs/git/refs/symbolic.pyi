# Stubs for git.refs.symbolic (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, overload

class SymbolicReference:
    repo: Any = ...
    path: Any = ...
    def __init__(self, repo, path) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    @property
    def name(self): ...
    @property
    def abspath(self): ...
    @classmethod
    def dereference_recursive(cls, repo, ref_path): ...
    def set_commit(self, commit, logmsg: Optional[Any] = ...): ...
    def set_object(self, object, logmsg: Optional[Any] = ...): ...
    commit: Any = ...
    object: Any = ...
    def set_reference(self, ref, logmsg: Optional[Any] = ...): ...
    reference: Any = ...
    ref: Any = ...
    def is_valid(self): ...
    @property
    def is_detached(self): ...
    def log(self): ...
    def log_append(self, oldbinsha, message, newbinsha: Optional[Any] = ...): ...
    def log_entry(self, index): ...
    @classmethod
    def to_full_path(cls, path): ...
    @classmethod
    def delete(cls, repo, path) -> None: ...
    @classmethod
    def create(cls, repo, path, **kargs): ...
    # @classmethod
    # def create(cls, repo, path, reference: str = ..., force: bool = ..., logmsg: Optional[Any] = ...): ...
    def rename(self, new_path, force: bool = ...): ...
    @classmethod
    def iter_items(cls, repo, common_path: Optional[Any] = ..., *args, **kwargs): ...
    @classmethod
    def from_path(cls, repo, path): ...
    def is_remote(self): ...