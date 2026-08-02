import React from 'react';
import './ContactCard.css';

const ContactCard = ({ contact, onSelect }) => {
  const getStatusStyle = (status) => {
    if (status === 'Keep in Touch') {
      return { background: 'linear-gradient(135deg, #11998e, #38ef7d)' };
    }
    return { background: 'linear-gradient(135deg, #f093fb, #f5576c)' };
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
        style={getStatusStyle(contact.status)}
      >
        {contact.status}
      </div>
    </div>
  );
};

export default ContactCard;