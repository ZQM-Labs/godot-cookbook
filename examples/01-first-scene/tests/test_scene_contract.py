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
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, script)


if __name__ == "__main__":
    unittest.main()
