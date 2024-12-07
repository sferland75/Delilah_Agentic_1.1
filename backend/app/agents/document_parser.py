from typing import Dict, Any

class DocumentParserAgent:
    def parse_document(self, content: bytes) -> Dict[str, Any]:
        return {'parsed': True, 'content': str(content)}

    def extract_data(self, parsed_content: Dict[str, Any]) -> Dict[str, Any]:
        return parsed_content