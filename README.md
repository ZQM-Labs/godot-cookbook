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

A **Godot cookbook** for location games: scenes, GDScript, project structure, and asset pipelines. Patterns are written for quest-style games built with Godot, where scenes are the building blocks and scripts stay small and readable. It is intended for game developers building playable games with Godot. Validate each pattern against your own game, Godot version, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — seeding. Pattern passes land in follow-up work; the table below lists what is planned, not what is already written.

**What this repository is:** Godot patterns — scenes, GDScript, project structure, and asset pipelines for games.

**What it contributes:** Part of the ZQM Labs game-development portfolio, and a sibling to the ZQM Computing geospatial cookbook series.

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Game developers building playable games with Godot, especially scene-based and quest-style games.

## Prerequisites

- Godot 4.7.2 (fleet-verified on Node-1; version pinned per pattern at fill time)
- The Godot editor or a text editor for GDScript
- Synthetic art and audio placeholders for the examples

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-first-scene` | A first playable scene: nodes, a player character, and a minimal game loop |
| 02 | `02-gdscript-patterns` | GDScript structure: signals, autoloads, and scene-tree organization for quest games |
| 03 | `03-project-structure` | Project layout: scenes, scripts, assets, and exports that stay organized as a game grows |
| 04 | `04-asset-pipeline` | Importing and versioning art and audio for Godot builds, including WebP textures |

## Repository layout

```text
godot-cookbook/
├── examples/  # one directory per pattern
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: first scene (01), then GDScript patterns (02)
- Second pass: project structure (03) and asset pipeline (04)

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.
