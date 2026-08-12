# AGENTS.md

## Purpose

This repository is a learning-state repository for building economic intuition from a physics / dynamical-systems perspective. The Markdown vault is the source of truth for learned concepts, and repository updates should reflect what has actually been learned.

## Teaching and note-taking style

- Prefer models, equations, state variables, flows, feedback loops, fixed points, stability, comparative statics, and dynamic paths over terminology-first explanations.
- When a new concept is learned, connect it to the existing knowledge graph and update the relevant Markdown notes.
- Keep explanations reproducible and mathematically grounded where possible.

## Figures and diagrams policy

When visual material is needed for teaching or documentation:

1. **Do not use text-based schematic diagrams** when the concept can be represented by a real mathematical plot, simulation, phase diagram, trajectory, or data visualization.
2. **Do not use generative image tools** for teaching figures.
3. Figures should be generated from **real functions, equations, numerical simulations, or real data** using small reproducible scripts.
4. Put plotting / simulation source code in `Scripts/`.
5. Markdown notes should reference the generated PNG files under `Figures/`.
6. **Do not manually upload or maintain generated PNG files as the source of truth.** The script is the source of truth.
7. **Do not commit generated PNG files just to publish a figure.** The deploy workflow should regenerate them automatically from the scripts.
8. The GitHub Pages / Quartz deploy pipeline should:
   - install the required Python plotting dependencies;
   - run the figure-generation scripts;
   - generate PNG files into `Figures/`;
   - copy/publish those generated figures with the site.
9. Prefer figures such as:
   - real function plots;
   - phase diagrams;
   - steady-state and comparative-statics plots;
   - convergence paths;
   - growth-rate paths;
   - numerical simulation results;
   - plots from real economic data.
10. Avoid ASCII art, box-and-arrow text diagrams, or purely textual sketches as substitutes for mathematical visualizations when a proper plotted figure is possible.

### Figure workflow

Use this workflow by default:

```text
model / equation / data
        ->
small reproducible script in Scripts/
        ->
PNG generated during deploy into Figures/
        ->
referenced from the relevant Markdown note
```

In short: **real math first, script-generated PNGs, scripts committed, PNGs regenerated automatically during deploy.**
