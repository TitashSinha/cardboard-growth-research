# Public discovery accessibility

Observed 2026-10-02. Scope: sampled public pages and sitemap, not GSC or server logs.

| Signal | Observation | Implication / limitation |
|---|---|---|
| robots.txt (E009) | Wildcard allow and sitemap declaration | No explicit OAI-SearchBot block in this file; WAF/IP access remains unknown |
| Sitemap (E008) | 22 listed URLs, including 8 blog articles | Discoverable inventory, not an index count |
| Sample metadata (E010) | Accessible HTML, canonical and index/follow signals on reviewed pages | No broad crawl exclusion established; no assurance of indexing |
| Redirects (E010) | HTTP and bare-domain homepage requests resolve to HTTPS www | Canonical domain behavior observed; full redirect chains not retained |
| Legacy demo (E017) | demo.usecardboard.com resolves to current homepage | Historical hands-on-demo link no longer reaches a distinct demo in this observation |
| Blog navigation (E023) | Same eight article routes found in blog links and sitemap | No dedicated SaaS launch workflow page found in inspected inventory; avoid claiming sitewide absence |
| Headings | Homepage/desktop include headings inside product mockups | Low-priority semantics review; not a demonstrated ranking blocker |
| llms.txt | Public file accessible and linked from robots comment | Existing; no reason to prioritize adding one |
| Mobile | Pending narrow visual check | No Core Web Vitals or field-performance claim |

## Recommendations with failure checks

1. **Refresh offer claims in the three checked articles.** Before asking for more traffic, make the route from article to pricing consistent. Owner: company content/product team. Verify with the same price/trial checklist after changes. Failure: buyers still cannot explain web vs Mac access in a comprehension test.
2. **Create one focused workflow proof page if coverage review confirms it adds value.** Preserve useful current examples; link related articles to the sample and then the correct platform route. Failure: target buyers prefer existing workflow or cannot identify a credible advantage.
3. **Keep public pages crawlable and readable.** Validate OAI-SearchBot against actual logs/WAF later. Google recommends standard SEO and useful content; OpenAI separates search crawling from training (E015–E016). Do not promise inclusion or change training permissions as a prerequisite for search.

No invented SEO health score, mandatory passage length, FAQ rich-result promise, or llms.txt citation trick. The imported GEO checklist mislabels GPTBot's purpose; the current official documentation takes precedence. Proposed Article/Organization markup should reflect visible content and pass the relevant validators if company implementation proceeds.
