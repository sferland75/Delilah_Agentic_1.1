from typing import Dict, Any

class DataCollectionAgent:
    def validate_input(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {'valid': True, 'data': data}

    def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return data