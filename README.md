# Godot Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Labs</strong><br>
  <a href="https://github.com/ZQM-Labs">ZQM Labs</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **Godot cookbook** for quest-style games: scenes, GDScript, input, project structure, and asset pipelines. Examples should be small enough to understand, runnable in the documented engine version, and explicit about what static tests do and do not verify.

## Repository role and status

**Status:** Active, public — first-scene project and static contract tests added. The pattern list distinguishes implemented content from planned work.

**What this repository is:** Practical Godot patterns for scene lifecycle, UI/input, project structure, and asset delivery.

**What it contributes:** Part of the ZQM Labs game-development portfolio. It complements ZQM Computing's geospatial engineering repositories by focusing on the game client and playable experience.

**Quality bar:** Keep scene references valid, use engine-native controls where possible, include keyboard-accessible interactions, and test with the documented Godot version. Static checks are useful guardrails but do not establish engine runtime compatibility.

## Who this is for

Game developers building playable games with Godot, especially scene-based and quest-style games.

## Prerequisites

- Godot 4.7.2 (the version targeted by this example)
- Python 3.11+ for dependency-free static contract tests
- The Godot editor or command-line executable for runtime verification

## Patterns

### 01 — First playable scene (implemented)

[Open the first-scene example](examples/01-first-scene/). Includes a project entry point, a root scene, programmatically constructed UI, a keyboard-focusable button, a visible counter/status, and static reference checks.

### 02 — GDScript patterns (planned)

Signals, script responsibilities, autoload boundaries, and scene-tree organization for quest games.

### 03 — Project structure (planned)

A maintainable layout for scenes, scripts, assets, and exports as a game grows.

### 04 — Asset pipeline (planned)

Importing and versioning art/audio, WebP textures, export presets, and reproducible builds.

## Quick start

Open `examples/01-first-scene/project.godot` in Godot 4.7.2 and run the project.

Run static contract checks from the example directory:

```sh
cd examples/01-first-scene
python -m unittest discover -s tests -v
```

These checks verify project and scene references and key interaction/status strings; they do not parse GDScript or replace an engine smoke test.

## Repository layout

```text
godot-cookbook/
├── .github/workflows/examples.yml
├── examples/
│   └── 01-first-scene/
│       ├── project.godot
│       ├── main.tscn
│       ├── main.gd
│       ├── README.md
│       └── tests/
│           └── test_scene_contract.py
├── README.md
└── LICENSE
```

## Engineering principles

- Keep scene setup explicit and startup paths easy to trace.
- Use signals for interactions and avoid hidden global state until there is a concrete need.
- Prefer built-in UI controls for keyboard focus and activation.
- Expose important state as readable text, not only visual effects.
- Do not treat client-side state as proof of purchase, entitlement, or trusted score.
- State the engine version and distinguish static checks from runtime testing.

## Roadmap

1. Add GDScript signal/autoload patterns with small examples.
2. Add a reusable quest-state model with deterministic tests.
3. Add project layout and asset-import/export guidance.
4. Add headless Godot validation when the pinned engine is available in CI.

## How this cookbook connects to the ZQM Labs stack

Use this repository for the **game client and engine layer**. It is not the source of truth for browser automation, identity, or payment state.

| Need | Related cookbook | Contract between layers |
|---|---|---|
| Validate browser-visible game flows | [Playwright Cookbook](https://github.com/ZQM-Labs/playwright-cookbook) | Test user-visible behavior against a local/synthetic fixture first; configure a live game target explicitly and separately. |
| Player identity and private profile access | [PocketBase Cookbook](https://github.com/ZQM-Labs/pocketbase-cookbook) | The server derives identity from the authenticated session; client-side state is not authorization. |
| Checkout and paid fulfillment | [Stripe Cookbook](https://github.com/ZQM-Labs/stripe-cookbook) | Treat verified server-side payment events and durable fulfillment as authoritative; never unlock paid content from a client redirect. |

### Integration sequence

1. Build the scene and player interaction here.
2. Exercise the critical path with Playwright using deterministic fixtures.
3. Add authenticated server requests through PocketBase, with access rules tested for both allowed and denied cases.
4. For paid products, use Stripe's verified fulfillment flow; persist entitlements server-side and have the game request authorization from the backend.
5. Add an end-to-end test only after each boundary has an explicit test environment and synthetic data.

These repositories are **complementary recipes, not a pre-integrated application**. Their examples do not automatically share schemas, credentials, deployments, or runtime configuration. Integration work must document the API contract, identity mapping, entitlement schema, environment variables, and failure/retry behavior before connecting real services.

## Contributing

Each pattern should include a minimal project or runnable example, exact verification commands, target engine version, known limitations, and input/accessibility considerations. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.
