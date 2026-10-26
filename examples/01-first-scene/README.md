# 01 — First playable scene

A minimal Godot 4 scene built entirely from GDScript-created UI controls. It demonstrates the project entry point, a scene resource, a focused interactive button, and visible state changes without external art assets.

## Run it

Open this directory as a project in Godot 4.7.2, then run the project. The button supports mouse, touch, and standard keyboard activation when focused. Resize the window to check the centered layout.

If Godot is installed on the command line:

```sh
godot --path . --editor
```

Run the project from the editor or with the project's main scene. The contract tests below are static checks; they do not parse GDScript or replace running the project in the Godot editor.

## Static contract tests

Requires Python 3.11 or newer:

```sh
python -m unittest discover -s tests -v
```

## Files

- `project.godot` — pinned project feature metadata and main-scene entry point.
- `main.tscn` — root Control scene and script reference.
- `main.gd` — builds the UI and handles activation state.
- `tests/test_scene_contract.py` — verifies that scene references resolve and the interaction/status contract remains present.

## Design notes

- Keep the scene tree and startup path simple before adding autoloads or scene transitions.
- Prefer standard Controls for form-like interactions because they provide built-in focus and keyboard activation.
- Expose meaningful state in text, not only color or animation.
- This counter is presentation state only. Never use a client-side counter as proof of a purchase, entitlement, or trusted score.
- Static checks do not guarantee engine compatibility. Run the project with the documented Godot version before using it in another project.
