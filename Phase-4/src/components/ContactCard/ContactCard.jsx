import React from 'react';
import './ContactCard.css';

const ContactCard = ({ contact, onSelect }) => {
  const getStatusColor = (status) => {
    return status === 'Keep in Touch' ? '#4CAF50' : '#FF6B6B';
  };

  return (
    <div className="contact-card" onClick={() => onSelect(contact.id)}>
      <div className="contact-avatar">
        {contact.name.charAt(0)}
      </div>
      <div className="contact-info">
        <h3>{contact.name}</h3>
        <p className="organization">{contact.organization}</p>
        <p className="role">{contact.role}</p>
      </div>
      <div 
        className="status-tag" 
        style={{ backgroundColor: getStatusColor(contact.status) }}
      >
        {contact.status}
      </div>
    </div>
  );
};

export default ContactCard;