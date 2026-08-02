import React from 'react';
import ContactCard from '../ContactCard/ContactCard';
import './Gallery.css';

const Gallery = ({ contacts, onSelectContact }) => {
  return (
    <div className="gallery-container">
      <h2>📇 My Network</h2>
      <div className="gallery-grid">
        {contacts.map(contact => (
          <ContactCard 
            key={contact.id} 
            contact={contact} 
            onSelect={onSelectContact} 
          />
        ))}
      </div>
    </div>
  );
};

export default Gallery;