#!/usr/bin/env python3
"""Standalone AMRKB diagram renderer: canonical annotated Mermaid subset.

Adapted from the existing BIPKB nested renderer and OSDS/EIRKB conventions.
Python standard library only. No neighbouring checkout, private evidence or network.
"""
import argparse
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

def nested_diagram(source):
    """Render the canonical annotated Mermaid group/text subset, without an engine dependency.

    Palette, text metrics and layout come from the source, as in OSDS/EIRKB.
    This branch leaves the earlier conceptual-map rendering byte-identical.
    """
    import xml.etree.ElementTree as ET
    text = source.read_text(encoding='utf-8')
    width, height = map(int, re.search(r'^%% @canvas (\d+) (\d+)$', text, re.M).groups())
    title = re.search(r'^%% @title (.+)$', text, re.M)[1]
    description = re.search(r'^%% @description (.+)$', text, re.M)[1]
    labels = dict(re.findall(r'^\s*(?:subgraph\s+)?(\w+)\["([^"\n]+)"\]', text, re.M))
    hints = re.findall(r'^%% @(box|group) (\w+) (\d+) (\d+) (\d+) (\d+) (\w+)$', text, re.M)
    boxes = {n: tuple(map(int, (x, y, w, h))) for _, n, x, y, w, h, _ in hints}
    styles = {n: dict(item.split(':', 1) for item in values.split(','))
              for n, values in re.findall(r'^\s*classDef (\w+) ([^\n;]+);', text, re.M)}
    if set(boxes) != set(labels) or len(boxes) != len(hints):
        raise ValueError('Every unique label needs exactly one layout hint')
    # Validate actual Mermaid nesting against the supplied layout, not just drawn rectangles.
    stack = []
    for line in text.splitlines():
        group = re.match(r'^\s*subgraph (\w+)\[', line)
        node = re.match(r'^\s*(\w+)\[', line)
        name = group[1] if group else node[1] if node else None
        if name and stack:
            x, y, w, h = boxes[name]; px, py, pw, ph = boxes[stack[-1]]
            if not (px <= x and py <= y and x+w <= px+pw and y+h <= py+ph):
                raise ValueError('Nested item outside parent: '+name)
        if group: stack.append(name)
        elif line.strip() == 'end':
            if not stack: raise ValueError('Unmatched Mermaid end')
            stack.pop()
    if stack: raise ValueError('Unclosed Mermaid subgraph')
    esc = html.escape
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
           f'<title id="title">{esc(title)}</title><desc id="desc">{esc(description)}</desc>',
           '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#637286"/></marker></defs>',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           '<g font-family="Arial, Helvetica, sans-serif" text-anchor="middle">']
    for a, relationship, b in re.findall(r'^\s*(\w+) (<-->|-->) (\w+)\s*$', text, re.M):
        ax, ay, aw, ah = boxes[a]; bx, by, bw, bh = boxes[b]
        if by <= ay+ah: raise ValueError('Layer connectors must run downward')
        start = ' marker-start="url(#arrow)"' if relationship == '<-->' else ''
        out.append(f'<path d="M{ax+aw/2:g} {ay+ah+4} L{bx+bw/2:g} {by-5}" fill="none" stroke="#637286" stroke-width="1.6" marker-end="url(#arrow)"{start}/>')
    for kind, name, _, _, _, _, role in hints:
        x, y, w, h = boxes[name]; style = styles[role]
        if not (0 <= x < x+w <= width and 0 <= y < y+h <= height): raise ValueError('Outside canvas: '+name)
        dash = ' stroke-dasharray="6 4"' if name == 'DRM' else ''
        out.append(f'<rect id="box-{name}" x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-width="{style.get("stroke-width", "1.5")}"{dash}/>')
        hint = re.search(r'^%% @text '+name+r' ([\d.,]+) ([\d.,]+) ([\d,]+)$', text, re.M)
        if not hint: raise ValueError('Missing typography: '+name)
        sizes, offsets, weights = [list(map(float, values.split(','))) for values in hint.groups()]
        lines = labels[name].split('<br/>')
        if not len(lines) == len(sizes) == len(offsets) == len(weights): raise ValueError('Typography count: '+name)
        for line, size, offset, weight in zip(lines, sizes, offsets, weights):
            if not (offset-size*.8 > 0 and offset+size*.25 < h): raise ValueError('Vertical text bounds: '+name)
            out.append(f'<text data-box="{name}" x="{x+w/2:g}" y="{y+offset:g}" font-size="{size:g}" font-weight="{weight:g}" fill="{style["color"]}">{esc(line)}</text>')
    out.append('</g></svg>')
    svg = '\n'.join(out)+'\n'
    ET.fromstring(svg)
    return svg


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Compare without writing')
    parser.add_argument('--output', type=Path, help='Optional development render destination')
    args = parser.parse_args()
    source = HERE / 'amrkb_overview.mmd'
    target = args.output or source.with_suffix('.svg')
    svg = nested_diagram(source).encode('utf-8')
    if args.check:
        if not target.is_file() or target.read_bytes() != svg:
            raise SystemExit('AMRKB diagram output differs from source')
        print('PASS: AMRKB deterministic diagram parity.')
    else:
        target.write_bytes(svg)
        print('Rendered ' + str(target))

if __name__ == '__main__':
    main()
