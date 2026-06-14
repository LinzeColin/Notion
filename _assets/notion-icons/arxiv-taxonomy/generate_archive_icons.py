#!/usr/bin/env python3
"""Generate purple-white arXiv archive icons from the exported Notion manifest."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "archive-icon-manifest-20260614.json"
OUT_DIR = ROOT / "archives"
DATE = "20260614"


def esc(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def suffix(code: str) -> str:
    return code.split(" - ", 1)[1]


def slug_for(code: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", code.lower()).strip("-")


def hash_int(code: str, idx: int) -> int:
    digest = hashlib.sha256(f"{code}:{idx}".encode()).hexdigest()
    return int(digest[:8], 16)


def hash_point(code: str, idx: int, x0: int, x1: int, y0: int, y1: int) -> tuple[int, int]:
    h = hash_int(code, idx)
    return x0 + h % (x1 - x0 + 1), y0 + (h >> 9) % (y1 - y0 + 1)


def code_label(code: str) -> str:
    group, leaf = code.split(" - ", 1)
    group = group.replace("Q-FIN", "QF").replace("Q-BIO", "QB")
    return leaf if len(leaf) <= 8 else leaf[:8]


def common_card(inner: str, code: str, archive: str, motif: str) -> str:
    c1 = "#c084fc"
    c2 = "#5b21b6"
    c3 = "#8b5cf6"
    c4 = "#d8b4fe"
    p1 = hash_point(code, 1, 34, 70, 182, 220)
    p2 = hash_point(code, 2, 184, 220, 34, 74)
    label = esc(code_label(code))
    aria = esc(f"{archive} {code} purple white icon")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="{aria}">
  <defs>
    <linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff"/><stop offset="1" stop-color="#eadcff"/></linearGradient>
    <linearGradient id="p" x1="44" y1="42" x2="214" y2="218"><stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
    <filter id="s"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#4c1d95" flood-opacity=".20"/></filter>
  </defs>
  <rect width="256" height="256" rx="56" fill="url(#b)"/>
  <circle cx="{p1[0]}" cy="{p1[1]}" r="28" fill="{c4}" opacity=".30"/>
  <circle cx="{p2[0]}" cy="{p2[1]}" r="24" fill="#fff" opacity=".72"/>
  <g filter="url(#s)">
    <rect x="42" y="42" width="172" height="172" rx="40" fill="#fff"/>
    {inner}
    <rect x="80" y="180" width="96" height="26" rx="13" fill="#f5efff" stroke="#e9d5ff" stroke-width="2"/>
    <text x="128" y="198" text-anchor="middle" font-family="Avenir Next, Montserrat, Arial, sans-serif" font-size="13" font-weight="800" fill="{c2}">{label}</text>
  </g>
  <path d="M58 62h22M62 58v22" stroke="{c4}" stroke-width="7" stroke-linecap="round" opacity=".85"/>
  <circle cx="198" cy="196" r="7" fill="{c3}" opacity=".58"/>
</svg>
"""


def m_neural(code: str) -> str:
    pts = [(82, 106), (117, 82), (150, 106), (112, 137), (166, 145), (88, 150)]
    lines = [(0, 1), (1, 2), (0, 3), (2, 3), (3, 4), (3, 5), (5, 0), (4, 2)]
    return "".join(f'<path d="M{pts[a][0]} {pts[a][1]}L{pts[b][0]} {pts[b][1]}" stroke="#a78bfa" stroke-width="7" stroke-linecap="round" opacity=".72"/>' for a, b in lines) + "".join(
        f'<circle cx="{x}" cy="{y}" r="{10 + (hash_int(code, i) % 4)}" fill="url(#p)"/>'
        for i, (x, y) in enumerate(pts)
    )


def m_chip(code: str) -> str:
    pins = "".join(f'<path d="M{66+i*18} 65v18M{66+i*18} 157v18M65 {72+i*18}h18M173 {72+i*18}h18" stroke="#c084fc" stroke-width="7" stroke-linecap="round"/>' for i in range(5))
    return f'{pins}<rect x="78" y="78" width="100" height="92" rx="22" fill="#f7f0ff" stroke="url(#p)" stroke-width="10"/><path d="M103 112h50M103 136h32" stroke="#5b21b6" stroke-width="9" stroke-linecap="round"/><circle cx="152" cy="136" r="8" fill="#8b5cf6"/>'


def m_graph(code: str) -> str:
    pts = [(78, 148), (96, 91), (132, 118), (163, 82), (178, 151)]
    return '<path d="M76 160h110" stroke="#e9d5ff" stroke-width="10" stroke-linecap="round"/>' + "".join(
        f'<path d="M{pts[i][0]} {pts[i][1]}L{pts[i+1][0]} {pts[i+1][1]}" stroke="url(#p)" stroke-width="9" stroke-linecap="round"/>'
        for i in range(len(pts) - 1)
    ) + "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="#5b21b6"/>' for x, y in pts)


def m_curve(code: str) -> str:
    return '<path d="M74 158C104 98 140 96 181 73" fill="none" stroke="url(#p)" stroke-width="12" stroke-linecap="round"/><path d="M74 82c33 40 64 70 111 83" fill="none" stroke="#c084fc" stroke-width="10" stroke-linecap="round"/><circle cx="128" cy="121" r="12" fill="#5b21b6"/><path d="M72 166h118M73 68v100" stroke="#e9d5ff" stroke-width="8" stroke-linecap="round"/>'


def m_geometry(code: str) -> str:
    return '<path d="M78 156L128 73l54 83z" fill="#f7f0ff" stroke="url(#p)" stroke-width="10" stroke-linejoin="round"/><circle cx="128" cy="120" r="29" fill="none" stroke="#a78bfa" stroke-width="8"/><path d="M80 156h103M128 73v83" stroke="#5b21b6" stroke-width="7" stroke-linecap="round" opacity=".72"/>'


def m_language(code: str) -> str:
    return '<rect x="70" y="72" width="116" height="88" rx="24" fill="#f7f0ff" stroke="url(#p)" stroke-width="9"/><path d="M98 161l-18 24 38-20" fill="#f7f0ff" stroke="#8b5cf6" stroke-width="8" stroke-linejoin="round"/><path d="M96 101h65M96 124h45" stroke="#5b21b6" stroke-width="9" stroke-linecap="round"/>'


def m_shield(code: str) -> str:
    return '<path d="M128 66l55 20v39c0 36-23 58-55 72-32-14-55-36-55-72V86z" fill="#f7f0ff" stroke="url(#p)" stroke-width="10" stroke-linejoin="round"/><rect x="104" y="119" width="49" height="38" rx="10" fill="#5b21b6"/><path d="M111 119v-12c0-21 35-21 35 0v12" fill="none" stroke="#8b5cf6" stroke-width="9" stroke-linecap="round"/>'


def m_eye(code: str) -> str:
    return '<path d="M67 128c22-35 100-35 122 0-22 35-100 35-122 0z" fill="#f7f0ff" stroke="url(#p)" stroke-width="10" stroke-linejoin="round"/><circle cx="128" cy="128" r="27" fill="#8b5cf6"/><circle cx="128" cy="128" r="12" fill="#fff"/><path d="M82 83l20 18M174 83l-20 18" stroke="#c084fc" stroke-width="8" stroke-linecap="round"/>'


def m_database(code: str) -> str:
    return '<ellipse cx="128" cy="81" rx="54" ry="20" fill="#f7f0ff" stroke="url(#p)" stroke-width="9"/><path d="M74 82v76c0 12 24 22 54 22s54-10 54-22V82" fill="#f7f0ff" stroke="url(#p)" stroke-width="9"/><path d="M74 121c0 12 24 22 54 22s54-10 54-22" fill="none" stroke="#8b5cf6" stroke-width="8"/><path d="M74 150c0 12 24 22 54 22s54-10 54-22" fill="none" stroke="#c084fc" stroke-width="7"/>'


def m_cluster(code: str) -> str:
    pts = [(82, 91), (128, 78), (174, 92), (93, 151), (163, 154), (128, 126)]
    return "".join(f'<path d="M128 126L{x} {y}" stroke="#c084fc" stroke-width="8" stroke-linecap="round"/>' for x, y in pts[:-1]) + "".join(f'<rect x="{x-15}" y="{y-15}" width="30" height="30" rx="9" fill="url(#p)"/>' for x, y in pts)


def m_book(code: str) -> str:
    return '<path d="M72 78h51c14 0 25 11 25 25v73H96c-14 0-24-10-24-24z" fill="#f7f0ff" stroke="url(#p)" stroke-width="9"/><path d="M148 103c0-14 11-25 25-25h11v98h-36z" fill="#f7f0ff" stroke="#8b5cf6" stroke-width="9"/><path d="M96 105h31M96 129h25M166 106h14" stroke="#5b21b6" stroke-width="7" stroke-linecap="round"/>'


def m_wave(code: str) -> str:
    return '<path d="M65 128h20l12-39 24 78 24-78 12 39h34" fill="none" stroke="url(#p)" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path d="M76 88c32-20 72-20 104 0M76 168c32 20 72 20 104 0" stroke="#c084fc" stroke-width="7" stroke-linecap="round" opacity=".75"/>'


def m_orbit(code: str) -> str:
    return '<ellipse cx="128" cy="123" rx="68" ry="25" fill="none" stroke="url(#p)" stroke-width="9"/><ellipse cx="128" cy="123" rx="68" ry="25" fill="none" stroke="#8b5cf6" stroke-width="9" transform="rotate(60 128 123)" opacity=".85"/><ellipse cx="128" cy="123" rx="68" ry="25" fill="none" stroke="#c084fc" stroke-width="9" transform="rotate(-60 128 123)" opacity=".75"/><circle cx="128" cy="123" r="17" fill="#5b21b6"/><circle cx="187" cy="123" r="7" fill="#c084fc"/>'


def m_star(code: str) -> str:
    return '<path d="M128 66l13 38 40-1-32 24 13 38-34-23-34 23 13-38-32-24 40 1z" fill="#f7f0ff" stroke="url(#p)" stroke-width="9" stroke-linejoin="round"/><circle cx="82" cy="154" r="8" fill="#c084fc"/><circle cx="183" cy="79" r="7" fill="#5b21b6"/><path d="M82 97c45-35 75 55 118 18" fill="none" stroke="#a78bfa" stroke-width="7" stroke-linecap="round"/>'


def m_equation(code: str) -> str:
    return '<path d="M77 92h104M77 128h104M77 164h104" stroke="#e9d5ff" stroke-width="10" stroke-linecap="round"/><text x="91" y="119" font-family="Georgia, serif" font-size="50" font-weight="700" fill="#5b21b6">∑</text><text x="133" y="151" font-family="Georgia, serif" font-size="42" font-weight="700" fill="#8b5cf6">∂</text>'


def m_lens(code: str) -> str:
    return '<circle cx="119" cy="117" r="48" fill="#f7f0ff" stroke="url(#p)" stroke-width="10"/><path d="M153 151l32 32" stroke="#5b21b6" stroke-width="13" stroke-linecap="round"/><path d="M91 117h56M119 89v56" stroke="#c084fc" stroke-width="8" stroke-linecap="round"/><path d="M72 72l24 17M169 72l-24 17" stroke="#8b5cf6" stroke-width="7" stroke-linecap="round"/>'


def m_gear(code: str) -> str:
    return '<circle cx="128" cy="126" r="48" fill="#f7f0ff" stroke="url(#p)" stroke-width="10"/><circle cx="128" cy="126" r="17" fill="#5b21b6"/><path d="M128 62v24M128 166v24M64 126h24M168 126h24M83 81l17 17M156 154l17 17M173 81l-17 17M100 154l-17 17" stroke="#c084fc" stroke-width="9" stroke-linecap="round"/>'


def m_robot(code: str) -> str:
    return '<rect x="82" y="79" width="92" height="78" rx="24" fill="#f7f0ff" stroke="url(#p)" stroke-width="10"/><circle cx="109" cy="117" r="8" fill="#5b21b6"/><circle cx="147" cy="117" r="8" fill="#5b21b6"/><path d="M105 144h46M128 79V61M92 172l-20 21M164 172l20 21" stroke="#8b5cf6" stroke-width="9" stroke-linecap="round"/>'


def m_dna(code: str) -> str:
    bars = "".join(f'<path d="M101 {82+i*18}h54" stroke="#d8b4fe" stroke-width="7" stroke-linecap="round"/>' for i in range(5))
    return f'{bars}<path d="M98 70c55 22 55 73 0 103M158 70c-55 22-55 73 0 103" fill="none" stroke="url(#p)" stroke-width="10" stroke-linecap="round"/>'


def m_cell(code: str) -> str:
    return '<circle cx="128" cy="125" r="58" fill="#f7f0ff" stroke="url(#p)" stroke-width="10"/><circle cx="124" cy="126" r="24" fill="#8b5cf6" opacity=".9"/><circle cx="160" cy="96" r="9" fill="#c084fc"/><circle cx="91" cy="139" r="8" fill="#c084fc"/><path d="M83 105c22-34 73-37 93 0" stroke="#d8b4fe" stroke-width="7" stroke-linecap="round" fill="none"/>'


def m_neuron(code: str) -> str:
    pts = [(126, 122), (85, 83), (178, 84), (80, 162), (179, 162), (128, 70)]
    return "".join(f'<path d="M126 122L{x} {y}" stroke="#a78bfa" stroke-width="8" stroke-linecap="round"/>' for x, y in pts[1:]) + '<circle cx="126" cy="122" r="25" fill="url(#p)"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="#5b21b6"/>' for x, y in pts[1:])


def m_orderbook(code: str) -> str:
    return '<rect x="70" y="71" width="116" height="101" rx="24" fill="#f7f0ff" stroke="url(#p)" stroke-width="9"/><path d="M91 99h37M91 122h55M91 145h75" stroke="#5b21b6" stroke-width="8" stroke-linecap="round"/><path d="M159 95l18 18-18 18M97 153l-18-18 18-18" fill="none" stroke="#c084fc" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'


def m_portfolio(code: str) -> str:
    return '<path d="M128 73a55 55 0 1 1-49 80h49z" fill="#f7f0ff" stroke="url(#p)" stroke-width="10"/><path d="M128 73v80h49a55 55 0 0 0-49-80z" fill="#c084fc" opacity=".75"/><path d="M128 153l39 38" stroke="#5b21b6" stroke-width="8" stroke-linecap="round"/>'


def m_microscope(code: str) -> str:
    return '<path d="M112 75l42 28-19 29-42-28z" fill="#f7f0ff" stroke="url(#p)" stroke-width="9" stroke-linejoin="round"/><path d="M132 131c-5 30-28 46-54 45M92 176h88M128 176v-28M151 101l20-28" stroke="#5b21b6" stroke-width="10" stroke-linecap="round"/><circle cx="86" cy="176" r="10" fill="#c084fc"/>'


def m_tag(code: str) -> str:
    return '<path d="M75 84h69l42 42-69 69-42-42z" fill="#f7f0ff" stroke="url(#p)" stroke-width="10" stroke-linejoin="round"/><circle cx="104" cy="113" r="10" fill="#5b21b6"/><path d="M118 143h42M118 164h22" stroke="#8b5cf6" stroke-width="8" stroke-linecap="round"/>'


def m_flow(code: str) -> str:
    return '<rect x="80" y="70" width="96" height="34" rx="13" fill="#f7f0ff" stroke="url(#p)" stroke-width="8"/><rect x="70" y="134" width="48" height="38" rx="13" fill="#8b5cf6"/><rect x="138" y="134" width="48" height="38" rx="13" fill="#5b21b6"/><path d="M128 104v22M128 126H94v8M128 126h34v8" stroke="#c084fc" stroke-width="8" stroke-linecap="round"/>'


def m_cube(code: str) -> str:
    return '<path d="M128 68l54 31v61l-54 32-54-32V99z" fill="#f7f0ff" stroke="url(#p)" stroke-width="9" stroke-linejoin="round"/><path d="M74 99l54 31 54-31M128 130v62" fill="none" stroke="#5b21b6" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'


def m_cursor(code: str) -> str:
    return '<rect x="68" y="72" width="120" height="86" rx="22" fill="#f7f0ff" stroke="url(#p)" stroke-width="9"/><path d="M102 102l56 26-28 9 15 30-18 9-15-31-22 21z" fill="#5b21b6"/><path d="M88 92h80" stroke="#c084fc" stroke-width="7" stroke-linecap="round"/>'


MOTIFS = {
    "neural": m_neural,
    "chip": m_chip,
    "graph": m_graph,
    "curve": m_curve,
    "geometry": m_geometry,
    "language": m_language,
    "shield": m_shield,
    "eye": m_eye,
    "database": m_database,
    "cluster": m_cluster,
    "book": m_book,
    "wave": m_wave,
    "orbit": m_orbit,
    "star": m_star,
    "equation": m_equation,
    "lens": m_lens,
    "gear": m_gear,
    "robot": m_robot,
    "dna": m_dna,
    "cell": m_cell,
    "neuron": m_neuron,
    "orderbook": m_orderbook,
    "portfolio": m_portfolio,
    "microscope": m_microscope,
    "tag": m_tag,
    "flow": m_flow,
    "cube": m_cube,
    "cursor": m_cursor,
}


CODE_MOTIFS = {
    "CS - AI": "neural", "CS - AR": "chip", "CS - CC": "graph", "CS - CE": "curve",
    "CS - CG": "geometry", "CS - CL": "language", "CS - CR": "shield", "CS - CV": "eye",
    "CS - CY": "cluster", "CS - DB": "database", "CS - DC": "cluster", "CS - DL": "book",
    "CS - DM": "geometry", "CS - DS": "flow", "CS - ET": "star", "CS - FL": "flow",
    "CS - GL": "document", "CS - GR": "cube", "CS - GT": "graph", "CS - HC": "cursor",
    "CS - IR": "lens", "CS - IT": "wave", "CS - LG": "neural", "CS - LO": "equation",
    "CS - MA": "cluster", "CS - MM": "eye", "CS - MS": "equation", "CS - NA": "gear",
    "CS - NE": "neuron", "CS - NI": "cluster", "CS - OH": "book", "CS - OS": "chip",
    "CS - PF": "gear", "CS - PL": "language", "CS - RO": "robot", "CS - SC": "equation",
    "CS - SD": "wave", "CS - SE": "flow", "CS - SI": "cluster", "CS - SY": "curve",
    "ECON - EM": "curve", "ECON - GN": "curve", "ECON - TH": "graph",
    "EESS - AS": "wave", "EESS - IV": "eye", "EESS - SP": "wave", "EESS - SY": "curve",
    "Q-BIO - BM": "cell", "Q-BIO - CB": "cell", "Q-BIO - GN": "dna", "Q-BIO - MN": "cluster",
    "Q-BIO - NC": "neuron", "Q-BIO - OT": "microscope", "Q-BIO - PE": "graph",
    "Q-BIO - QM": "equation", "Q-BIO - SC": "cell", "Q-BIO - TO": "microscope",
    "Q-FIN - CP": "gear", "Q-FIN - EC": "curve", "Q-FIN - GN": "curve", "Q-FIN - MF": "equation",
    "Q-FIN - PM": "portfolio", "Q-FIN - PR": "tag", "Q-FIN - RM": "shield",
    "Q-FIN - ST": "graph", "Q-FIN - TR": "orderbook",
    "STAT - AP": "curve", "STAT - CO": "gear", "STAT - ME": "equation",
    "STAT - ML": "neural", "STAT - OT": "book", "STAT - TH": "equation",
}


MATH_DEFAULTS = {
    "AC": "equation", "AG": "geometry", "AP": "wave", "AT": "geometry", "CA": "wave",
    "CO": "graph", "CT": "cluster", "CV": "geometry", "DG": "geometry", "DS": "curve",
    "FA": "equation", "GM": "book", "GN": "geometry", "GR": "graph", "GT": "geometry",
    "HO": "book", "IT": "wave", "KT": "geometry", "LO": "equation", "MG": "geometry",
    "MP": "orbit", "NA": "gear", "NT": "equation", "OA": "equation", "OC": "curve",
    "PR": "curve", "QA": "orbit", "RA": "equation", "RT": "geometry", "SG": "geometry",
    "SP": "wave", "ST": "equation",
}


PHYS_DEFAULTS = {
    "acc-ph": "gear", "AO": "curve", "ao-ph": "wave", "app-ph": "gear", "atm-clus": "orbit",
    "atom-ph": "orbit", "bio-ph": "cell", "CD": "curve", "CG": "geometry", "chem-ph": "cell",
    "class-ph": "curve", "CO": "star", "comp-ph": "gear", "data-an": "curve", "dis-nn": "neuron",
    "ed-ph": "book", "EP": "star", "flu-dyn": "wave", "GA": "star", "gen-ph": "orbit",
    "geo-ph": "star", "gr-qc": "geometry", "HE": "star", "hep-ex": "lens", "hep-lat": "geometry",
    "hep-ph": "graph", "hep-th": "equation", "hist-ph": "book", "IM": "lens", "ins-det": "lens",
    "math-ph": "equation", "med-ph": "microscope", "mes-hall": "chip", "mtrl-sci": "chip",
    "nucl-ex": "orbit", "nucl-th": "equation", "optics": "lens", "other": "book",
    "plasm-ph": "wave", "pop-ph": "star", "PS": "wave", "quant-gas": "orbit",
    "quant-ph": "orbit", "SI": "equation", "soc-ph": "cluster", "soft": "cell",
    "space-ph": "star", "SR": "star", "stat-mech": "curve", "str-el": "chip", "supr-con": "wave",
}


def choose_motif(row: dict[str, str]) -> str:
    code = row["code"]
    if code in CODE_MOTIFS:
        return CODE_MOTIFS[code]
    group, leaf = code.split(" - ", 1)
    if group == "MATH":
        return MATH_DEFAULTS.get(leaf, "equation")
    if group == "PHYS":
        return PHYS_DEFAULTS.get(leaf, "orbit")
    return "graph"


def icon_for(row: dict[str, str]) -> str:
    code = row["code"]
    archive = row["archive"]
    motif = choose_motif(row)
    inner = MOTIFS.get(motif, m_graph)(code)
    if motif == "document":
        inner = m_book(code)
    return common_card(inner, code, archive, motif)


def main() -> None:
    rows = json.loads(MANIFEST.read_text())
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    seen = set()
    for row in rows:
        code = row["code"]
        if code in seen:
            raise SystemExit(f"Duplicate code: {code}")
        seen.add(code)
        path = OUT_DIR / f"pw-{slug_for(code)}-{DATE}.svg"
        path.write_text(icon_for(row), encoding="utf-8")
    print(json.dumps({"generated": len(rows), "dir": str(OUT_DIR)}, indent=2))


if __name__ == "__main__":
    main()
