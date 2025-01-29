#!/usr/bin/env python3

from fastcore.utils import *
import api_reference.api_reference as api_reference
def fname2title(ref_fn_name): return ref_fn_name[5:].replace('_',' | ').title() 

def create_llms_txt():    
    # Get examples
    base = "https://monsterui.answer.ai"
    examples = [f for f in Path('examples').glob('*.py') if not f.name.startswith('__') and f.name.endswith('.py')]
    example_links = [f"[{f.stem.title()}]({base}/{f.name[:-3]}/md)" for f in examples]
    

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
        *[f'- {a}' for a in example_links]
    ]
    
    # Write to file
    Path('llms.txt').write_text('\n'.join(content))

create_llms_txt()
