# LLM Document Manager
This application enables users to upload company documents and generate relevant metadata. It supports various document formats including PDF, DOC, DOCX, TXT, CSV, and XLS.

## Key Features
1. Instructor Integration: Utilizes the Instructor library to enhance the OpenAI client, ensuring reliability and consistency in the LLM's data structures. 
- For more information, visit: https://jxnl.github.io/instructor/

2. Pydantic Data Models: Leverages Pydantic to define data models, including optional fields and various field validation requirements, ensuring robust and clear data handling.

3. Llama Index Parsing: Employs Llama Index for parsing documents, enabling efficient and effective extraction of information from supported formats.
- For more information, visit: https://www.llamaindex.ai/,  https://llamahub.ai/


## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/duncandevs/llm-document-manager.git
    cd llm-document-manager
    ```

2. **Install the backend dependencies**:
    from root cd into back-end
    ```bash
    cd back-end
    ```

    ```bash
    pip install -r requirements.txt
    ```

    ```bash
    pip install -e .
    ```

3. **Set the OpenAI key**:
    ```bash
    replace OPEN_AI_KEY in back-end .env file with your openai key
    ```

4. **Install the front end dependencies**
    from root cd into front-end

    ```bash
    cd front-end
    ```

    run install command with yarn
    ```bash
    yarn install
    ```

## Starting the App

1. From root Start the pocketbase db instance, run the following command:

    ```bash
    ./pocketbase serve
    ```
    *you may encounter a permission error at this step. If this happens open the root folder and double click the pocketbase exec file to grant permission, then retry this step.*

2. From back-end dir, run the following command:

    ```bash
    start-app
    ```

3. From front-end, run the following command:

    ```bash
    yarn dev
    ```

## Usage:
1. View local app url
    ```bash
    localhost:3000
    ```

2. View local database url
    ```bash
    http://127.0.0.1:8090/_/
    ```

    enter the following DB credentials
    email: tester@example.com
    password: password1234

# Resources: 
- useful materials to continue building on this demo
1. Jason Liu guide to prompt Engineering:
- https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/

2. Instructor For Structured LLMs:
- https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/

3. LLama Index Document Summary Index:
- https://docs.llamaindex.ai/en/stable/examples/index_structs/doc_summary/DocSummary/

4. LLama Index Pydantic Metadata Extractor
- https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/


