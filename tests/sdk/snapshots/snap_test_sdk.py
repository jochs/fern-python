# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot
from snapshottest.file import FileSnapshot


snapshots = Snapshot()

snapshots['test_github_sdk filepaths'] = [
    'src/fern/__init__.py',
    'src/fern/client.py',
    'src/fern/core/__init__.py',
    'src/fern/core/api_error.py',
    'src/fern/core/datetime_utils.py',
    'src/fern/core/jsonable_encoder.py',
    'src/fern/core/remove_none_from_headers.py',
    'src/fern/resources/__init__.py',
    'src/fern/resources/movie/__init__.py',
    'src/fern/resources/movie/client.py',
    'src/fern/resources/movie/errors/__init__.py',
    'src/fern/resources/movie/errors/invalid_movie_error.py',
    'src/fern/resources/movie/errors/movie_already_exists_error.py',
    'src/fern/resources/movie/errors/movie_not_found_error.py',
    'src/fern/resources/movie/types/__init__.py',
    'src/fern/resources/movie/types/movie.py',
    'src/fern/resources/movie/types/movie_id.py'
]

snapshots['test_github_sdk src_fern___init__'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern___init__.py')

snapshots['test_github_sdk src_fern_client'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_client.py')

snapshots['test_github_sdk src_fern_core___init__'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_core___init__.py')

snapshots['test_github_sdk src_fern_core_api_error'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_core_api_error.py')

snapshots['test_github_sdk src_fern_core_datetime_utils'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_core_datetime_utils.py')

snapshots['test_github_sdk src_fern_core_jsonable_encoder'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_core_jsonable_encoder.py')

snapshots['test_github_sdk src_fern_core_remove_none_from_headers'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_core_remove_none_from_headers.py')

snapshots['test_github_sdk src_fern_resources___init__'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources___init__.py')

snapshots['test_github_sdk src_fern_resources_movie___init__'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie___init__.py')

snapshots['test_github_sdk src_fern_resources_movie_client'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie_client.py')

snapshots['test_github_sdk src_fern_resources_movie_errors___init__'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie_errors___init__.py')

snapshots['test_github_sdk src_fern_resources_movie_errors_invalid_movie_error'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie_errors_invalid_movie_error.py')

snapshots['test_github_sdk src_fern_resources_movie_errors_movie_already_exists_error'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie_errors_movie_already_exists_error.py')

snapshots['test_github_sdk src_fern_resources_movie_errors_movie_not_found_error'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie_errors_movie_not_found_error.py')

snapshots['test_github_sdk src_fern_resources_movie_types___init__'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie_types___init__.py')

snapshots['test_github_sdk src_fern_resources_movie_types_movie'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie_types_movie.py')

snapshots['test_github_sdk src_fern_resources_movie_types_movie_id'] = FileSnapshot('snap_test_sdk/test_github_sdk src_fern_resources_movie_types_movie_id.py')
