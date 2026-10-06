# Presentation handoff

October 6, 2026. Ten slides, native editable text and shapes, 16:9, Arial. Research story: observation → exploratory learning → intervention → missing formal verdict → actual editorial revision → package → prospective tests.

- [Editable PowerPoint](cardboard-growth-work-sample.pptx)
- [Rendered PDF](cardboard-growth-work-sample.pdf)
- [Claim and number map](source-to-number-map.md)
- [Final package acceptance](../quality/final-package-acceptance-2026-10-06.md)

Source notes are embedded in each slide. PDF readers should use the number map. The deck has no flattened screenshot slides, external image assets, charts, synthetic buyer responses or genuine-product-output claims. Text remains editable; authoring rows are native text shapes, not data tables.

## Verification and reproduction

Created with the bundled Artifact Tool JavaScript runtime. Package integrity, geometry/font policy and first-party re-import passed. Final PPTX was converted with LibreOffice to PDF; every PDF page was rendered at 1280 × 720 and individually inspected. This is a LibreOffice rendering check, not a claim of native PowerPoint execution.

[Builder](build-deck.mjs) is the reproducible source. Obtain the configured Node/Python/package paths using the workspace dependency tool. Copy the builder into the ignored `.build/deck` directory and link that directory's `node_modules` to the bundled packages. Set absolute `SKILL_DIR`, `RUNTIME_NODE_MODULES`, `RUNTIME_NODE` and `RUNTIME_PYTHON`; run the builder with the bundled Node from the repository root. The skill's artifact-start marker is required before a new authoring operation. Finalizer output names must be new; revise the builder's final filename rather than overwriting an existing checked output.

Convert the checked PPTX using installed LibreOffice's `soffice.com --headless --convert-to pdf`, with a task-specific `UserInstallation` and explicit output directory. Render that PDF with an available configured PDF renderer and inspect every slide. Private build previews/validation receipts remain ignored; final files and the acceptance summary are retained here.
