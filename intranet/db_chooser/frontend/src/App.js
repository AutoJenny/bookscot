import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import TableDropdown from './components/TableDropdown';
import ColumnDropdown from './components/ColumnDropdown';
import DataDisplayTable from './components/DataDisplayTable';
import ErrorMessage from './components/ErrorMessage';
import LoadingSpinner from './components/LoadingSpinner';

function App() {
  // Define state variables
  const [selectedTable, setSelectedTable] = useState('');
  const [selectedColumns, setSelectedColumns] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Define functions to fetch data
  const fetchColumnsForTable = (tableName) => {
    // Make API call to fetch columns for the selected table
    // Update selectedColumns state
    console.log(`Fetching columns for table: ${tableName}`); // Example of using console for logging
  };

  const fetchDataForTable = (tableName, columns) => {
    // Make API call to fetch data for the selected table and columns
    // Update data state
    console.log(`Fetching data for table: ${tableName} with columns: ${columns.join(', ')}`); // Example of logging
  };

  // useEffect hook to fetch tables when component mounts
  useEffect(() => {
    // Make API call to fetch tables and update state
    console.log("Fetching table list on component mount."); // Example of logging
  }, []);

  // Event handler functions
  const handleTableSelect = (tableName) => {
    setSelectedTable(tableName);
    fetchColumnsForTable(tableName);
  };

  const handleColumnsSelect = (selectedColumns) => {
    setSelectedColumns(selectedColumns);
    fetchDataForTable(selectedTable, selectedColumns);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Database Chooser</h1>
        {/* TableDropdown component */}
        <TableDropdown onSelect={handleTableSelect} />
        {/* ColumnDropdown component */}
        <ColumnDropdown 
          selectedTable={selectedTable} 
          onSelect={handleColumnsSelect} 
        />
        {/* LoadingSpinner component */}
        {loading && <LoadingSpinner />}
        {/* ErrorMessage component */}
        {error && <ErrorMessage message={error} />}
        {/* DataDisplayTable component */}
        <DataDisplayTable data={data} />
      </header>
    </div>
  );
}

export default App;
