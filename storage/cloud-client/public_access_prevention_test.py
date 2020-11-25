# Copyright 2019 Google Inc. All Rights Reserved.
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

import storage_get_public_access_prevention
import storage_set_public_access_prevention_enforced
import storage_set_public_access_prevention_unspecified


def test_get_public_access_prevention(bucket, capsys):
    short_name = storage_get_public_access_prevention
    short_name.get_public_access_prevention(
        bucket.name
    )
    out, _ = capsys.readouterr()
    assert (
        "Public access prevention is unspecified for {}.".format(bucket.name)
        in out
    )


def test_set_public_access_prevention_enforced(bucket, capsys):
    short_name = storage_set_public_access_prevention_enforced
    short_name.set_public_access_prevention_enforced(
        bucket.name
    )
    out, _ = capsys.readouterr()
    assert (
        "Public access prevention is set to enforced for {}.".format(bucket.name)
        in out
    )


def test_set_public_access_prevention_unspecified(bucket, capsys):
    short_name = storage_set_public_access_prevention_unspecified
    short_name.set_public_access_prevention_unspecified(
        bucket.name
    )
    out, _ = capsys.readouterr()
    assert (
        "Public access prevention is 'unspecified' for {}.".format(bucket.name)
        in out
    )