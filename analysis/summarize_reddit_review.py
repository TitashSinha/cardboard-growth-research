"""Reproduce the bounded Monday snapshot inventory; never infer missing comments."""
import csv
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research'

def summarize():
    with (RESEARCH / 'reddit-reply-classification-2026-10-05.csv').open(encoding='utf-8', newline='') as f:
        classifications = list(csv.DictReader(f))
    keys = [(r['post_id'], r['comment_id']) for r in classifications]
    assert len(keys) == len(set(keys)), 'Duplicate classification'
    by_key = dict(zip(keys, classifications))
    posts, all_authors, retained_keys = [], set(), set()
    for path in sorted((RESEARCH / 'captures/reddit-monday-2026-10-05').glob('RP*.json')):
        capture = json.loads(path.read_text(encoding='utf-8'))
        pid = capture['registry_id']
        selected = []
        for comment in capture['comments']:
            key = (pid, comment['comment_id'])
            assert key not in retained_keys, 'Duplicate captured comment'
            retained_keys.add(key)
            cls = by_key[key]
            assert (cls['kind'] == 'author') == (comment['author'] == capture['post']['author'])
            assert cls['kind'] in {'human', 'author', 'bot'}
            top = comment['depth'] == '0'
            if cls['substantive_top_level'] == 'yes':
                assert top and cls['kind'] == 'human'
            if cls['explicit_firsthand_top_level'] == 'yes':
                assert cls['substantive_top_level'] == 'yes'
            selected.append((comment, cls))
        humans = [(c, r) for c, r in selected if r['kind'] == 'human']
        authors = {c['author'] for c, r in humans}
        all_authors.update(authors)
        # No retained text contains the term. If a future refresh does, manual
        # AI-editor vs literal-material and recommendation/use coding is required.
        assert not any('cardboard' in (c['body'] or '').lower() for c, r in selected), 'Recode new brand mention manually'
        assert 'cardboard' not in (capture['post']['body'] or '').lower(), 'Inspect brand priming'
        elapsed = datetime.fromisoformat(capture['captured_utc']) - datetime.fromisoformat(capture['post']['created_utc'])
        posts.append({
            'post_id': pid, 'snapshot_utc': capture['captured_utc'],
            'elapsed_hours': round(elapsed.total_seconds() / 3600, 2),
            'platform_badge': int(capture['post']['platform_comment_count']),
            'retained_nodes': len(selected),
            'badge_minus_retained': int(capture['post']['platform_comment_count']) - len(selected),
            'author_comments': sum(r['kind'] == 'author' for c, r in selected),
            'bot_comments': sum(r['kind'] == 'bot' for c, r in selected),
            'visible_non_author_comments': sum(r['kind'] != 'author' for c, r in selected),
            'human_non_author_comments': len(humans),
            'distinct_human_accounts': len(authors),
            'substantive_top_level_responses': sum(r['substantive_top_level'] == 'yes' for c, r in selected),
            'behavioral_top_level_responses': sum(r['substantive_top_level'] == 'yes' and r['detail'] == 'behavioral' for c, r in selected),
            'explicit_firsthand_top_level_responses': sum(r['explicit_firsthand_top_level'] == 'yes' for c, r in selected),
            'disclosed_builder_top_level_responses': sum(r['substantive_top_level'] == 'yes' and r['affiliation'] == 'disclosed_builder' for c, r in selected),
            'possible_brand_association_top_level_responses': sum(r['substantive_top_level'] == 'yes' and r['affiliation'] == 'possible_brand_association' for c, r in selected),
            'cardboard_comments': 0, 'cardboard_recommendations': 0, 'firsthand_cardboard_accounts': 0,
        })
    assert retained_keys == set(by_key), 'Classification and capture mismatch'
    assert {r['post_id'] for r in posts} == {f'RP{i:02}' for i in range(1, 7)}
    totals = {k: sum(r[k] for r in posts) for k in posts[0] if k not in {'post_id', 'snapshot_utc', 'elapsed_hours', 'distinct_human_accounts'}}
    totals['distinct_human_accounts_across_posts'] = len(all_authors)
    return {'posts': posts, 'inventory_totals_not_market_rates': totals,
            'limitations': ['Public self-reports; eligibility, identity, affiliation and outcomes unverified.',
                           'Badge differences unexplained; counts concern retained visible nodes only.',
                           'Substantive includes relevant sparse tool answers; behavioral detail counted separately.',
                           'Firsthand includes unnamed in-my-experience claims; not verified product use.',
                           'Bots included only in all non-author inventory; excluded human counts.',
                           'Separate task/community cohorts and unequal exposure; no market prevalence or EX01 result.']}

if __name__ == '__main__':
    result = summarize()
    destination = RESEARCH / 'reddit-reply-summary-2026-10-05.json'
    destination.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
