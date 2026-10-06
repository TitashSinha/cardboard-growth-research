import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

// Run a copy from .build/deck with a node_modules link to the bundled runtime.
// Set SKILL_DIR and RUNTIME_PYTHON to the configured presentation skill/runtime.
const root = process.cwd();
const { SKILL_DIR, RUNTIME_PYTHON } = process.env;
if (!path.isAbsolute(SKILL_DIR ?? '') || !path.isAbsolute(RUNTIME_PYTHON ?? '')) {
  throw new Error('Set absolute SKILL_DIR and RUNTIME_PYTHON.');
}
const { resolvePresentationFont, finalizePresentation } = await import(
  pathToFileURL(path.join(SKILL_DIR, 'container_tools/artifact_tool_utils.mjs')).href,
);
const family = resolvePresentationFont({ availableFonts: ['Arial'] });
const p = Presentation.create({ slideSize: { width: 1280, height: 720 } });
const C = { paper: '#F4F1E9', ink: '#202D2A', muted: '#56635C', accent: '#AD562F', rule: '#D5D8CB', white: '#FFFFFF' };
function box(s, value, x, y, w, h, size = 26, color = C.ink, bold = false) {
  const sh = s.shapes.add({ geometry: 'textbox', position: { left: x, top: y, width: w, height: h }, fill: 'none', line: { fill: 'none', width: 0 } });
  sh.text = value;
  sh.text.style = { typeface: family, fontSize: size, bold, color, autoFit: 'none' };
  return sh;
}
function rect(s,x,y,w,h,fill) {
  return s.shapes.add({ geometry: 'rect', position: { left:x,top:y,width:w,height:h },fill,line:{fill:'none',width:0} });
}
function base(title,kicker,notes, dark=false) {
  const s=p.slides.add();s.background.fill=dark?C.ink:C.paper;
  box(s,kicker.toUpperCase(),64,34,1120,32,18,dark?'#D5D8CB':C.accent,true);
  box(s,title,64,88,1150,114,44,dark?C.paper:C.ink,true);
  rect(s,64,658,1152,1,dark?'#56635C':C.rule);
  box(s,'Titash Sinha  /  Independent, AI-assisted work sample  /  6 October 2026',64,673,1080,25,16,dark?'#D5D8CB':C.muted);
  box(s,String(p.slides.items.length).padStart(2,'0'),1160,673,56,25,16,dark?'#D5D8CB':C.muted);
  s.speakerNotes.textFrame.setText(notes);
  return s;
}
function label(s,t,x,y,w=520){box(s,t,x,y,w,38,24,C.accent,true);}
function body(s,t,x,y,w=520,h=120){box(s,t,x,y,w,h,26);}
function limit(s,t,y=603){box(s,t,64,y,1152,42,19,C.muted);}

let s=base('Cardboard\nWorkflow learning into useful content','Growth research + editorial work',
  'Scope: README.md; quality/final-repository-review-2026-10-06.md; D040/D041 in decisions.md. Independent package, unpublished, no Cardboard account/internal access. EX01 stopped with partial exploratory evidence. No company growth outcome.',true);
box(s,'Identify the work that needs help.\nKeep the editor that already works.',64,330,1020,116,38,C.paper);
box(s,'Research  →  exploratory learning  →  articles + evaluation copy  →  proposed tests',64,526,1100,64,24,'#D5D8CB');

s=base('A specific offer inconsistency,\nwith an unmeasured business effect','Observation',
  'Three specifically inspected official articles: research/product-audit.md, research/offer-refresh-2026-10-04.md and research/website-hygiene.md. Dates October 2–4, 2026. Exact comparisons retained there; not a census. Sources https://www.cardboard.ai/pricing and three dated blog routes. No lost-signup/comprehension evidence. Historical claims not current access terms.');
box(s,'3',64,235,180,128,96,C.accent,true);
box(s,'checked official articles',248,250,800,48,30,C.ink,true);
body(s,'Offer claims differed from the inspected pricing display or from one another.',248,308,860,100);
label(s,'WHAT THIS ESTABLISHES',64,458);
body(s,'Information needs reconciliation.\nConfirm the source of offer truth.',64,506,520,90);
label(s,'WHAT TO TEST NEXT',670,458);
body(s,'Can a relevant reader explain access\nand choose a truthful next action?',670,506,545,90);
limit(s,'No measured buyer confusion, conversion loss or revenue effect.');

s=base('Discovery is a bounded inventory,\nnot a market-wide visibility verdict','Research scope',
  'research/evidence-summary.json and research/collection-method.md: 20 original Google observations, 12 completed ChatGPT observations, 72 source entries. Original Google lists incomplete/location unknown. ChatGPT cohorts differ/date/effort, branded controls and repeated wording. Separate October 5 India/English cohort: research/google-followup-summary-2026-10-05.json and review; 5 queries, 10 page captures, 92 headings, 0 owned, 1 third-party YC Cardboard heading. Not comparable rank trend.');
for(const [x,n,t,d] of [[64,'20','Google observations','Original field-note cohort'],[448,'12','ChatGPT observations','Completed; mixed settings'],[832,'72','Source records','Inventory, including rereads']]) {
  box(s,n,x,228,320,100,76,C.accent,true);box(s,t,x,341,350,43,28,C.ink,true);box(s,d,x,395,350,66,23,C.muted);
}
rect(s,64,494,1152,87,'#E4E8DE');
box(s,'Separate India / English check: 5 queries, 92 captured headings',88,508,1110,32,25,C.ink,true);
box(s,'0 owned Cardboard headings; 1 third-party YC result',88,548,1110,30,24,C.ink);
limit(s,'Incomplete original Google retention; mixed AI cohorts. No universal invisibility or ranking trend.');

s=base('Different production stages\nneed different kinds of help','Exploratory maker learning',
  'Generalized observations only: experiments/workflow-fit/collection-closeout-2026-10-06.md and content/revisions/01-workflow-switch-v1.2-notes.md. Private mappings/exact replies outside Git. No frequency, eligible buyer count or representative inference. Some accounts are maker/service-provider context, eligibility unknown.');
const stages=[['Planning + graphics','Ideas, storyboards and interface preparation'],['Animation + polish','Timing, easing, sound and precise creative control'],['Corrections + handoff','Editable structure, assets and access matter'],['Incumbent fit','AI assistance can coexist with manual finishing']];
stages.forEach(([a,b],i)=>{const y=228+i*86;box(s,a,64,y,345,44,28,C.ink,true);box(s,b,440,y,760,65,27);if(i<3)rect(s,64,y+68,1152,1,C.rule);});
limit(s,'Useful context, not screened SaaS-buyer validation or evidence of Cardboard performance.');

s=base('EX01: what the replies helped us learn','Conversation findings',
  'Current basis: experiments/workflow-fit/reply-evidence-summary-2026-10-06.md and D043. Retained private audit/ledger observations support generalized workflow learning. Exact replies and identities outside Git. Original structured protocol and closeout preserved, not executed as designed. Worksheet participation is not an admission criterion for this conversation synthesis. Named-brand questions yield prompted opinions, not unaided awareness. No Cardboard performance or purchase behavior established.');
const findings=[['Workflow','Planning, animation and finishing need different help.'],['Switching considerations','Control, editability and setup matter when comparing methods.'],['Cardboard opinions','Keep stated non-use separate from opinions and ambiguous use.']];
findings.forEach(([a,b],i)=>{const y=232+i*108;box(s,a,64,y,1130,41,29,C.ink,true);box(s,b,64,y+47,1120,55,27);});
rect(s,64,571,1152,71,'#E4E8DE');
box(s,'Enough to guide the content. Product performance and purchase intent remain unknown.',86,586,1110,48,23);

s=base('Actual replies changed the first article.\nThe aid revision remains an untested prototype.','Result → editorial revision',
  'Article before: content/blogs/01-workflow-switch.md and content/revisions/01-workflow-switch-seo-v1.1.md. After: content/revisions/01-workflow-switch-evidence-v1.2.md. Reasoning: 01-workflow-switch-v1.2-notes.md. Aid v2: experiments/workflow-fit/materials/decision-aid-v2-exploratory.md; revision-log.md. Codex synthesized/drafted under Titash authorization. No respondent review or aid-task feedback.');
label(s,'BEFORE: A GENERAL CHOICE FRAME',64,230);
body(s,'Ask whether a different editor would\nhelp with a real recent video.',64,286,525,110);
body(s,'Correction and output checks were\npresent, but less stage-specific.',64,414,525,110);
label(s,'AFTER: DIAGNOSE THE STAGE',670,230);
body(s,'Separate planning, source footage,\nassembly, motion and finishing.',670,286,545,110);
body(s,'Distinguish useful craft from rework.\nInspect editability and whole-project fit.',670,414,545,110);
limit(s,'Reply-informed editorial revision; no demonstrated reader effect or executed aid feedback.');

s=base('Five task-specific articles\nand a complete evaluation-page copy sample','Content package',
  'research/artifact-manifest.json lists five current drafts and brief references. Article 1 v1.2 plus corrected articles 2–5. quality/final-editorial-review-2026-10-06.md: distinct jobs, narrow coverage rereads, publication gates. Page: content/conversion/saas-demo-evaluation-page-v1.md and notes. Illustrative storyboard not product output. Drafts unpublished; exact-query/canonical/company approval and public routes remain release dependencies.');
const topics=['Choose a workflow without assuming a switch','QA a recorded SaaS product demo','Inspect an editable AI-video handoff','Compare Cardboard and Descript by workflow','Adapt one demo feature for LinkedIn'];
topics.forEach((t,i)=>{box(s,String(i+1).padStart(2,'0'),64,230+i*67,64,40,25,C.accent,true);box(s,t,148,230+i*67,690,49,26);});
rect(s,898,224,318,340,'#E4E8DE');
box(s,'PAGE SAMPLE',922,246,272,38,21,C.accent,true);
box(s,'One feature.\nOne explanation.',922,307,270,118,34,C.ink,true);
box(s,'Inputs → first cut →\ncorrection → export checks',922,452,270,92,24);
limit(s,'Unpublished. Illustrative storyboard, genuine-proof requirements and truthful access links.');

s=base('Measurement follows delivered value,\nnot activity alone','AAARRR specification',
  'strategy/funnel.md, strategy/measurement-plan.md, strategy/measurement-events.csv: six AAARRR stages, 12 proposed event contracts. Activation useful delivery within 7 days provisional; retention distinct job in 30 days provisional; revenue settled positive access, refunds/net distinct; payment may precede delivery so revenue denominator unpaid at entry. Referral attributable eligible new account useful delivery. No implementation, baseline or result.');
const measures=[['Awareness','Fixed query/prompt observations, not market share'],['Acquisition','Eligible route sessions and explicit evaluation actions'],['Activation','User-confirmed useful delivery'],['Retention','Another distinct job; cadence still unknown'],['Revenue','Settled paid access; refunds and net revenue separate'],['Referral','Attributable new account reaching useful delivery']];
measures.forEach(([a,b],i)=>{const y=220+i*60;box(s,a,64,y,238,40,25,C.ink,true);box(s,b,337,y,878,45,25);});
limit(s,'6 stages / 12 proposed event contracts. No instrumented events, company baseline or growth result.');

s=base('Test comprehension first.\nProduct proof and commercial impact come later.','Prioritized prospective backlog',
  'strategy/experiment-backlog.md: EX02 page comprehension, EX03 conditional offer comprehension, EX04 genuine correction comparison, EX05 article usefulness, EX06 company commercial route. Five proposals, not run/authorized. Small pilots are formative, not population or conversion estimates. Existing measurement event contracts reused. No new outreach/account/spend/publication authorized.');
const tests=[['EX02  Page comprehension','Can readers identify the task, proof and next action?'],['EX03  Offer comprehension','Only after company-confirmed terms and relevant confusion.'],['EX04  Genuine correction comparison','Same inputs; record all work, failures and access constraints.']];
tests.forEach(([a,b],i)=>{const y=228+i*110;box(s,a,64,y,1110,42,29,C.ink,true);box(s,b,64,y+47,1110,49,26);});
limit(s,'Then EX05 article usefulness and EX06 company-route testing. Proposed; no result or uplift forecast.');

s=base('A reviewable contribution,\nwith clear ownership and limits','Handoff',
  'strategy/contribution-log.md; decisions.md D040/D041; quality/final-repository-review-2026-10-06.md. Titash chose incumbent adequacy first and authorized evidence-bound revisions/package. Codex performed public research, synthesis/drafting and package checks; other AI drafted supplied articles, corrected here. Founder refreshed October 6 via https://www.ycombinator.com/companies/cardboard and https://www.cardboard.ai/; pitch outreach/founder-message.md remains unsent, repo private/access not granted.');
label(s,'TITASH',64,232);body(s,'Set scope, challenged switching assumptions\nand directed the work-sample decisions.',64,285,540,120);
label(s,'AI ASSISTANCE',670,232);body(s,'Public research, synthesis, drafting,\neditorial correction and package checks.',670,285,545,120);
rect(s,64,452,1152,113,'#E4E8DE');
box(s,'Next business action: authorized founder handoff with usable access',88,470,1098,43,28,C.ink,true);
box(s,'Then company/editor review, confirmed proof and terms, and prioritized testing.',88,520,1090,37,24);
limit(s,'Pitch is UNSENT. No affiliation, product access, completed validation or company outcome claimed.');

const staging=path.join(root,'.build/deck');await fs.mkdir(staging,{recursive:true});
const candidate=path.join(staging,'candidate.pptx');
await (await PresentationFile.exportPptx(p)).save(candidate);
const result=await finalizePresentation({workspaceDir:root,candidatePath:candidate,
  finalPath:path.join(root,'presentation/cardboard-growth-work-sample-v1.1.pptx'),
  pythonExecutable:RUNTIME_PYTHON,
  integrityValidatorPath:path.join(SKILL_DIR,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(SKILL_DIR,'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],
  fontPolicy:{basis:'design',families:[family]},verifyArtifactToolImport:true,
  requiredNativeTableOwnerSlides:[],requiredNativeChartOwnerSlides:[],
  receiptPath:path.join(staging,'validation-v1.1.json')});
console.log(JSON.stringify(result));
