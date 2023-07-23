import React from "react";
import "./InformationCard.css";

const InformationCard = () => {
  return (
    <div className="wrapper">
      <p>
        ShortenMe is a free tool available to shorten lengthy URLs and generate
        a shorter link.
      </p>
      <p>
        Once a link is shortened the short link will remain active for 15 days
        before it expires!
      </p>
    </div>
  );
};

export default InformationCard;
