"""Helm template file parser for extracting variables"""
import os
import re
from config import TEMPLATES_SUBDIR


class HelmTemplateParser:
    def __init__(self):
        self.pattern = re.compile(r'\{\{\s*\.Values\.([a-zA-Z0-9_]+)')
    
    def list_template_files(self):
        """List all template files in the templates directory"""
        files = [f for f in os.listdir(TEMPLATES_SUBDIR) if f.endswith(('.yaml', '.tpl'))]
        print(f'📁 Found {len(files)} template files:')
        for file in files:
            print(f'   - {file}')
        print("\n" + "="*50)
        return files
    
    def extract_variables(self, files):
        """Extract Helm variables from template files"""
        variables = set()
        print("🔍 Scanning template files for variables...")
        for fname in files:
            file_path = os.path.join(TEMPLATES_SUBDIR, fname)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    found = self.pattern.findall(content)
                    if found:
                        print(f'   📄 {fname}: {found}')
                    variables.update(found)
            except Exception as e:
                print(f'   ❌ Error reading {fname}: {e}')
        print(f'\n✅ Total unique variables found: {len(variables)}')
        print(f'📋 Variables needed: {sorted(list(variables))}')
        return variables
