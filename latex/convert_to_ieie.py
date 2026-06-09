from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'paper_statistical_implausibility_ko.md'
OUT = ROOT / 'latex' / 'ieie' / 'main.tex'

md = SRC.read_text(encoding='utf-8')
lines = md.splitlines()

title = lines[0].lstrip('# ').strip()
abstract = ''
keywords = ''
for i, line in enumerate(lines):
    if line.startswith('## 초록'):
        abstract = lines[i + 2].strip()
        if i + 4 < len(lines) and lines[i + 4].startswith('주요어:'):
            keywords = lines[i + 4].strip()
        break

# The Markdown abstract is intentionally detailed for the repository package.
# The IEIE PDF needs a compact first page; otherwise the abstract spills into
# the right column before Section 1 and looks visually broken.
latex_abstract = (
    '본 논문은 2026년 제9회 전국동시지방선거 관내사전투표에서 관찰된 '
    '동일 득표쌍 반복이 과거 공식 개표자료의 경험적 기준선과 양립하는지 '
    '검토한다. 중앙선거관리위원회 선거통계시스템 공식 화면 HTML에서 '
    '12개 사건행과 6개 동일 득표쌍을 재현했고, 2014년부터 2025년까지 '
    '공개자료 81,701개 개표단위 행을 파싱해 과거 기준선을 구성했다. '
    '2014·2018·2022년 시·도지사 선거 51개 선거구에서 한 선거구 안 '
    '동일 득표쌍의 최대 반복은 3쌍이었으며, 광주전남 5쌍 이상 반복의 '
    '포아송 근사 확률은 약 0.115%로 추정된다. 관찰된 5개 대응쌍을 '
    '지정 대응쌍으로 둘 때 모두 일치할 조건부 확률은 약 '
    '\\(9.54\\times10^{-26}\\)이다. 과거 실제 득표쌍 풀의 비복원 '
    '재표본추출 200,000회에서도 5쌍 이상 반복은 0회였고, '
    '95% 상한은 약 0.0015%였다. 또한 2020년과 2024년 국회의원선거에서는 '
    '분석 가능한 모든 지역구에서 더불어민주당 후보의 '
    '사전투표 양자득표율이 당일투표보다 높았다. 본 연구의 결론은 특정 '
    '부정행위의 법적 확정이 아니라, 공개자료만으로도 우연가설을 약화시키는 '
    '통계적 이상성이 존재하며 독립적 원자료 감사가 필요하다는 것이다.'
)

# Body starts at first numbered section.
start = next(i for i, line in enumerate(lines) if line.startswith('## 1.'))
body_lines = lines[start:]

specials = {
    '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_',
    '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}',
}

def esc_plain(s: str) -> str:
    return ''.join(specials.get(ch, ch) for ch in s)

math_pat = re.compile(r'(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))')

def esc_text(s: str) -> str:
    # Convert markdown inline code before general escaping.
    chunks = []
    pos = 0
    for m in re.finditer(r'`([^`]+)`', s):
        chunks.append(('text', s[pos:m.start()]))
        chunks.append(('code', m.group(1)))
        pos = m.end()
    chunks.append(('text', s[pos:]))
    out = []
    for kind, value in chunks:
        if kind == 'code':
            out.append(r'\texttt{' + esc_plain(value) + '}')
            continue
        parts = math_pat.split(value)
        for part in parts:
            if not part:
                continue
            if part.startswith('\\[') or part.startswith('\\('):
                out.append(part)
            else:
                out.append(esc_plain(part))
    return ''.join(out)

def clean_heading(s: str) -> str:
    s = s.strip()
    s = re.sub(r'^\d+(?:\.\d+)*\.?\s*', '', s)
    return s

out: list[str] = []
open_list: str | None = None
in_display = False
in_onecolumn_appendix = False

def close_list():
    global open_list
    if open_list:
        out.append(r'\end{' + open_list + '}')
        open_list = None

def split_md_table_row(line: str) -> list[str]:
    token = '\x00PIPE\x00'
    protected = line.strip().strip('|').replace('\\|', token)
    return [c.strip().replace(token, '|') for c in protected.split('|')]

def table_to_latex(block: list[str]) -> list[str]:
    rows = []
    for line in block:
        cells = split_md_table_row(line)
        rows.append(cells)
    header = rows[0]
    data = rows[2:]
    wide_table = len(header) >= 4
    if wide_table:
        width = 0.95 / len(header)
        colspec = ''.join(f'p{{{width:.3f}\\linewidth}}' for _ in header)
    elif len(header) == 2:
        if in_onecolumn_appendix:
            colspec = (
                r'>{\raggedright\arraybackslash}p{0.18\linewidth}'
                r'>{\raggedright\arraybackslash}p{0.76\linewidth}'
            )
        else:
            colspec = (
                r'>{\raggedright\arraybackslash}p{0.25\linewidth}'
                r'>{\raggedright\arraybackslash}p{0.63\linewidth}'
            )
    else:
        width = 0.88 / len(header)
        colspec = ''.join(
            rf'>{{\raggedright\arraybackslash}}p{{{width:.3f}\linewidth}}'
            for _ in header
        )
    floating_wide_table = wide_table and not in_onecolumn_appendix
    table_size = r'\small' if in_onecolumn_appendix and len(header) == 2 else r'\scriptsize'
    if wide_table:
        result = [r'\begin{table*}[t]', r'\centering', table_size]
    else:
        result = [r'\begin{center}', table_size]
    if wide_table and in_onecolumn_appendix:
        result = [r'\begin{center}', table_size]
    use_resize = wide_table
    if use_resize:
        result.append(r'\resizebox{\linewidth}{!}{%')
    result.extend([r'\begin{tabular}{' + colspec + '}', r'\toprule'])
    result.append(' & '.join(esc_text(c) for c in header) + r' \\')
    result.append(r'\midrule')
    for row in data:
        row = row + [''] * (len(header) - len(row))
        result.append(' & '.join(esc_text(c) for c in row[:len(header)]) + r' \\')
    result.extend([r'\bottomrule', r'\end{tabular}'])
    if use_resize:
        result.append(r'}')
    if floating_wide_table:
        result.append(r'\end{table*}')
    else:
        result.append(r'\end{center}')
    return result

idx = 0
while idx < len(body_lines):
    line = body_lines[idx]
    stripped = line.strip()

    if not stripped:
        close_list()
        out.append('')
        idx += 1
        continue

    if stripped.startswith('|') and idx + 1 < len(body_lines) and body_lines[idx + 1].strip().startswith('|'):
        close_list()
        block = []
        while idx < len(body_lines) and body_lines[idx].strip().startswith('|'):
            block.append(body_lines[idx])
            idx += 1
        out.extend(table_to_latex(block))
        continue

    if stripped == r'\[':
        close_list()
        in_display = True
        out.append(r'\[')
        idx += 1
        continue
    if stripped == r'\]':
        out.append(r'\]')
        in_display = False
        idx += 1
        continue
    if in_display:
        out.append(line)
        idx += 1
        continue

    if stripped.startswith('## '):
        close_list()
        heading = clean_heading(stripped[3:])
        if heading.startswith('부록 ') or heading == '참고자료':
            if heading.startswith('부록 ') and not in_onecolumn_appendix:
                out.append(r'\clearpage')
                out.append(r'\onecolumn')
                in_onecolumn_appendix = True
            elif in_onecolumn_appendix:
                out.append(r'\vspace{1em}')
        if heading == '연구윤리 및 이해상충':
            out.append(r'\enlargethispage{3\baselineskip}')
        if heading.startswith('부록 ') or heading in {'참고자료', '재현 산출물'}:
            out.append(r'\section*{' + esc_text(heading) + '}')
        else:
            out.append(r'\section{' + esc_text(heading) + '}')
        idx += 1
        continue

    if stripped.startswith('### '):
        close_list()
        out.append(r'\subsection{' + esc_text(clean_heading(stripped[4:])) + '}')
        idx += 1
        continue

    if stripped.startswith('> '):
        close_list()
        out.append(r'\begin{quote}')
        out.append(esc_text(stripped[2:]))
        out.append(r'\end{quote}')
        idx += 1
        continue

    m_num = re.match(r'^(\d+)\.\s+(.*)$', stripped)
    if m_num:
        if open_list != 'enumerate':
            close_list()
            open_list = 'enumerate'
            out.append(r'\begin{enumerate}')
        out.append(r'\item ' + esc_text(m_num.group(2)))
        idx += 1
        continue

    if stripped.startswith('- '):
        if open_list != 'itemize':
            close_list()
            open_list = 'itemize'
            out.append(r'\begin{itemize}')
        out.append(r'\item ' + esc_text(stripped[2:]))
        idx += 1
        continue

    close_list()
    out.append(esc_text(stripped))
    idx += 1
close_list()

tex = r'''
\documentclass[preprint]{IEIE}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{array}
\usepackage{url}

\title{우연가설을 압도하는 관내사전투표\\동일 득표쌍 반복과 원자료 감사 요구}
\author{김준호 \\ 소속 없음 \\ e-mail : junhokim0331@gmail.com}
\engtitle{Repeated Identical Vote Pairs Overwhelming the Chance Hypothesis\\and the Need for Source-Record Audit}
\engauthor{Junho Kim \\ No Affiliation}
\abstract{
''' + esc_text(latex_abstract) + r'''\\[2mm]\noindent ''' + esc_text(keywords) + r'''
}

\begin{document}
\maketitle
\makeabstract

''' + '\n'.join(out) + r'''

\end{document}
'''

OUT.write_text(tex, encoding='utf-8')
print(OUT)
