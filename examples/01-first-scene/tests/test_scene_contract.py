from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FirstSceneContractTests(unittest.TestCase):
    def test_project_points_to_existing_main_scene(self):
        project = (ROOT / "project.godot").read_text(encoding="utf-8")
        match = re.search(r'^run/main_scene="res://([^"]+)"$', project, re.MULTILINE)
        self.assertIsNotNone(match, "project.godot must define run/main_scene")
        self.assertTrue((ROOT / match.group(1)).is_file(), "main scene path must exist")

    def test_scene_script_reference_resolves(self):
        scene = (ROOT / "main.tscn").read_text(encoding="utf-8")
        match = re.search(r'path="res://([^"]+)"', scene)
        self.assertIsNotNone(match, "scene must reference its script")
        self.assertTrue((ROOT / match.group(1)).is_file(), "scene script path must exist")

    def test_scene_has_input_and_visible_state_contract(self):
        script = (ROOT / "main.gd").read_text(encoding="utf-8")
        for expected in (
            "button.pressed.connect(_on_activate)",
            "button.focus_mode = Control.FOCUS_ALL",
            'counter_label.text = "Activations: %d" % activations',
            'status_label.text = "Ready. Activations: %d." % activations',
            "button.grab_focus()",
            "stack.size_flags_horizontal = Control.SIZE_EXPAND_FILL",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, script)


    def test_interactive_control_has_keyboard_focus_and_touch_target(self):
        script = (ROOT / "main.gd").read_text(encoding="utf-8")
        self.assertIn("button.focus_mode = Control.FOCUS_ALL", script)
        self.assertIn("button.custom_minimum_size = Vector2(0, 56)", script)
        self.assertIn("button.pressed.connect(_on_activate)", script)
        self.assertIn("button.grab_focus()", script)

    def test_long_instruction_and_status_text_can_wrap(self):
        script = (ROOT / "main.gd").read_text(encoding="utf-8")
        self.assertIn("instructions.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART", script)
        self.assertIn("status_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART", script)

    def test_layout_uses_bounded_margins_and_expandable_content(self):
        script = (ROOT / "main.gd").read_text(encoding="utf-8")
        self.assertIn('margin.add_theme_constant_override("margin_left", 32)', script)
        self.assertIn('margin.add_theme_constant_override("margin_right", 32)', script)
        self.assertIn("stack.size_flags_horizontal = Control.SIZE_EXPAND_FILL", script)
        self.assertNotIn("stack.custom_minimum_size = Vector2(360, 0)", script)

    def test_layout_does_not_force_a_fixed_minimum_width(self):
        script = (ROOT / "main.gd").read_text(encoding="utf-8")
        self.assertNotIn("stack.custom_minimum_size = Vector2(360, 0)", script)


if __name__ == "__main__":
    unittest.main()
