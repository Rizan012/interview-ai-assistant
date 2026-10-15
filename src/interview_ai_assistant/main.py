from fastapi import FastAPI, UploadFile, File, HTTPException
from ingest import clean_text, recursive_text_chunk, semantic_text_chunk
from embeddings import generate_embeddings

app = FastAPI()

@app.post("/document")
async def upload_document(file: UploadFile = File(...)):
    filename = file.filename

    if not filename.endswith((".pdf",".txt")):
        raise HTTPException(400, "Please upload .pdf or .txt extention file.")

    
    try:
        content = await file.read()
        file_content = clean_text(filename,content)
        chunks = semantic_text_chunk(file_content)
        print(chunks)
        vectors = generate_embeddings(chunks)

        return {"vectors":vectors}


        if not file_content:
            raise HTTPException(400, "File is empty")
        
    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(400,f"Failed :( error: {error}")

    finally:
        await file.close()