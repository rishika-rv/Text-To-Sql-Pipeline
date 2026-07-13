function QueryForm({ question, setQuestion, onSubmit, onUploadDb }) {
  return (
    <div className="query-box">
      <textarea
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        rows={4}
      />

      <input
        type="file"
        accept=".db,.sqlite"
        onChange={(e) => {
          const file = e.target.files?.[0];
          if (file && onUploadDb) {
            onUploadDb(file);
          }
        }}
      />

      <button onClick={onSubmit}>Ask</button>
    </div>
  );
}

export default QueryForm;