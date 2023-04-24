import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileSelect = (event) => {
    setSelectedFile(event.target.files[0]);
  }

  function handleUpload(event) {
    event.preventDefault();
    const formData = new FormData();
    formData.append('image', selectedFile);
    axios.post('http://127.0.0.1:5000 ', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.log(error);
    });
  }

  return (
    <div style={{ backgroundColor: '#0070C9', height: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <form onSubmit={handleUpload} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', backgroundColor: '#FFF', padding: '20px', borderRadius: '10px', boxShadow: '0px 0px 5px 0px rgba(0,0,0,0.75)' }}>
        <input type="file" onChange={handleFileSelect} style={{ marginBottom: '20px' }} />
        {selectedFile && <p style={{marginBottom: '20px'}}>Archivo seleccionado: {selectedFile.name}</p>}
        <button type="submit" style={{ backgroundColor: '#FF2800', color: '#FFF', padding: '10px 20px', borderRadius: '5px', fontSize: '1.2rem', fontWeight: 'bold', border: 'none' }}>Enviar archivo</button>
      </form>
    </div>
  );
}

export default App;