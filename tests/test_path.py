# Copyright 2020 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from v3iofs import path as v3path

import pytest


split_cases = [
    # path, expected, raises
    ("", None, True),
    ("/", ("", ""), False),
    ("/a", ("a", ""), False),
    ("/a/b/c", ("a", "b/c"), False),
]


@pytest.mark.parametrize("path, expected, raises", split_cases)
def test_split_container(path, expected, raises):
    if raises:
        with pytest.raises(ValueError):
            v3path.split_container(path)
        return

    out = v3path.split_container(path)
    assert expected == tuple(out), "split"


unslash_cases = [
    # path, expected
    ("", ""),
    ("/", ""),
    ("/a", "/a"),
    ("/a/", "/a"),
]


@pytest.mark.parametrize("path, expected", unslash_cases)
def test_unslash(path, expected):
    out = v3path.unslash(path)
    assert out == expected
