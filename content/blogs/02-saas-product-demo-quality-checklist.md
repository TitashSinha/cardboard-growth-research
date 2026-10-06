---
title: "SaaS product demo QA: check the interface, captions and sequence before publishing"
suggested_slug: saas-product-demo-quality-checklist
meta_description: "A final-review checklist for SaaS product demos: compare the export with the live product, check readability and captions, and log corrections."
status: Editorially corrected draft v1.1; unpublished; final publication review pending
date: 2026-10-06
audience: Provisional small SaaS marketing cohort
---

# SaaS product demo QA: check the interface, captions and sequence before publishing

Review the exported video against the current product, alongside any checks in the editing project. Log each problem with a timestamp and the expected correction. A polished animation does not establish an accurate explanation.

This guide covers the final review of a demo you have already produced. If you are still deciding how to produce one, start with [How to choose a video editor for SaaS product demos](../revisions/01-workflow-switch-evidence-v1.2.md).

## Use the current product as the reference

Open the product beside the video and pause at each scene. Compare:

- **Labels and control names.** Does the video say what the product says?
- **State changes.** If a toggle flips or a status updates after a click, does the video show it?
- **Sequence.** Could a viewer repeat the steps in the order shown? Look for a setting changed off-screen or a step cut for time.
- **Currency.** Has the product changed since you recorded? Mark any scene that no longer matches as outdated instead of editing around it.

Use the product itself as the reference. A regenerated or imitation interface can look right and still differ from what a viewer sees after signing in.

## Check readability in the exported file

Watch the exported file at the size your viewer is likely to use: a laptop browser window, a phone, a shared-screen call. The editing canvas can be larger than that, so a label that looks fine there may be hard to read in the export.

No fixed font size or hold time works for every demo. Use a practical test instead: can you read every label the narration mentions without pausing or leaning in? Inspect these first:

- crops that cut off the edge of a menu or panel
- zooms that blur small text
- captions or overlays sitting on top of a control
- scenes that change before a viewer can find the element being discussed

If an edit changes a layer's position, size or crop, recheck the label afterward. Descript's [Scene Editor documentation](https://help.descript.com/visuals/scene-editor-overview) describes a layer toolbar for adjusting size, position and cropping, which is the kind of control to look for in any editor. The documentation does not say a label stays readable after such an edit, so that check stays with you.

## Match narration, captions and transitions to the action

Play the video with sound and read the captions at the same time. Check that:

- product terms are spelled and capitalized as they appear in the product
- shortened captions keep the sentence's meaning
- the narration names a control while it is on screen, not before or after
- a transition does not hide the state change the viewer needs to see

Also check how captions will be delivered. Descript's [subtitle export documentation](https://help.descript.com/export-and-share/subtitles) separates SRT/VTT subtitle files, which you upload alongside a video, from captions that stay on the video itself. If you publish with an uploaded file, review that file as its own deliverable. If captions are part of the picture, review the export.

## Make feedback easy to act on

"Fix the captions" leaves the editor guessing. A correction log gives each issue a timestamp, a specific change, an owner and a status.

| Timestamp | Issue | Expected correction | Owner | Recheck status |
|---|---|---|---|---|
| 00:42 | **Illustrative row:** caption covers the control the narration tells the viewer to select | Move the caption clear of the control; keep the wording unchanged | Editor | Open: recheck in the next export |

Write each correction so someone could make it without a follow-up question. If a reviewer is unsure of the fix, record the observation and leave the correction for the editor to propose.

**Illustrative example:** the narration says "select the control in the upper right," and a caption sits on top of that control from 00:41 to 00:44. The editor moves the caption, then checks the exported scene to confirm the control is visible while it is mentioned. The row above records this.

## Recheck the corrected export

Re-export and review each logged timestamp in the new file. Then watch the neighboring scenes, because changing one scene's length can shift what follows.

When every row is closed, approve one named version, for example by file name, export date and approver. If the product interface changes afterward, treat that approval as out of date.

**Next step:** take one exported demo and build a correction log from the table above before sending it for review.

---

**Editorial note:** Independent article prepared with AI assistance. The checks above are proposed editorial practices; they were not tested and were not confirmed as problems across exploratory maker conversations, which were not a screened sample of the target cohort. Descript documentation was read on October 6, 2026 and describes features only; it does not guarantee demo accuracy. No Cardboard product test, account setup or generated output occurred. Editorial and publication review are pending.
