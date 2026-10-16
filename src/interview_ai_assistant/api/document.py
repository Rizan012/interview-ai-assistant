
from fastapi import APIRouter,UploadFile, File, HTTPException
from ingest import clean_text, recursive_text_chunk, semantic_text_chunk
from embeddings import generate_embeddings
from qdrant_store import vector_store, client, COLLECTION_NAME
from qdrant_client import models


router = APIRouter()

@router.post("/document")
async def upload_document(file: UploadFile = File(...)):
    filename = file.filename

    if not filename.endswith((".pdf",".txt")):
        raise HTTPException(400, "Please upload .pdf or .txt extention file.")


    try:
        content = await file.read()
        file_content = clean_text(filename,content)

        if not file_content:
            raise HTTPException(400, "File is empty")

        chunks = recursive_text_chunk(file_content)
        chunks = list(dict.fromkeys(chunks))

        vectors = generate_embeddings(chunks)

        client.delete(
            collection_name=COLLECTION_NAME,
            points_selector=models.FilterSelector(
                filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="metadata.source",
                            match=models.MatchValue(value=filename),
                        )
                    ]
                )
            ),
        )

        vector_store.add_texts(
                texts=chunks,
                metadatas=[
                    {"source": filename, "chunk_index": i}
                    for i in range(len(chunks))
                ],
        )

        return {"message": "Upload successful", "vectors": len(chunks)}


    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(400,f"Failed :( error: {error}")

    finally:
        await file.close()
