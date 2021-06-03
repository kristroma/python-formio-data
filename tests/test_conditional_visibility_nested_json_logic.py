# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

import json
import unittest

from tests.utils import readfile
from formiodata.builder import Builder
from formiodata.form import Form
from formiodata.components import textfieldComponent, passwordComponent

class ConditionalVisibilityNestedJsonLogicTestCase(unittest.TestCase):
    def setUp(self):
        super(ConditionalVisibilityNestedJsonLogicTestCase, self).setUp()

        self.builder_json = readfile('data', 'test_conditional_visibility_nested_json_logic_builder.json')
        self.hide_secret_form_json = readfile('data', 'test_conditional_visibility_nested_json_logic_hide_secret.json')
        self.show_secret_form_json = readfile('data', 'test_conditional_visibility_nested_json_logic_show_secret.json')
        self.hide_global_secret_only_form_json = readfile('data', 'test_conditional_visibility_nested_json_logic_hide_global_secret_only.json')
        self.show_global_secret_only_form_json = readfile('data', 'test_conditional_visibility_nested_json_logic_show_global_secret_only.json')


    def test_conditionally_shown_top_level_form_elements_have_default_state_in_builder(self):
        builder = Builder(self.builder_json)

        self.assertTrue(builder.input_components['username'].conditionally_visible)
        self.assertTrue(builder.input_components['password'].conditionally_visible)
        self.assertFalse(builder.input_components['secret'].conditionally_visible)


    def test_conditionally_shown_form_elements_in_panel_have_default_state_in_builder(self):
        builder = Builder(self.builder_json)

        self.assertTrue(builder.input_components['username1'].conditionally_visible)
        self.assertTrue(builder.input_components['password1'].conditionally_visible)
        self.assertFalse(builder.input_components['secret1'].conditionally_visible)

        self.assertTrue(builder.input_components['username2'].conditionally_visible)
        self.assertTrue(builder.input_components['password2'].conditionally_visible)
        self.assertFalse(builder.input_components['secret2'].conditionally_visible)


    def test_conditionally_shown_top_level_form_elements_toggle_on_condition_being_met(self):
        builder = Builder(self.builder_json)

        hide_secret_form = Form(self.hide_secret_form_json, builder)
        self.assertTrue(hide_secret_form.input_components['username'].conditionally_visible)
        self.assertTrue(hide_secret_form.input_components['password'].conditionally_visible)
        self.assertFalse(hide_secret_form.input_components['secret'].conditionally_visible)

        show_secret_form = Form(self.show_secret_form_json, builder)
        self.assertTrue(show_secret_form.input_components['username'].conditionally_visible)
        self.assertTrue(show_secret_form.input_components['password'].conditionally_visible)
        self.assertTrue(show_secret_form.input_components['secret'].conditionally_visible)


    def test_conditionally_shown_form_elements_in_panel_toggle_on_condition_being_met(self):
        builder = Builder(self.builder_json)

        hide_secret_form = Form(self.hide_secret_form_json, builder)
        self.assertTrue(hide_secret_form.input_components['username1'].conditionally_visible)
        self.assertTrue(hide_secret_form.input_components['password1'].conditionally_visible)
        self.assertFalse(hide_secret_form.input_components['secret1'].conditionally_visible)

        self.assertTrue(hide_secret_form.input_components['username2'].conditionally_visible)
        self.assertTrue(hide_secret_form.input_components['password2'].conditionally_visible)
        self.assertFalse(hide_secret_form.input_components['secret2'].conditionally_visible)

        show_secret_form = Form(self.show_secret_form_json, builder)
        self.assertTrue(show_secret_form.input_components['username1'].conditionally_visible)
        self.assertTrue(show_secret_form.input_components['password1'].conditionally_visible)
        self.assertTrue(show_secret_form.input_components['secret1'].conditionally_visible)

        self.assertTrue(show_secret_form.input_components['username2'].conditionally_visible)
        self.assertTrue(show_secret_form.input_components['password2'].conditionally_visible)
        self.assertTrue(show_secret_form.input_components['secret2'].conditionally_visible)


    def test_conditionally_shown_form_elements_in_data_grid_toggle_on_local_row_condition_met(self):
        builder = Builder(self.builder_json)

        hide_secret_form = Form(self.hide_secret_form_json, builder)
        hide_secret_datagrid = hide_secret_form.input_components['dataGrid']

        hide_secret_first_row = hide_secret_datagrid.rows[0]
        self.assertTrue(hide_secret_first_row.input_components['username3'].conditionally_visible)
        self.assertTrue(hide_secret_first_row.input_components['password3'].conditionally_visible)
        self.assertFalse(hide_secret_first_row.input_components['secret3'].conditionally_visible)
        self.assertFalse(hide_secret_first_row.input_components['globalSecret'].conditionally_visible)

        hide_secret_second_row = hide_secret_datagrid.rows[1]
        self.assertTrue(hide_secret_second_row.input_components['username3'].conditionally_visible)
        self.assertTrue(hide_secret_second_row.input_components['password3'].conditionally_visible)
        self.assertFalse(hide_secret_second_row.input_components['secret3'].conditionally_visible)
        self.assertFalse(hide_secret_second_row.input_components['globalSecret'].conditionally_visible)

        show_secret_form = Form(self.show_secret_form_json, builder)
        show_secret_datagrid = show_secret_form.input_components['dataGrid']

        show_secret_first_row = show_secret_datagrid.rows[0]
        self.assertTrue(show_secret_first_row.input_components['username3'].conditionally_visible)
        self.assertTrue(show_secret_first_row.input_components['password3'].conditionally_visible)
        self.assertTrue(show_secret_first_row.input_components['secret3'].conditionally_visible)
        self.assertTrue(show_secret_first_row.input_components['globalSecret'].conditionally_visible)

        show_secret_second_row = show_secret_datagrid.rows[0]
        self.assertTrue(show_secret_second_row.input_components['username3'].conditionally_visible)
        self.assertTrue(show_secret_second_row.input_components['password3'].conditionally_visible)
        self.assertTrue(show_secret_second_row.input_components['secret3'].conditionally_visible)
        self.assertTrue(show_secret_second_row.input_components['globalSecret'].conditionally_visible)


    def test_conditionally_shown_form_elements_in_data_grid_toggle_on_global_data_condition_met(self):
        builder = Builder(self.builder_json)

        show_global_secret_only_form = Form(self.show_global_secret_only_form_json, builder)
        show_global_secret_only_datagrid = show_global_secret_only_form.input_components['dataGrid']

        show_global_secret_only_first_row = show_global_secret_only_datagrid.rows[0]
        self.assertTrue(show_global_secret_only_first_row.input_components['username3'].conditionally_visible)
        self.assertTrue(show_global_secret_only_first_row.input_components['password3'].conditionally_visible)
        self.assertFalse(show_global_secret_only_first_row.input_components['secret3'].conditionally_visible)
        self.assertTrue(show_global_secret_only_first_row.input_components['globalSecret'].conditionally_visible)

        show_global_secret_only_second_row = show_global_secret_only_datagrid.rows[1]
        self.assertTrue(show_global_secret_only_second_row.input_components['username3'].conditionally_visible)
        self.assertTrue(show_global_secret_only_second_row.input_components['password3'].conditionally_visible)
        self.assertFalse(show_global_secret_only_second_row.input_components['secret3'].conditionally_visible)
        self.assertTrue(show_global_secret_only_second_row.input_components['globalSecret'].conditionally_visible)

        hide_global_secret_only_form = Form(self.hide_global_secret_only_form_json, builder)
        hide_global_secret_only_datagrid = hide_global_secret_only_form.input_components['dataGrid']

        hide_global_secret_only_first_row = hide_global_secret_only_datagrid.rows[0]
        self.assertTrue(hide_global_secret_only_first_row.input_components['username3'].conditionally_visible)
        self.assertTrue(hide_global_secret_only_first_row.input_components['password3'].conditionally_visible)
        self.assertTrue(hide_global_secret_only_first_row.input_components['secret3'].conditionally_visible)
        self.assertFalse(hide_global_secret_only_first_row.input_components['globalSecret'].conditionally_visible)

        hide_global_secret_only_second_row = hide_global_secret_only_datagrid.rows[0]
        self.assertTrue(hide_global_secret_only_second_row.input_components['username3'].conditionally_visible)
        self.assertTrue(hide_global_secret_only_second_row.input_components['password3'].conditionally_visible)
        self.assertTrue(hide_global_secret_only_second_row.input_components['secret3'].conditionally_visible)
        self.assertFalse(hide_global_secret_only_second_row.input_components['globalSecret'].conditionally_visible)


    def test_conditionally_shown_top_level_form_elements_do_not_render_when_hidden(self):
        builder = Builder(self.builder_json)

        hide_secret_form = Form(self.hide_secret_form_json, builder)
        hide_secret_form.render_components()
        self.assertEqual('<p>wrong</p>', hide_secret_form.input_components['username'].html_component)
        self.assertEqual('<p>incorrect</p>', hide_secret_form.input_components['password'].html_component)
        self.assertEqual('', hide_secret_form.input_components['secret'].html_component)

        show_secret_form = Form(self.show_secret_form_json, builder)
        show_secret_form.render_components()
        self.assertEqual('<p>user</p>', show_secret_form.input_components['username'].html_component)
        self.assertEqual('<p>secret</p>', show_secret_form.input_components['password'].html_component)
        self.assertEqual('<p>Secret message</p>', show_secret_form.input_components['secret'].html_component)


    def test_conditionally_shown_form_elements_in_panel_do_not_render_when_hidden(self):
        builder = Builder(self.builder_json)

        hide_secret_form = Form(self.hide_secret_form_json, builder)
        hide_secret_form.render_components()
        self.assertEqual('<p>wrong</p>', hide_secret_form.input_components['username1'].html_component)
        self.assertEqual('<p>incorrect</p>', hide_secret_form.input_components['password1'].html_component)
        self.assertEqual('', hide_secret_form.input_components['secret1'].html_component)

        self.assertEqual('<p>wrong</p>', hide_secret_form.input_components['username2'].html_component)
        self.assertEqual('<p>incorrect</p>', hide_secret_form.input_components['password2'].html_component)
        self.assertEqual('', hide_secret_form.input_components['secret2'].html_component)

        show_secret_form = Form(self.show_secret_form_json, builder)
        show_secret_form.render_components()
        self.assertEqual('<p>user</p>', show_secret_form.input_components['username1'].html_component)
        self.assertEqual('<p>secret</p>', show_secret_form.input_components['password1'].html_component)
        self.assertEqual('<p>Secret message</p>', show_secret_form.input_components['secret1'].html_component)

        self.assertEqual('<p>user</p>', show_secret_form.input_components['username2'].html_component)
        self.assertEqual('<p>secret</p>', show_secret_form.input_components['password2'].html_component)
        self.assertEqual('<p>Secret message</p>', show_secret_form.input_components['secret2'].html_component)


    def test_conditionally_shown_form_elements_for_local_row_condition_in_data_grid_do_not_render_when_hidden(self):
        builder = Builder(self.builder_json)

        hide_secret_form = Form(self.hide_secret_form_json, builder)
        hide_secret_form.render_components()
        hide_secret_datagrid = hide_secret_form.input_components['dataGrid']

        hide_secret_first_row = hide_secret_datagrid.rows[0]
        self.assertEqual('<tr><td><table><tr><td><p>wrong</p></td><td><p>incorrect</p></td><td></td><td></td></tr></table></td></tr>', hide_secret_first_row.html_component)
        self.assertEqual('<p>wrong</p>', hide_secret_first_row.input_components['username3'].html_component)
        self.assertEqual('<p>incorrect</p>', hide_secret_first_row.input_components['password3'].html_component)
        self.assertEqual('', hide_secret_first_row.input_components['secret3'].html_component)
        self.assertEqual('', hide_secret_first_row.input_components['globalSecret'].html_component)

        hide_secret_second_row = hide_secret_datagrid.rows[1]
        self.assertEqual('<tr><td><table><tr><td><p>wrong</p></td><td><p>incorrect</p></td><td></td><td></td></tr></table></td></tr>', hide_secret_second_row.html_component)
        self.assertEqual('<p>wrong</p>', hide_secret_second_row.input_components['username3'].html_component)
        self.assertEqual('<p>incorrect</p>', hide_secret_second_row.input_components['password3'].html_component)
        self.assertEqual('', hide_secret_second_row.input_components['secret3'].html_component)
        self.assertEqual('', hide_secret_second_row.input_components['globalSecret'].html_component)

        # Tying it all together
        self.assertEqual(
            f'<table>{hide_secret_first_row.html_component}{hide_secret_second_row.html_component}</table>',
            hide_secret_datagrid.html_component
        )

        show_secret_form = Form(self.show_secret_form_json, builder)
        show_secret_form.render_components()
        show_secret_datagrid = show_secret_form.input_components['dataGrid']

        show_secret_first_row = show_secret_datagrid.rows[0]
        self.assertEqual('<tr><td><table><tr><td><p>user</p></td><td><p>secret</p></td><td><p>Secret message</p></td><td><p>Another secret message</p></td></tr></table></td></tr>', show_secret_first_row.html_component)
        self.assertEqual('<p>user</p>', show_secret_first_row.input_components['username3'].html_component)
        self.assertEqual('<p>secret</p>', show_secret_first_row.input_components['password3'].html_component)
        self.assertEqual('<p>Secret message</p>', show_secret_first_row.input_components['secret3'].html_component)
        self.assertEqual('<p>Another secret message</p>', show_secret_first_row.input_components['globalSecret'].html_component)

        show_secret_second_row = show_secret_datagrid.rows[0]
        self.assertEqual('<tr><td><table><tr><td><p>user</p></td><td><p>secret</p></td><td><p>Secret message</p></td><td><p>Another secret message</p></td></tr></table></td></tr>', show_secret_second_row.html_component)
        self.assertEqual('<p>user</p>', show_secret_second_row.input_components['username3'].html_component)
        self.assertEqual('<p>secret</p>', show_secret_second_row.input_components['password3'].html_component)
        self.assertEqual('<p>Secret message</p>', show_secret_second_row.input_components['secret3'].html_component)
        self.assertEqual('<p>Another secret message</p>', show_secret_second_row.input_components['globalSecret'].html_component)

        # Tying it all together
        self.assertEqual(
            f'<table>{show_secret_first_row.html_component}{show_secret_second_row.html_component}</table>',
            show_secret_datagrid.html_component
        )


    def test_conditionally_shown_form_elements_for_global_data_condition_in_data_grid_do_not_render_when_hidden(self):
        builder = Builder(self.builder_json)

        show_global_secret_only_form = Form(self.show_global_secret_only_form_json, builder)
        show_global_secret_only_form.render_components()
        show_global_secret_only_datagrid = show_global_secret_only_form.input_components['dataGrid']

        show_global_secret_only_first_row = show_global_secret_only_datagrid.rows[0]
        self.assertEqual('<tr><td><table><tr><td><p>wrong</p></td><td><p>incorrect</p></td><td></td><td><p>Another secret message</p></td></tr></table></td></tr>', show_global_secret_only_first_row.html_component)
        self.assertEqual('<p>wrong</p>', show_global_secret_only_first_row.input_components['username3'].html_component)
        self.assertEqual('<p>incorrect</p>', show_global_secret_only_first_row.input_components['password3'].html_component)
        self.assertEqual('', show_global_secret_only_first_row.input_components['secret3'].html_component)
        self.assertEqual('<p>Another secret message</p>', show_global_secret_only_first_row.input_components['globalSecret'].html_component)

        show_global_secret_only_second_row = show_global_secret_only_datagrid.rows[1]
        self.assertEqual('<tr><td><table><tr><td><p>wrong</p></td><td><p>incorrect</p></td><td></td><td><p>Another secret message</p></td></tr></table></td></tr>', show_global_secret_only_second_row.html_component)
        self.assertEqual('<p>wrong</p>', show_global_secret_only_second_row.input_components['username3'].html_component)
        self.assertEqual('<p>incorrect</p>', show_global_secret_only_second_row.input_components['password3'].html_component)
        self.assertEqual('', show_global_secret_only_second_row.input_components['secret3'].html_component)
        self.assertEqual('<p>Another secret message</p>', show_global_secret_only_second_row.input_components['globalSecret'].html_component)

        # Tying it all together
        self.assertEqual(
            f'<table>{show_global_secret_only_first_row.html_component}{show_global_secret_only_second_row.html_component}</table>',
            show_global_secret_only_datagrid.html_component
        )

        hide_global_secret_only_form = Form(self.hide_global_secret_only_form_json, builder)
        hide_global_secret_only_form.render_components()
        hide_global_secret_only_datagrid = hide_global_secret_only_form.input_components['dataGrid']

        hide_global_secret_only_first_row = hide_global_secret_only_datagrid.rows[0]
        self.assertEqual('<tr><td><table><tr><td><p>user</p></td><td><p>secret</p></td><td><p>Secret message</p></td><td></td></tr></table></td></tr>', hide_global_secret_only_first_row.html_component)
        self.assertEqual('<p>user</p>', hide_global_secret_only_first_row.input_components['username3'].html_component)
        self.assertEqual('<p>secret</p>', hide_global_secret_only_first_row.input_components['password3'].html_component)
        self.assertEqual('<p>Secret message</p>', hide_global_secret_only_first_row.input_components['secret3'].html_component)
        self.assertEqual('', hide_global_secret_only_first_row.input_components['globalSecret'].html_component)

        hide_global_secret_only_second_row = hide_global_secret_only_datagrid.rows[0]
        self.assertEqual('<tr><td><table><tr><td><p>user</p></td><td><p>secret</p></td><td><p>Secret message</p></td><td></td></tr></table></td></tr>', hide_global_secret_only_second_row.html_component)
        self.assertEqual('<p>user</p>', hide_global_secret_only_second_row.input_components['username3'].html_component)
        self.assertEqual('<p>secret</p>', hide_global_secret_only_second_row.input_components['password3'].html_component)
        self.assertEqual('<p>Secret message</p>', hide_global_secret_only_second_row.input_components['secret3'].html_component)
        self.assertEqual('', hide_global_secret_only_second_row.input_components['globalSecret'].html_component)

        # Tying it all together
        self.assertEqual(
            f'<table>{hide_global_secret_only_first_row.html_component}{hide_global_secret_only_second_row.html_component}</table>',
            hide_global_secret_only_datagrid.html_component
        )
