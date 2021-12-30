import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [pingResponse, setPingResponse] = useState('no pong');

  useEffect(() => {
    fetch('/ping').then(res => res.json()).then(data => {
      setPingResponse(data.ping);
    });
  }, []);

  return (
    <div className='App'>
      <header className='App-header'>
        <p>The current PING is {pingResponse}.</p>
      </header>
    </div>
  );
}

export default App;