function ResultsTable({ generatedSQL, results }) {
  const columns = results.length > 0 ? Object.keys(results[0]) : [];

  return (
    <div className="response-section">
      <h2>Generated SQL</h2>
      <pre>{generatedSQL || "Your generated SQL will appear here."}</pre>

      <h2>Results</h2>

      {results.length === 0 ? (
        <div className="table-placeholder">
          Query results will appear here.
        </div>
      ) : (
        <table>
          <thead>
            <tr>
              {columns.map((column) => (
                <th key={column}>{column}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {results.map((row, index) => (
              <tr key={index}>
                {columns.map((column) => (
                  <td key={column}>{String(row[column])}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ResultsTable;