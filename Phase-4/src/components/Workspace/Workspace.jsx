import React from 'react';
import DraftBox from '../DraftBox/DraftBox';
import './Workspace.css';

const Workspace = ({ contact, draft }) => {
  if (!contact) {
    return (
      <div className="workspace-container">
        <div className="empty-state">
          <h3>👈 Select a contact to view details</h3>
          <p>Click on any contact card to see their interaction history and AI-generated draft.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="workspace-container">
      <div className="workspace-header">
        <h2>{contact.name}</h2>
        <p className="workspace-subtitle">{contact.role} at {contact.organization}</p>
        <div className="workspace-meta">
          <span>📧 {contact.email}</span>
          <span>🔗 {contact.linkedin}</span>
        </div>
      </div>

      <div className="workspace-split">
        <div className="notes-panel">
          <h4>📝 Interaction History</h4>
          <div className="notes-list">
            {contact.notes && contact.notes.length > 0 ? (
              contact.notes.map((note, index) => (
                <div key={index} className="note-item">
                  <div className="note-date">{note.date}</div>
                  <div className="note-text">{note.text}</div>
                </div>
              ))
            ) : (
              <p className="no-notes">No notes yet.</p>
            )}
          </div>
        </div>

        <div className="draft-panel">
          <DraftBox draft={draft} />
        </div>
      </div>
    </div>
  );
};

export default Workspace;