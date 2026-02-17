class DocumentReaderTool:
    name = "read_document"
    description = "Reads a text document from disk"

    def run(self, input_data):
        path = input_data["path"]
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
