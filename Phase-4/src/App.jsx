import React, { useState } from 'react';
import { contacts, getAIDraft } from './data/mockData';
import Gallery from './components/Gallery/Gallery';
import Workspace from './components/Workspace/Workspace';
import './App.css';

function App() {
  const [selectedContact, setSelectedContact] = useState(null);
  const [draft, setDraft] = useState('Select a contact to generate a draft.');

  const handleSelectContact = (contactId) => {
    const contact = contacts.find(c => c.id === contactId);
    setSelectedContact(contact);
    if (contact) {
      setDraft(getAIDraft(contactId));
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>🤝 Smart Personal CRM</h1>
        <p>Manage your professional network</p>
      </header>
      
      <div className="app-body">
        <div className="gallery-section">
          <Gallery contacts={contacts} onSelectContact={handleSelectContact} />
        </div>
        <div className="workspace-section">
          <Workspace contact={selectedContact} draft={draft} />
        </div>
      </div>
    </div>
  );
}

export default App;