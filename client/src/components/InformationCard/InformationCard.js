import React from "react";
import "./InformationCard.css";
import "../InformationCard/InformationCard.css";
import "../InputBox/InputBox.css";
const InformationCard = ({ generatedShortUrl }) => {
  return (
    <div className="input-card responsive">
      <div className="content-wrapper">
        <input
          className="input-box"
          placeholder="short url placeholder"
          value={generatedShortUrl}
          readOnly
        />
        <p className="description-text">
          ShortenMe allows for the easy shortening of those long and
          disorganized links that are so common today. Enter your long URL and
          receive your new shortened URL that you can share on all websites!
        </p>
      </div>
    </div>
  );
};

export default InformationCard;
