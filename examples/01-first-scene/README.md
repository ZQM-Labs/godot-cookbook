# 01 — First playable scene

A minimal Godot 4 scene built entirely from GDScript-created UI controls. It demonstrates the project entry point, a scene resource, a focused interactive button, and visible state changes without external art assets.

## Run it

Open this directory as a project in Godot 4.7.2, then run the project. The button supports mouse, touch, and standard keyboard activation when focused. Resize the window, including to a narrow mobile-sized width, to check the centered layout. The content stack expands into the available width instead of forcing a 360-pixel minimum.

If Godot is installed on the command line:

```sh
godot --path . --editor
```

Run the project from the editor or with the project's main scene. CI also runs a headless smoke test using the pinned Godot 4.7.2 engine; that test parses and instantiates the scene and verifies the activation counter and status text update. It is not a visual viewport test and does not replace manual layout checks in the editor.

## Automated tests

Static contract checks require Python 3.11 or newer:

```sh
python -m unittest discover -s tests -v
```

The engine-backed smoke test requires Godot 4.7.2:

```sh
godot --headless --path . --script res://tests/runtime_smoke.gd
```

The smoke test loads the actual scene, checks the generated button and labels, emits the button's `pressed` signal, and asserts that both visible state labels advance to activation 1. CI downloads the official Godot 4.7.2 Linux binary and verifies its SHA-256 before execution.

## Files

- `project.godot` — pinned project feature metadata and main-scene entry point.
- `main.tscn` — root Control scene and script reference.
- `main.gd` — builds the UI and handles activation state.
- `tests/test_scene_contract.py` — verifies source-level scene and accessibility contracts.
- `tests/runtime_smoke.gd` — loads the scene in the real Godot engine and checks activation behavior.

## Design notes

- Keep the scene tree and startup path simple before adding autoloads or scene transitions.
- Prefer standard Controls for form-like interactions because they provide built-in focus and keyboard activation.
- Expose meaningful state in text, not only color or animation.
- This counter is presentation state only. Never use a client-side counter as proof of a purchase, entitlement, or trusted score.
- The headless runtime test verifies parsing and interaction state, not rendered layout. It does not measure actual control sizes or prove usability at a particular viewport. Validate narrow and desktop layouts manually in the Godot editor before shipping.

The static contract suite also guards the button's keyboard focusability and 56-pixel minimum height, wrapping of long instruction/status text, and expandable content with bounded horizontal margins. These checks protect intended source-level affordances; they do not measure the rendered control size or prove usability at a specific viewport. Validate in Godot at narrow and desktop sizes before treating the layout as runtime-verified.
