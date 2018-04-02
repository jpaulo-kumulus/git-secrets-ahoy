# Stubs for git.cmd (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .util import LazyMixin
from typing import Any, Optional

class Git(LazyMixin):
    max_chunk_size: Any = ...
    git_exec_name: str = ...
    GIT_PYTHON_TRACE: Any = ...
    USE_SHELL: bool = ...
    GIT_PYTHON_GIT_EXECUTABLE: Any = ...
    @classmethod
    def refresh(cls, path: Optional[Any] = ...): ...
    @classmethod
    def is_cygwin(cls): ...
    @classmethod
    def polish_url(cls, url, is_cygwin: Optional[Any] = ...): ...
    class AutoInterrupt:
        proc: Any = ...
        args: Any = ...
        def __init__(self, proc, args) -> None: ...
        def __del__(self): ...
        def __getattr__(self, attr): ...
        def wait(self, stderr: bytes = ...): ...
    class CatFileContentStream:
        def __init__(self, size, stream) -> None: ...
        def read(self, size: int = ...): ...
        def readline(self, size: int = ...): ...
        def readlines(self, size: int = ...): ...
        def __iter__(self): ...
        def next(self): ...
        def __del__(self) -> None: ...
    cat_file_header: Any = ...
    cat_file_all: Any = ...
    def __init__(self, working_dir: Optional[Any] = ...) -> None: ...
    def __getattr__(self, name): ...
    def set_persistent_git_options(self, **kwargs) -> None: ...
    @property
    def working_dir(self): ...
    @property
    def version_info(self): ...
    def execute(self, command, istream: Optional[Any] = ..., with_extended_output: bool = ..., with_exceptions: bool = ..., as_process: bool = ..., output_stream: Optional[Any] = ..., stdout_as_string: bool = ..., kill_after_timeout: Optional[Any] = ..., with_stdout: bool = ..., universal_newlines: bool = ..., shell: Optional[Any] = ..., env: Optional[Any] = ..., **subprocess_kwargs): ...
    def environment(self): ...
    def update_environment(self, **kwargs): ...
    def custom_environment(self, **kwargs) -> None: ...
    def transform_kwarg(self, name, value, split_single_char_options): ...
    def transform_kwargs(self, split_single_char_options: bool = ..., **kwargs): ...
    def __call__(self, **kwargs): ...
    def get_object_header(self, ref): ...
    def get_object_data(self, ref): ...
    def stream_object_data(self, ref): ...
    def clear_cache(self): ...
