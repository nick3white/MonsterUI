#!/usr/bin/env python3

from fastcore.utils import *
import api_reference.api_reference as api_reference
def fname2title(ref_fn_name): return ref_fn_name[5:].replace('_',' | ').title() 

def create_llms_txt():    
    # Get examples
    base = "https://monsterui.answer.ai"
    examples = [f for f in Path('examples').glob('*.py') if not f.name.startswith('__') and f.name.endswith('.py')]
    example_links = [f"[{f.stem.title()}]({base}/{f.name[:-3]}/md)" for f in examples]
    reference_fns = L([o for o in dir(api_reference) if o.startswith('docs_')])
    api_links = [f"[{fname2title(f)}]({base}/api_ref/{f}/md)" for f in reference_fns]
    
    # Create content
    content = [
        "# MonsterUI Documentation",
        '''
> MonsterUI is a python library which brings styling to python for FastHTML apps.

'''
        "## API Reference",
        '- [API List](https://raw.githubusercontent.com/AnswerDotAI/MonsterUI/refs/heads/main/docs/apilist.txt)',
        "",
        "## Examples",
        *[f'- {a}' for a in example_links],
        "",
        "## Optional",
        *[f'- {a}' for a in api_links],
        "- [Layout](https://monsterui.answer.ai/tutorial_layout/md)",
        "- [Spacing](https://monsterui.answer.ai/tutorial_spacing/md)",
    ]
    
    # Write to file
    Path('llms.txt').write_text('\n'.join(content))

create_llms_txt()
