import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ColumnDropdown = ({ onSelect }) => {
  const [columns, setColumns] = useState([]);

  useEffect(() => {
    // Fetch columns for the hard-coded table name 'aibos_site_article'
    const fetchColumns = async () => {
      try {
        const response = await axios.get('http://3.252.131.54:8000/api/columns/aibos_site_article'); // Replace with actual endpoint
        if (Array.isArray(response.data)) {
          setColumns(response.data);
        } else {
          throw new Error('Data is not an array');
        }
      } catch (error) {
        console.error('Error fetching columns:', error);
      }
    };

    fetchColumns();
  }, []);

  return (
    <div>
      <label>Select Columns:</label>
      <select multiple onChange={(e) => onSelect(Array.from(e.target.selectedOptions, (option) => option.value))}>
        {columns.map((column, index) => (
          <option key={index} value={column}>
            {column}
          </option>
        ))}
      </select>
    </div>
  );
};

export default ColumnDropdown;
