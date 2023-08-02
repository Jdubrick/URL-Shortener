import React from "react";
import "./ConvertButton.css";
import { sendUserUrlToServer } from "../../api/utils";
import axios from "axios";

const ConvertButton = ({ longUrl, urlAlias, updateShortUrl, wasSuccess }) => {
  const handleClick = (e) => {
    axios
      .post(
        "http://localhost:5000/api/url",
        {
          url: longUrl,
          name: urlAlias,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
      .then((res) => {
        updateShortUrl(res.data.url);
      })
      .catch((e) => console.log(e));
  };

  return (
    <button className="convert-button" onClick={handleClick}>
      Shorten URL
    </button>
  );
};

export default ConvertButton;
