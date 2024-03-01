import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TableDropdown = ({ onSelect }) => {
  const [tables, setTables] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    // Fetch tables from backend when component mounts
    const fetchTables = async () => {
      try {
        const response = await axios.get('http://3.252.131.54:8000/api/tables-list/');
        if (response.data && typeof response.data === 'object') {
          // If the response is an object, assume it has a 'tables' property containing the array
          const tablesArray = response.data.tables;
          if (Array.isArray(tablesArray)) {
            setTables(tablesArray);
          } else {
            throw new Error('Data tables is not an array');
          }
        } else {
          throw new Error('Response data is not an object');
        }
      } catch (error) {
        setError(error.message);
        console.error('Error fetching tables:', error);
      }
    };
  
    fetchTables();
  }, []);
  

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <label>Select Table:</label>
      <select onChange={(e) => onSelect(e.target.value)}>
        <option value="">Select a table</option>
        {tables.map((table, index) => (
          <option key={index} value={table}>
            {table}
          </option>
        ))}
      </select>
    </div>
  );
};

export default TableDropdown;
