#!/usr/bin/env python3
"""独立技能结构、自包含引用与模板完整性验证。"""
import ast
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
EXPECTED={'git-awesome','git-workflow','git-init','git-branch','git-audit','git-commit','git-sync','git-release','git-recovery'}

def validate():
    errors=[]
    dirs={p.name for p in (ROOT/'skills').iterdir() if p.is_dir()}
    if dirs!=EXPECTED:errors.append('九技能目录不一致')
    for name in sorted(EXPECTED):
        root=ROOT/'skills'/name
        file=root/'SKILL.md'
        if not file.is_file():errors.append('缺少 '+name);continue
        value=file.read_text()
        if len(value.splitlines())>=500 or not value.startswith('---\nname: '+name+'\n'):errors.append('frontmatter/行数 '+name)
        for section in ('## 前置条件与授权','## 执行步骤','## 验证与输出','## 正例','## 反例','## 异常处理'):
            if section not in value:errors.append('章节缺失 '+name+section)
        for doc in root.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',doc.read_text()):
                if '://' in target or target.startswith('#'):continue
                resolved=(doc.parent/target.split('#')[0]).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():errors.append('非自包含引用 '+str(doc)+': '+target)
        for script in root.rglob('*.py'):ast.parse(script.read_text())
    sources=json.loads((ROOT/'sources.json').read_text())
    if len(sources['sources'])!=9:errors.append('来源模型数错误')
    for file in (ROOT/'profiles').glob('*.json'):
        p=json.loads(file.read_text())
        for name in ('git-init','git-workflow'):
            if (ROOT/'skills'/name/'references/profiles'/file.name).read_bytes()!=file.read_bytes():errors.append('模板快照漂移')
    return errors

if __name__=='__main__':
    errors=validate()
    print(json.dumps({'decision':'deny' if errors else 'allow','skills':len(EXPECTED),'errors':errors},ensure_ascii=False,indent=2))
    raise SystemExit(bool(errors))
