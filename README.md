# Langchain basics 

This is a basic application that runs an LLM application using Langchain and Langserve. 

## Requirements 

You need to have:

* Mistral Account to get a Mistral API Key
* Docker installed

## Run the application 

To run the application simply:

```bash
docker run -p 7860:7680 -e MISTRAL_API_KEY=REPLACE_WITH_YOUR_MISTRAL_API_KEY jedha/langchain-base
```
And then open web browser and go to:

* http://localhost:7860/chain/playground 

This endpoint will prompt you to a web page to test the `/chain` endpoint.
