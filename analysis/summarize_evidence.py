"""Reproduce inventory counts and keep unlike discovery cohorts separate."""
import argparse, csv, json
from collections import Counter
from pathlib import Path
from summarize_google_followup import summarize as summarize_google_followup

ROOT = Path(__file__).resolve().parents[1]

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def summarize():
    research = ROOT / 'research'
    google = rows(research / 'search-baseline.csv')
    ai = rows(research / 'ai-discovery-baseline.csv')
    sources = rows(research / 'sources.csv')
    metadata = json.loads((research / 'public-metadata-refresh.json').read_text(encoding='utf-8'))
    sitemap = next(r['locations'] for r in metadata if 'locations' in r)
    complete = [r for r in ai if r['status'] == 'complete']
    cohorts = Counter((r['date'], r['model'], r['effort']) for r in complete)
    # Explicitly chosen exclusions are part of the sampling definition, not a classifier.
    nonbrand_google = [r for r in google if r['query_id'] not in {'Q06','Q07','Q08','Q20'}]
    nonbrand_ai = [r for r in complete if r['test_id'] not in {'AI10','AI11'}]
    followup = summarize_google_followup()
    manifest = json.loads((research / 'artifact-manifest.json').read_text(encoding='utf-8'))
    for item in manifest['articles']:
        assert (ROOT / item['current_draft']).is_file() and (ROOT / item['brief']).is_file()
    return {
        'google_observations': len(google),
        'google_india_followup_queries_separate_cohort': followup['queries'],
        'google_india_followup_page_captures': followup['page_captures'],
        'google_india_followup_official_cardboard_headings': followup['official_cardboard_headings'],
        'google_india_followup_thirdparty_cardboard_headings': followup['thirdparty_cardboard_headings'],
        'google_nonbrand_observations': len(nonbrand_google),
        'google_nonbrand_with_official_result_in_inspected_headings': sum(bool(r['official_cardboard_positions']) for r in nonbrand_google),
        'chatgpt_completed_observations': len(complete),
        'chatgpt_nonbrand_observations_including_repeat': len(nonbrand_ai),
        'chatgpt_nonbrand_cardboard_mentions': sum(r['mention'] == 'yes' for r in nonbrand_ai),
        'chatgpt_cohorts': [{'date':d,'model':m,'effort':e,'observations':n} for (d,m,e),n in sorted(cohorts.items())],
        'source_entries': len(sources),
        'unique_source_ids': len({r['evidence_id'] for r in sources}),
        'competitor_alternatives': len(rows(research / 'competitors.csv')),
        'sitemap_urls_in_retained_refresh': len(sitemap),
        'blog_urls_in_retained_refresh': sum('/blog/' in u for u in sitemap),
        'current_distinct_article_drafts': len(manifest['articles']),
        'current_article_brief_tasks': len(manifest['articles']),
        'blog_drafts': len(list((ROOT/'content/blogs').glob('*.md'))),
        'briefs': len(list((ROOT/'content/briefs').glob('*.md'))),
        'participant_feedback_records': len(rows(ROOT/'experiments/workflow-fit/results.csv')) if (ROOT/'experiments/workflow-fit/results.csv').exists() else 0,
        'limits': ['Google field notes lack full result lists; location unknown.', 'AI cohorts differ in date/effort; two branded prompts excluded from unaided observations.', 'AI12 repeats AI01 with different effort; not a matched comparison.', 'Counts are inventory/sample observations, not demand or business outcomes.', 'blog_drafts and briefs count stored Markdown files; current article/brief tasks use the explicit artifact manifest.']
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, help='Optional JSON summary path; derived file may be regenerated')
    args = parser.parse_args()
    result = json.dumps(summarize(), indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result+'\n', encoding='utf-8')
    print(result)
