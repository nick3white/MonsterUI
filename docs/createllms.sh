#!/usr/bin/env python3

from fastcore.utils import *
import api_reference.api_reference as api_reference
def fname2title(ref_fn_name): return ref_fn_name[5:].replace('_',' | ').title() 

def create_llms_txt():
    # Get API reference sections
    base = 'https://monsterui.answer.ai'
    fns = L([o for o in dir(api_reference) if o.startswith('docs_')])
    urls = [f"{base}/api_ref/{r}/md" for r in fns]
    api_refs = [f"[{fname2title(r)}]({u})" for r,u in zip(fns, urls)]
    
    # Get examples
    base = "https://monsterui.answer.ai"
    examples = [f for f in Path('examples').glob('*.py') if not f.name.startswith('__') and f.name.endswith('.py')]
    example_links = [f"[{f.stem.title()}]({base}/{f.name[:-3]}/md)" for f in examples]
    
    # Create content
    content = [
        "# MonsterUI Documentation",
        '''

> MonsterUI is a python library which brings styling to python for FastHTML apps.

Things to remembers when using MonsterUI:
- While Pico CSS is commonly used in FastHTML apps, that is *completely incompatible* with MonsterUI. 
- MonsterUI is *not* compatible with FastAPI syntax and is not targeted at creating API services.

'''
        "## API Reference",
        *[f'- {a}' for a in api_refs],
        "",
        "## Optional",
        *[f'- {a}' for a in example_links]
    ]
    
    # Write to file
    Path('../docs/llms.txt').write_text('\n'.join(content))
    return urls, examples

urls, examples = create_llms_txt()
