from typing import Dict, Any

class TemplateMapperAgent:
    def generate_report(self, data: Dict[str, Any], template_id: str) -> str:
        return f'Report generated from template {template_id}'