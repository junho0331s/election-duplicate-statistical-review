# 2026 Official Vote-Count Data Availability and Official-Page Extraction Check

Check date: 2026-06-09 KST

## Purpose

This document explains which official 2026 materials were available for the in-district early-vote identical-pair analysis, and which materials are still needed. The key distinction is:

1. At the time this package was prepared, the official integrated Public Data Portal XLSX file for the 9th nationwide local election had not been obtained in the same format as the historical baseline files.
2. The twelve 2026 event-row vote counts were nevertheless rechecked by direct extraction from the National Election Commission election-statistics system's official counting-unit result HTML pages.

## Official Sources Checked

### 1. Public Data Portal: National Election Commission voting/counting information

- URL: https://www.data.go.kr/data/15000900/openapi.do
- Check result: the service description states that voting/counting information is not same-day live progress data; it is normally provided after election-management consultation and data transfer/verification procedures, usually within two months after the election.
- Check result: at the time of review, the nationwide local-election coverage was listed as the 3rd through 8th nationwide local elections.
- Check result: the API is described as a service for querying voting and counting results by election ID, election type code, province/city name, and district/county name.

### 2. Public Data Portal: 8th nationwide local election vote-count result file

- URL: https://www.data.go.kr/data/15101509/fileData.do
- Check result: the 8th nationwide local-election vote-count result is provided as XLSX file data.
- Check result: the file is described as containing vote-count information by province/city, district/county, and eup/myeon/dong.
- Check result: this is the same class of official integrated file used in this package's historical governor-election baseline.

### 3. Public Data Portal search for the 9th nationwide local election

- Search terms checked: Korean-language queries for the National Election Commission 9th nationwide local-election vote-count result and the 9th nationwide local-election vote-count result.
- Check result: at the time of review, the package did not identify an official integrated XLSX file corresponding to the 9th nationwide local-election vote-count result.

### 4. NEC election-statistics system: counting-unit result page

- URL: https://info.nec.go.kr/main/showDocument.xhtml?electionId=0020260603&topMenuId=VC&secondMenuId=VCCP08
- Check result: the current-election menu for the 9th nationwide local election provides counting-unit result pages.
- Check result: `scripts/fetch_nec_2026_duplicate_cases.py` saves the relevant POST-response HTML and parses candidate vote counts from in-district early-vote rows.
- Check result: the parser reproduces twelve event rows and six identical vote pairs.

## Effect on the Paper

The 2026 identical-pair event values began as publicly reported cases, but in the final package they are no longer treated as screenshot-only values. They are rechecked against official NEC election-statistics page values. The original HTML cache is stored under `data/nec_2026_official_html/`, and parsed outputs are stored in:

- `outputs/nec_2026_reported_duplicate_cases.csv`
- `outputs/nec_2026_reported_duplicate_pairs.csv`

However, official page values are not the same evidentiary layer as an integrated XLSX file or original counting statements. When the official integrated vote-count file or original counting statements become available, the same parsing and checking procedure should be applied to confirm:

1. Whether the twelve in-district early-vote values extracted from the official page match the official integrated file and original counting statements.
2. Whether the Gwangju-Jeonnam five-pair set remains a repeated pattern within the same contest, candidate combination, and vote type.
3. Whether the official-file repeated-pair count remains at five or more.
4. Whether the official-file in-district early-vote unit count \(N\) remains inside the sensitivity range used in the paper.

## Recommended Submission Wording

Acceptable wording:

> Based on public data and the reported event definition, the Gwangju-Jeonnam five-pair repetition is a statistical anomaly difficult to reconcile with the historical official-data baseline, and official raw-data disclosure plus independent verification are required.

Stronger wording currently supported by this package:

> Taken together, the NEC election-statistics official page values and the historical official-data baseline indicate that the Gwangju-Jeonnam five-pair repetition is a statistical anomaly difficult to reconcile with the ordinary-randomness hypothesis, and independent verification of original counting statements and first-pass sorter records is required.

Wording to avoid:

> The official integrated 2026 vote-count file has already proven a specific act of misconduct.

That statement exceeds the current evidence. The package's strength is not a final legal attribution. Its strength is that public official-page values, historical official-data baselines, and reproducible probability calculations narrowly and strongly support the need for raw-data audit.
