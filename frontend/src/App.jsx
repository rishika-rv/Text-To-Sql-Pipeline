import { useState } from "react";
import "./App.css";
import QueryForm from "./components/QueryForm";
import ResultsTable from "./components/ResultsTable";

function App() {
  const [question, setQuestion] = useState("");
  const [generatedSQL, setGeneratedSQL] = useState("");
  const [results, setResults] = useState([]);
  const [uploadMessage, setUploadMessage] = useState("");

  const handleUploadDb = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload-db", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Upload failed");
      }

      setUploadMessage(`Uploaded: ${data.filename}`);
    } catch (error) {
      console.error("Upload error:", error);
      setUploadMessage("Database upload failed.");
    }
  };

  const handleSubmit = async () => {
    if (!question.trim()) return;

    try {
      const response = await fetch("http://127.0.0.1:8000/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      setGeneratedSQL(data.generated_sql);
      setResults(data.results);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="app">
      <h1>Text to SQL Assistant</h1>

      <QueryForm
        question={question}
        setQuestion={setQuestion}
        onSubmit={handleSubmit}
        onUploadDb={handleUploadDb}
      />
      {uploadMessage && <p>{uploadMessage}</p>}
      <ResultsTable generatedSQL={generatedSQL} results={results} />
    </div>
  );
}

export default App;
