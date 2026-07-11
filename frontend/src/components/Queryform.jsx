function QueryForm({ question, setQuestion, onSubmit }) {
  return (
    <div className="query-box">
      <textarea
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        rows={4}
      />

      <button onClick={onSubmit}>Ask</button>
    </div>
  );
}

export default QueryForm;