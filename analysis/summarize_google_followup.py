"""Summarize retained India page-one/two headings, separately from old field notes."""
import csv
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

def summarize():
    rows = []
    for path in sorted((ROOT / 'research/captures/google-india-2026-10-05').glob('G*-p*.json')):
        r = json.loads(path.read_text(encoding='utf-8'))
        official = [h for h in r['headings'] if urlparse(h['url']).hostname in {'cardboard.ai', 'www.cardboard.ai', 'usecardboard.com', 'www.usecardboard.com'}]
        thirdparty = [h for h in r['headings'] if h not in official and ('cardboard' in h['title'].lower() or '/cardboard' in h['url'].lower())]
        rows.append({'query_id': r['id'], 'query': r['requested_query'], 'page': r['page'],
                     'captured_utc': r['captured_utc'], 'country_requested': r['country_requested'],
                     'country_observed': r['country_observed'], 'heading_count': len(r['headings']),
                     'official_cardboard_headings': len(official), 'thirdparty_cardboard_headings': len(thirdparty),
                     'thirdparty_urls': ';'.join(h['url'] for h in thirdparty),
                     'local_capture': f'captures/google-india-2026-10-05/{path.name}'})
    return {'cohort': '2026-10-05 India English signed-in pws=0; separate from original US-requested field notes',
            'queries': len({r['query_id'] for r in rows}), 'page_captures': len(rows),
            'linked_h3_headings': sum(r['heading_count'] for r in rows),
            'official_cardboard_headings': sum(r['official_cardboard_headings'] for r in rows),
            'thirdparty_cardboard_headings': sum(r['thirdparty_cardboard_headings'] for r in rows),
            'pages': rows, 'limits': ['Heading ordinal is capture order, not an absolute organic rank.',
                                    'AI Overviews were not expanded; not a full citation audit.',
                                    'No universal rank, change, volume, traffic or causal growth inference.',
                                    'Titash post RP01 in G03 is our own distribution artifact, not independent buyer evidence.']}

if __name__ == '__main__':
    result = summarize()
    p = ROOT / 'research'
    (p / 'google-followup-summary-2026-10-05.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    with (p / 'google-followup-2026-10-05.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(result['pages'][0]))
        writer.writeheader()
        writer.writerows(result['pages'])
    print(json.dumps(result, indent=2))
