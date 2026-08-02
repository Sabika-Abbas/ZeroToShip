import React, { useState } from 'react';
import './DraftBox.css';

const DraftBox = ({ draft }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(draft).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  return (
    <div className="draft-box">
      <div className="draft-header">
        <h4>✍️ AI Draft</h4>
        <button 
          className={`copy-btn ${copied ? 'copied' : ''}`} 
          onClick={handleCopy}
          disabled={!draft || draft === "Select a contact to generate a draft."}
        >
          {copied ? '✅ Copied!' : '📋 Copy'}
        </button>
      </div>
      <div className="draft-content">
        <pre>{draft}</pre>
      </div>
    </div>
  );
};

export default DraftBox;