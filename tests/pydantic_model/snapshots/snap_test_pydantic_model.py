# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot
from snapshottest.file import FileSnapshot


snapshots = Snapshot()

snapshots['test_pydantic_model filepaths'] = [
    'src/fern/__init__.py',
    'src/fern/admin/__init__.py',
    'src/fern/admin/store_traced_test_case_request.py',
    'src/fern/admin/store_traced_workspace_request.py',
    'src/fern/commons/__init__.py',
    'src/fern/commons/binary_tree_node_and_tree_value.py',
    'src/fern/commons/binary_tree_node_value.py',
    'src/fern/commons/binary_tree_value.py',
    'src/fern/commons/debug_key_value_pairs.py',
    'src/fern/commons/debug_map_value.py',
    'src/fern/commons/debug_variable_value.py',
    'src/fern/commons/doubly_linked_list_node_and_list_value.py',
    'src/fern/commons/doubly_linked_list_node_value.py',
    'src/fern/commons/doubly_linked_list_value.py',
    'src/fern/commons/file_info.py',
    'src/fern/commons/generic_value.py',
    'src/fern/commons/key_value_pair.py',
    'src/fern/commons/language.py',
    'src/fern/commons/list_type.py',
    'src/fern/commons/map_type.py',
    'src/fern/commons/map_value.py',
    'src/fern/commons/node_id.py',
    'src/fern/commons/problem_id.py',
    'src/fern/commons/singly_linked_list_node_and_list_value.py',
    'src/fern/commons/singly_linked_list_node_value.py',
    'src/fern/commons/singly_linked_list_value.py',
    'src/fern/commons/test_case.py',
    'src/fern/commons/test_case_with_expected_result.py',
    'src/fern/commons/user_id.py',
    'src/fern/commons/variable_type.py',
    'src/fern/commons/variable_value.py',
    'src/fern/lang_server/__init__.py',
    'src/fern/lang_server/lang_server_request.py',
    'src/fern/lang_server/lang_server_response.py',
    'src/fern/migration/__init__.py',
    'src/fern/migration/migration.py',
    'src/fern/migration/migration_status.py',
    'src/fern/playlist/__init__.py',
    'src/fern/playlist/playlist.py',
    'src/fern/playlist/playlist_create_request.py',
    'src/fern/playlist/playlist_id.py',
    'src/fern/playlist/update_playlist_request.py',
    'src/fern/problem/__init__.py',
    'src/fern/problem/create_problem_error.py',
    'src/fern/problem/create_problem_request.py',
    'src/fern/problem/create_problem_response.py',
    'src/fern/problem/generic_create_problem_error.py',
    'src/fern/problem/get_default_starter_files_request.py',
    'src/fern/problem/get_default_starter_files_response.py',
    'src/fern/problem/problem_description.py',
    'src/fern/problem/problem_description_board.py',
    'src/fern/problem/problem_files.py',
    'src/fern/problem/problem_info.py',
    'src/fern/problem/update_problem_response.py',
    'src/fern/problem/variable_type_and_name.py',
    'src/fern/submission/__init__.py',
    'src/fern/submission/actual_result.py',
    'src/fern/submission/building_executor_response.py',
    'src/fern/submission/code_execution_update.py',
    'src/fern/submission/compile_error.py',
    'src/fern/submission/custom_test_cases_unsupported.py',
    'src/fern/submission/error_info.py',
    'src/fern/submission/errored_response.py',
    'src/fern/submission/exception_info.py',
    'src/fern/submission/exception_v_2.py',
    'src/fern/submission/execution_session_response.py',
    'src/fern/submission/execution_session_state.py',
    'src/fern/submission/execution_session_status.py',
    'src/fern/submission/existing_submission_executing.py',
    'src/fern/submission/expression_location.py',
    'src/fern/submission/finished_response.py',
    'src/fern/submission/get_execution_session_state_response.py',
    'src/fern/submission/get_submission_state_response.py',
    'src/fern/submission/get_trace_responses_page_request.py',
    'src/fern/submission/graded_response.py',
    'src/fern/submission/graded_response_v_2.py',
    'src/fern/submission/graded_test_case_update.py',
    'src/fern/submission/initialize_problem_request.py',
    'src/fern/submission/internal_error.py',
    'src/fern/submission/invalid_request_cause.py',
    'src/fern/submission/invalid_request_response.py',
    'src/fern/submission/lightweight_stackframe_information.py',
    'src/fern/submission/recorded_response_notification.py',
    'src/fern/submission/recorded_test_case_update.py',
    'src/fern/submission/recording_response_notification.py',
    'src/fern/submission/running_response.py',
    'src/fern/submission/running_submission_state.py',
    'src/fern/submission/runtime_error.py',
    'src/fern/submission/scope.py',
    'src/fern/submission/share_id.py',
    'src/fern/submission/stack_frame.py',
    'src/fern/submission/stack_information.py',
    'src/fern/submission/stderr_response.py',
    'src/fern/submission/stdout_response.py',
    'src/fern/submission/stop_request.py',
    'src/fern/submission/stopped_response.py',
    'src/fern/submission/submission_file_info.py',
    'src/fern/submission/submission_id.py',
    'src/fern/submission/submission_id_not_found.py',
    'src/fern/submission/submission_request.py',
    'src/fern/submission/submission_response.py',
    'src/fern/submission/submission_status_for_test_case.py',
    'src/fern/submission/submission_status_v_2.py',
    'src/fern/submission/submission_type_enum.py',
    'src/fern/submission/submission_type_state.py',
    'src/fern/submission/submit_request_v_2.py',
    'src/fern/submission/terminated_response.py',
    'src/fern/submission/test_case_grade.py',
    'src/fern/submission/test_case_hidden_grade.py',
    'src/fern/submission/test_case_non_hidden_grade.py',
    'src/fern/submission/test_case_result.py',
    'src/fern/submission/test_case_result_with_stdout.py',
    'src/fern/submission/test_submission_state.py',
    'src/fern/submission/test_submission_status.py',
    'src/fern/submission/test_submission_status_v_2.py',
    'src/fern/submission/test_submission_update.py',
    'src/fern/submission/test_submission_update_info.py',
    'src/fern/submission/trace_response.py',
    'src/fern/submission/trace_response_v_2.py',
    'src/fern/submission/trace_responses_page.py',
    'src/fern/submission/trace_responses_page_v_2.py',
    'src/fern/submission/traced_file.py',
    'src/fern/submission/traced_test_case.py',
    'src/fern/submission/unexpected_language_error.py',
    'src/fern/submission/workspace_files.py',
    'src/fern/submission/workspace_ran_response.py',
    'src/fern/submission/workspace_run_details.py',
    'src/fern/submission/workspace_starter_files_response.py',
    'src/fern/submission/workspace_starter_files_response_v_2.py',
    'src/fern/submission/workspace_submission_state.py',
    'src/fern/submission/workspace_submission_status.py',
    'src/fern/submission/workspace_submission_status_v_2.py',
    'src/fern/submission/workspace_submission_update.py',
    'src/fern/submission/workspace_submission_update_info.py',
    'src/fern/submission/workspace_submit_request.py',
    'src/fern/submission/workspace_traced_update.py',
    'src/fern/v_2/__init__.py',
    'src/fern/v_2/problem/__init__.py',
    'src/fern/v_2/problem/assert_correctness_check.py',
    'src/fern/v_2/problem/basic_custom_files.py',
    'src/fern/v_2/problem/basic_test_case_template.py',
    'src/fern/v_2/problem/create_problem_request_v_2.py',
    'src/fern/v_2/problem/custom_files.py',
    'src/fern/v_2/problem/deep_equality_correctness_check.py',
    'src/fern/v_2/problem/default_provided_file.py',
    'src/fern/v_2/problem/file_info_v_2.py',
    'src/fern/v_2/problem/files.py',
    'src/fern/v_2/problem/function_implementation.py',
    'src/fern/v_2/problem/function_implementation_for_multiple_languages.py',
    'src/fern/v_2/problem/function_signature.py',
    'src/fern/v_2/problem/generated_files.py',
    'src/fern/v_2/problem/get_basic_solution_file_request.py',
    'src/fern/v_2/problem/get_basic_solution_file_response.py',
    'src/fern/v_2/problem/get_function_signature_request.py',
    'src/fern/v_2/problem/get_function_signature_response.py',
    'src/fern/v_2/problem/get_generated_test_case_file_request.py',
    'src/fern/v_2/problem/get_generated_test_case_template_file_request.py',
    'src/fern/v_2/problem/lightweight_problem_info_v_2.py',
    'src/fern/v_2/problem/non_void_function_definition.py',
    'src/fern/v_2/problem/non_void_function_signature.py',
    'src/fern/v_2/problem/parameter.py',
    'src/fern/v_2/problem/parameter_id.py',
    'src/fern/v_2/problem/problem_info_v_2.py',
    'src/fern/v_2/problem/test_case_expects.py',
    'src/fern/v_2/problem/test_case_function.py',
    'src/fern/v_2/problem/test_case_id.py',
    'src/fern/v_2/problem/test_case_implementation.py',
    'src/fern/v_2/problem/test_case_implementation_description.py',
    'src/fern/v_2/problem/test_case_implementation_description_board.py',
    'src/fern/v_2/problem/test_case_implementation_reference.py',
    'src/fern/v_2/problem/test_case_metadata.py',
    'src/fern/v_2/problem/test_case_template.py',
    'src/fern/v_2/problem/test_case_template_id.py',
    'src/fern/v_2/problem/test_case_v_2.py',
    'src/fern/v_2/problem/test_case_with_actual_result_implementation.py',
    'src/fern/v_2/problem/void_function_definition.py',
    'src/fern/v_2/problem/void_function_definition_that_takes_actual_result.py',
    'src/fern/v_2/problem/void_function_signature.py',
    'src/fern/v_2/problem/void_function_signature_that_takes_actual_result.py',
    'src/fern/v_2/v_3/__init__.py',
    'src/fern/v_2/v_3/problem/__init__.py',
    'src/fern/v_2/v_3/problem/assert_correctness_check.py',
    'src/fern/v_2/v_3/problem/basic_custom_files.py',
    'src/fern/v_2/v_3/problem/basic_test_case_template.py',
    'src/fern/v_2/v_3/problem/create_problem_request_v_2.py',
    'src/fern/v_2/v_3/problem/custom_files.py',
    'src/fern/v_2/v_3/problem/deep_equality_correctness_check.py',
    'src/fern/v_2/v_3/problem/default_provided_file.py',
    'src/fern/v_2/v_3/problem/file_info_v_2.py',
    'src/fern/v_2/v_3/problem/files.py',
    'src/fern/v_2/v_3/problem/function_implementation.py',
    'src/fern/v_2/v_3/problem/function_implementation_for_multiple_languages.py',
    'src/fern/v_2/v_3/problem/function_signature.py',
    'src/fern/v_2/v_3/problem/generated_files.py',
    'src/fern/v_2/v_3/problem/get_basic_solution_file_request.py',
    'src/fern/v_2/v_3/problem/get_basic_solution_file_response.py',
    'src/fern/v_2/v_3/problem/get_function_signature_request.py',
    'src/fern/v_2/v_3/problem/get_function_signature_response.py',
    'src/fern/v_2/v_3/problem/get_generated_test_case_file_request.py',
    'src/fern/v_2/v_3/problem/get_generated_test_case_template_file_request.py',
    'src/fern/v_2/v_3/problem/lightweight_problem_info_v_2.py',
    'src/fern/v_2/v_3/problem/non_void_function_definition.py',
    'src/fern/v_2/v_3/problem/non_void_function_signature.py',
    'src/fern/v_2/v_3/problem/parameter.py',
    'src/fern/v_2/v_3/problem/parameter_id.py',
    'src/fern/v_2/v_3/problem/problem_info_v_2.py',
    'src/fern/v_2/v_3/problem/test_case_expects.py',
    'src/fern/v_2/v_3/problem/test_case_function.py',
    'src/fern/v_2/v_3/problem/test_case_id.py',
    'src/fern/v_2/v_3/problem/test_case_implementation.py',
    'src/fern/v_2/v_3/problem/test_case_implementation_description.py',
    'src/fern/v_2/v_3/problem/test_case_implementation_description_board.py',
    'src/fern/v_2/v_3/problem/test_case_implementation_reference.py',
    'src/fern/v_2/v_3/problem/test_case_metadata.py',
    'src/fern/v_2/v_3/problem/test_case_template.py',
    'src/fern/v_2/v_3/problem/test_case_template_id.py',
    'src/fern/v_2/v_3/problem/test_case_v_2.py',
    'src/fern/v_2/v_3/problem/test_case_with_actual_result_implementation.py',
    'src/fern/v_2/v_3/problem/void_function_definition.py',
    'src/fern/v_2/v_3/problem/void_function_definition_that_takes_actual_result.py',
    'src/fern/v_2/v_3/problem/void_function_signature.py',
    'src/fern/v_2/v_3/problem/void_function_signature_that_takes_actual_result.py'
]

snapshots['test_pydantic_model src_fern___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern___init__.py')

snapshots['test_pydantic_model src_fern_admin___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_admin___init__.py')

snapshots['test_pydantic_model src_fern_admin_store_traced_test_case_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_admin_store_traced_test_case_request.py')

snapshots['test_pydantic_model src_fern_admin_store_traced_workspace_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_admin_store_traced_workspace_request.py')

snapshots['test_pydantic_model src_fern_commons___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons___init__.py')

snapshots['test_pydantic_model src_fern_commons_binary_tree_node_and_tree_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_binary_tree_node_and_tree_value.py')

snapshots['test_pydantic_model src_fern_commons_binary_tree_node_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_binary_tree_node_value.py')

snapshots['test_pydantic_model src_fern_commons_binary_tree_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_binary_tree_value.py')

snapshots['test_pydantic_model src_fern_commons_debug_key_value_pairs'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_debug_key_value_pairs.py')

snapshots['test_pydantic_model src_fern_commons_debug_map_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_debug_map_value.py')

snapshots['test_pydantic_model src_fern_commons_debug_variable_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_debug_variable_value.py')

snapshots['test_pydantic_model src_fern_commons_doubly_linked_list_node_and_list_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_doubly_linked_list_node_and_list_value.py')

snapshots['test_pydantic_model src_fern_commons_doubly_linked_list_node_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_doubly_linked_list_node_value.py')

snapshots['test_pydantic_model src_fern_commons_doubly_linked_list_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_doubly_linked_list_value.py')

snapshots['test_pydantic_model src_fern_commons_file_info'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_file_info.py')

snapshots['test_pydantic_model src_fern_commons_generic_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_generic_value.py')

snapshots['test_pydantic_model src_fern_commons_key_value_pair'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_key_value_pair.py')

snapshots['test_pydantic_model src_fern_commons_language'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_language.py')

snapshots['test_pydantic_model src_fern_commons_list_type'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_list_type.py')

snapshots['test_pydantic_model src_fern_commons_map_type'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_map_type.py')

snapshots['test_pydantic_model src_fern_commons_map_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_map_value.py')

snapshots['test_pydantic_model src_fern_commons_node_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_node_id.py')

snapshots['test_pydantic_model src_fern_commons_problem_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_problem_id.py')

snapshots['test_pydantic_model src_fern_commons_singly_linked_list_node_and_list_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_singly_linked_list_node_and_list_value.py')

snapshots['test_pydantic_model src_fern_commons_singly_linked_list_node_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_singly_linked_list_node_value.py')

snapshots['test_pydantic_model src_fern_commons_singly_linked_list_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_singly_linked_list_value.py')

snapshots['test_pydantic_model src_fern_commons_test_case'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_test_case.py')

snapshots['test_pydantic_model src_fern_commons_test_case_with_expected_result'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_test_case_with_expected_result.py')

snapshots['test_pydantic_model src_fern_commons_user_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_user_id.py')

snapshots['test_pydantic_model src_fern_commons_variable_type'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_variable_type.py')

snapshots['test_pydantic_model src_fern_commons_variable_value'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_commons_variable_value.py')

snapshots['test_pydantic_model src_fern_lang_server___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_lang_server___init__.py')

snapshots['test_pydantic_model src_fern_lang_server_lang_server_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_lang_server_lang_server_request.py')

snapshots['test_pydantic_model src_fern_lang_server_lang_server_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_lang_server_lang_server_response.py')

snapshots['test_pydantic_model src_fern_migration___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_migration___init__.py')

snapshots['test_pydantic_model src_fern_migration_migration'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_migration_migration.py')

snapshots['test_pydantic_model src_fern_migration_migration_status'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_migration_migration_status.py')

snapshots['test_pydantic_model src_fern_playlist___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_playlist___init__.py')

snapshots['test_pydantic_model src_fern_playlist_playlist'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_playlist_playlist.py')

snapshots['test_pydantic_model src_fern_playlist_playlist_create_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_playlist_playlist_create_request.py')

snapshots['test_pydantic_model src_fern_playlist_playlist_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_playlist_playlist_id.py')

snapshots['test_pydantic_model src_fern_playlist_update_playlist_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_playlist_update_playlist_request.py')

snapshots['test_pydantic_model src_fern_problem___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem___init__.py')

snapshots['test_pydantic_model src_fern_problem_create_problem_error'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_create_problem_error.py')

snapshots['test_pydantic_model src_fern_problem_create_problem_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_create_problem_request.py')

snapshots['test_pydantic_model src_fern_problem_create_problem_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_create_problem_response.py')

snapshots['test_pydantic_model src_fern_problem_generic_create_problem_error'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_generic_create_problem_error.py')

snapshots['test_pydantic_model src_fern_problem_get_default_starter_files_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_get_default_starter_files_request.py')

snapshots['test_pydantic_model src_fern_problem_get_default_starter_files_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_get_default_starter_files_response.py')

snapshots['test_pydantic_model src_fern_problem_problem_description'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_problem_description.py')

snapshots['test_pydantic_model src_fern_problem_problem_description_board'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_problem_description_board.py')

snapshots['test_pydantic_model src_fern_problem_problem_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_problem_files.py')

snapshots['test_pydantic_model src_fern_problem_problem_info'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_problem_info.py')

snapshots['test_pydantic_model src_fern_problem_update_problem_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_update_problem_response.py')

snapshots['test_pydantic_model src_fern_problem_variable_type_and_name'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_problem_variable_type_and_name.py')

snapshots['test_pydantic_model src_fern_submission___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission___init__.py')

snapshots['test_pydantic_model src_fern_submission_actual_result'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_actual_result.py')

snapshots['test_pydantic_model src_fern_submission_building_executor_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_building_executor_response.py')

snapshots['test_pydantic_model src_fern_submission_code_execution_update'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_code_execution_update.py')

snapshots['test_pydantic_model src_fern_submission_compile_error'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_compile_error.py')

snapshots['test_pydantic_model src_fern_submission_custom_test_cases_unsupported'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_custom_test_cases_unsupported.py')

snapshots['test_pydantic_model src_fern_submission_error_info'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_error_info.py')

snapshots['test_pydantic_model src_fern_submission_errored_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_errored_response.py')

snapshots['test_pydantic_model src_fern_submission_exception_info'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_exception_info.py')

snapshots['test_pydantic_model src_fern_submission_exception_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_exception_v_2.py')

snapshots['test_pydantic_model src_fern_submission_execution_session_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_execution_session_response.py')

snapshots['test_pydantic_model src_fern_submission_execution_session_state'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_execution_session_state.py')

snapshots['test_pydantic_model src_fern_submission_execution_session_status'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_execution_session_status.py')

snapshots['test_pydantic_model src_fern_submission_existing_submission_executing'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_existing_submission_executing.py')

snapshots['test_pydantic_model src_fern_submission_expression_location'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_expression_location.py')

snapshots['test_pydantic_model src_fern_submission_finished_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_finished_response.py')

snapshots['test_pydantic_model src_fern_submission_get_execution_session_state_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_get_execution_session_state_response.py')

snapshots['test_pydantic_model src_fern_submission_get_submission_state_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_get_submission_state_response.py')

snapshots['test_pydantic_model src_fern_submission_get_trace_responses_page_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_get_trace_responses_page_request.py')

snapshots['test_pydantic_model src_fern_submission_graded_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_graded_response.py')

snapshots['test_pydantic_model src_fern_submission_graded_response_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_graded_response_v_2.py')

snapshots['test_pydantic_model src_fern_submission_graded_test_case_update'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_graded_test_case_update.py')

snapshots['test_pydantic_model src_fern_submission_initialize_problem_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_initialize_problem_request.py')

snapshots['test_pydantic_model src_fern_submission_internal_error'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_internal_error.py')

snapshots['test_pydantic_model src_fern_submission_invalid_request_cause'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_invalid_request_cause.py')

snapshots['test_pydantic_model src_fern_submission_invalid_request_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_invalid_request_response.py')

snapshots['test_pydantic_model src_fern_submission_lightweight_stackframe_information'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_lightweight_stackframe_information.py')

snapshots['test_pydantic_model src_fern_submission_recorded_response_notification'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_recorded_response_notification.py')

snapshots['test_pydantic_model src_fern_submission_recorded_test_case_update'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_recorded_test_case_update.py')

snapshots['test_pydantic_model src_fern_submission_recording_response_notification'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_recording_response_notification.py')

snapshots['test_pydantic_model src_fern_submission_running_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_running_response.py')

snapshots['test_pydantic_model src_fern_submission_running_submission_state'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_running_submission_state.py')

snapshots['test_pydantic_model src_fern_submission_runtime_error'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_runtime_error.py')

snapshots['test_pydantic_model src_fern_submission_scope'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_scope.py')

snapshots['test_pydantic_model src_fern_submission_share_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_share_id.py')

snapshots['test_pydantic_model src_fern_submission_stack_frame'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_stack_frame.py')

snapshots['test_pydantic_model src_fern_submission_stack_information'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_stack_information.py')

snapshots['test_pydantic_model src_fern_submission_stderr_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_stderr_response.py')

snapshots['test_pydantic_model src_fern_submission_stdout_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_stdout_response.py')

snapshots['test_pydantic_model src_fern_submission_stop_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_stop_request.py')

snapshots['test_pydantic_model src_fern_submission_stopped_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_stopped_response.py')

snapshots['test_pydantic_model src_fern_submission_submission_file_info'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_file_info.py')

snapshots['test_pydantic_model src_fern_submission_submission_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_id.py')

snapshots['test_pydantic_model src_fern_submission_submission_id_not_found'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_id_not_found.py')

snapshots['test_pydantic_model src_fern_submission_submission_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_request.py')

snapshots['test_pydantic_model src_fern_submission_submission_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_response.py')

snapshots['test_pydantic_model src_fern_submission_submission_status_for_test_case'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_status_for_test_case.py')

snapshots['test_pydantic_model src_fern_submission_submission_status_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_status_v_2.py')

snapshots['test_pydantic_model src_fern_submission_submission_type_enum'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_type_enum.py')

snapshots['test_pydantic_model src_fern_submission_submission_type_state'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submission_type_state.py')

snapshots['test_pydantic_model src_fern_submission_submit_request_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_submit_request_v_2.py')

snapshots['test_pydantic_model src_fern_submission_terminated_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_terminated_response.py')

snapshots['test_pydantic_model src_fern_submission_test_case_grade'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_case_grade.py')

snapshots['test_pydantic_model src_fern_submission_test_case_hidden_grade'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_case_hidden_grade.py')

snapshots['test_pydantic_model src_fern_submission_test_case_non_hidden_grade'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_case_non_hidden_grade.py')

snapshots['test_pydantic_model src_fern_submission_test_case_result'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_case_result.py')

snapshots['test_pydantic_model src_fern_submission_test_case_result_with_stdout'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_case_result_with_stdout.py')

snapshots['test_pydantic_model src_fern_submission_test_submission_state'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_submission_state.py')

snapshots['test_pydantic_model src_fern_submission_test_submission_status'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_submission_status.py')

snapshots['test_pydantic_model src_fern_submission_test_submission_status_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_submission_status_v_2.py')

snapshots['test_pydantic_model src_fern_submission_test_submission_update'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_submission_update.py')

snapshots['test_pydantic_model src_fern_submission_test_submission_update_info'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_test_submission_update_info.py')

snapshots['test_pydantic_model src_fern_submission_trace_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_trace_response.py')

snapshots['test_pydantic_model src_fern_submission_trace_response_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_trace_response_v_2.py')

snapshots['test_pydantic_model src_fern_submission_trace_responses_page'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_trace_responses_page.py')

snapshots['test_pydantic_model src_fern_submission_trace_responses_page_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_trace_responses_page_v_2.py')

snapshots['test_pydantic_model src_fern_submission_traced_file'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_traced_file.py')

snapshots['test_pydantic_model src_fern_submission_traced_test_case'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_traced_test_case.py')

snapshots['test_pydantic_model src_fern_submission_unexpected_language_error'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_unexpected_language_error.py')

snapshots['test_pydantic_model src_fern_submission_workspace_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_files.py')

snapshots['test_pydantic_model src_fern_submission_workspace_ran_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_ran_response.py')

snapshots['test_pydantic_model src_fern_submission_workspace_run_details'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_run_details.py')

snapshots['test_pydantic_model src_fern_submission_workspace_starter_files_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_starter_files_response.py')

snapshots['test_pydantic_model src_fern_submission_workspace_starter_files_response_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_starter_files_response_v_2.py')

snapshots['test_pydantic_model src_fern_submission_workspace_submission_state'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_submission_state.py')

snapshots['test_pydantic_model src_fern_submission_workspace_submission_status'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_submission_status.py')

snapshots['test_pydantic_model src_fern_submission_workspace_submission_status_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_submission_status_v_2.py')

snapshots['test_pydantic_model src_fern_submission_workspace_submission_update'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_submission_update.py')

snapshots['test_pydantic_model src_fern_submission_workspace_submission_update_info'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_submission_update_info.py')

snapshots['test_pydantic_model src_fern_submission_workspace_submit_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_submit_request.py')

snapshots['test_pydantic_model src_fern_submission_workspace_traced_update'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_submission_workspace_traced_update.py')

snapshots['test_pydantic_model src_fern_v_2___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2___init__.py')

snapshots['test_pydantic_model src_fern_v_2_problem___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem___init__.py')

snapshots['test_pydantic_model src_fern_v_2_problem_assert_correctness_check'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_assert_correctness_check.py')

snapshots['test_pydantic_model src_fern_v_2_problem_basic_custom_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_basic_custom_files.py')

snapshots['test_pydantic_model src_fern_v_2_problem_basic_test_case_template'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_basic_test_case_template.py')

snapshots['test_pydantic_model src_fern_v_2_problem_create_problem_request_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_create_problem_request_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_problem_custom_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_custom_files.py')

snapshots['test_pydantic_model src_fern_v_2_problem_deep_equality_correctness_check'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_deep_equality_correctness_check.py')

snapshots['test_pydantic_model src_fern_v_2_problem_default_provided_file'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_default_provided_file.py')

snapshots['test_pydantic_model src_fern_v_2_problem_file_info_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_file_info_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_problem_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_files.py')

snapshots['test_pydantic_model src_fern_v_2_problem_function_implementation'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_function_implementation.py')

snapshots['test_pydantic_model src_fern_v_2_problem_function_implementation_for_multiple_languages'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_function_implementation_for_multiple_languages.py')

snapshots['test_pydantic_model src_fern_v_2_problem_function_signature'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_function_signature.py')

snapshots['test_pydantic_model src_fern_v_2_problem_generated_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_generated_files.py')

snapshots['test_pydantic_model src_fern_v_2_problem_get_basic_solution_file_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_get_basic_solution_file_request.py')

snapshots['test_pydantic_model src_fern_v_2_problem_get_basic_solution_file_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_get_basic_solution_file_response.py')

snapshots['test_pydantic_model src_fern_v_2_problem_get_function_signature_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_get_function_signature_request.py')

snapshots['test_pydantic_model src_fern_v_2_problem_get_function_signature_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_get_function_signature_response.py')

snapshots['test_pydantic_model src_fern_v_2_problem_get_generated_test_case_file_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_get_generated_test_case_file_request.py')

snapshots['test_pydantic_model src_fern_v_2_problem_get_generated_test_case_template_file_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_get_generated_test_case_template_file_request.py')

snapshots['test_pydantic_model src_fern_v_2_problem_lightweight_problem_info_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_lightweight_problem_info_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_problem_non_void_function_definition'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_non_void_function_definition.py')

snapshots['test_pydantic_model src_fern_v_2_problem_non_void_function_signature'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_non_void_function_signature.py')

snapshots['test_pydantic_model src_fern_v_2_problem_parameter'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_parameter.py')

snapshots['test_pydantic_model src_fern_v_2_problem_parameter_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_parameter_id.py')

snapshots['test_pydantic_model src_fern_v_2_problem_problem_info_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_problem_info_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_expects'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_expects.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_function'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_function.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_id.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_implementation'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_implementation.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_implementation_description'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_implementation_description.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_implementation_description_board'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_implementation_description_board.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_implementation_reference'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_implementation_reference.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_metadata'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_metadata.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_template'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_template.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_template_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_template_id.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_problem_test_case_with_actual_result_implementation'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_test_case_with_actual_result_implementation.py')

snapshots['test_pydantic_model src_fern_v_2_problem_void_function_definition'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_void_function_definition.py')

snapshots['test_pydantic_model src_fern_v_2_problem_void_function_definition_that_takes_actual_result'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_void_function_definition_that_takes_actual_result.py')

snapshots['test_pydantic_model src_fern_v_2_problem_void_function_signature'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_void_function_signature.py')

snapshots['test_pydantic_model src_fern_v_2_problem_void_function_signature_that_takes_actual_result'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_problem_void_function_signature_that_takes_actual_result.py')

snapshots['test_pydantic_model src_fern_v_2_v_3___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3___init__.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem___init__'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem___init__.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_assert_correctness_check'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_assert_correctness_check.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_basic_custom_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_basic_custom_files.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_basic_test_case_template'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_basic_test_case_template.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_create_problem_request_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_create_problem_request_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_custom_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_custom_files.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_deep_equality_correctness_check'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_deep_equality_correctness_check.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_default_provided_file'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_default_provided_file.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_file_info_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_file_info_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_files.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_function_implementation'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_function_implementation.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_function_implementation_for_multiple_languages'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_function_implementation_for_multiple_languages.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_function_signature'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_function_signature.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_generated_files'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_generated_files.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_get_basic_solution_file_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_get_basic_solution_file_request.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_get_basic_solution_file_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_get_basic_solution_file_response.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_get_function_signature_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_get_function_signature_request.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_get_function_signature_response'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_get_function_signature_response.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_get_generated_test_case_file_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_get_generated_test_case_file_request.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_get_generated_test_case_template_file_request'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_get_generated_test_case_template_file_request.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_lightweight_problem_info_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_lightweight_problem_info_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_non_void_function_definition'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_non_void_function_definition.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_non_void_function_signature'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_non_void_function_signature.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_parameter'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_parameter.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_parameter_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_parameter_id.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_problem_info_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_problem_info_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_expects'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_expects.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_function'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_function.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_id.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_implementation'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_implementation.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_implementation_description'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_implementation_description.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_implementation_description_board'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_implementation_description_board.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_implementation_reference'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_implementation_reference.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_metadata'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_metadata.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_template'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_template.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_template_id'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_template_id.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_v_2'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_v_2.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_test_case_with_actual_result_implementation'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_test_case_with_actual_result_implementation.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_void_function_definition'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_void_function_definition.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_void_function_definition_that_takes_actual_result'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_void_function_definition_that_takes_actual_result.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_void_function_signature'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_void_function_signature.py')

snapshots['test_pydantic_model src_fern_v_2_v_3_problem_void_function_signature_that_takes_actual_result'] = FileSnapshot('snap_test_pydantic_model/test_pydantic_model src_fern_v_2_v_3_problem_void_function_signature_that_takes_actual_result.py')
