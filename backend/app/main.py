from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import json

from agents.data_collection import DataCollectionAgent
from agents.document_parser import DocumentParserAgent
from agents.template_mapper import TemplateMapperAgent

app = FastAPI(title="Delilah Agentic API")

# Initialize agents
data_agent = DataCollectionAgent()
doc_agent = DocumentParserAgent()
template_agent = TemplateMapperAgent()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Delilah Agentic API"}

@app.post("/process-form")
async def process_form(data: Dict[str, Any]):
    # Validate and process form data
    validated = data_agent.validate_input(data)
    if not validated['valid']:
        raise HTTPException(status_code=400, detail="Invalid input data")
    
    processed = data_agent.process_data(validated['data'])
    return processed

@app.post("/parse-document")
async def parse_document(file: UploadFile = File(...)):
    content = await file.read()
    parsed = doc_agent.parse_document(content)
    extracted = doc_agent.extract_data(parsed)
    return extracted

@app.post("/generate-report/{template_id}")
async def generate_report(template_id: str, data: Dict[str, Any]):
    report = template_agent.generate_report(data, template_id)
    return {"report": report}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}