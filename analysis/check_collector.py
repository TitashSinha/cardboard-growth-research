"""Focused offline collector checks. Run: python analysis/check_collector.py."""
import contextlib
import io
import json
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import collect_public as collector


def main():
    page=collector.Page()
    page.feed('<html><head><title>Page title</title></head><body>'
              '<svg><title>Icon title</title></svg>'
              '<h1><span>M</span><span>a</span><span>k</span><span>e</span> '
              '<em>a video</em></h1><h1>Second <span>heading</span></h1></body></html>')
    assert ''.join(page.title)=='Page title', page.title
    assert page.h1==['Make a video', 'Second heading'], page.h1

    with TemporaryDirectory(prefix='cardboard-collector-check-') as temporary:
        root=Path(temporary)
        def fake_get(url):
            return {'requested_url':url, 'status':200}
        with patch.object(collector, 'ROOT', root), patch.object(collector, 'get', side_effect=fake_get) as get:
            explicit=root/'explicit'/'capture.json'
            with contextlib.redirect_stdout(io.StringIO()):
                assert collector.main(['--output', str(explicit)])==0
                assert collector.main([])==0
            assert len(json.loads(explicit.read_text(encoding='utf-8')))==11
            defaults=list((root/'research'/'captures').glob('*.json'))
            assert len(defaults)==1, defaults
            assert re.fullmatch(r'public-metadata-\d{8}T\d{6}\.\d{6}Z\.json', defaults[0].name)
            assert len(json.loads(defaults[0].read_text(encoding='utf-8')))==11
            original=explicit.read_bytes()
            calls=get.call_count
            error=io.StringIO()
            with contextlib.redirect_stderr(error):
                try:
                    collector.main(['--output', str(explicit)])
                    raise AssertionError('Existing path was accepted')
                except SystemExit as exc:
                    assert exc.code==2, exc.code
            assert 'Refusing to overwrite existing capture' in error.getvalue()
            assert get.call_count==calls, 'Overwrite rejection must precede network requests'
            try:
                collector.save_capture([], explicit)
                raise AssertionError('Exclusive creation failed')
            except FileExistsError:
                pass
            assert explicit.read_bytes()==original
    print('PASS: head title excludes SVG; nested H1; explicit/default output; overwrite refusal before capture and at save. No network used.')


if __name__=='__main__':
    main()
