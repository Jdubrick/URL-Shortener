import React, { useState } from "react";
import "./InputCard.css";
import InputBox from "../InputBox/InputBox";
import ConvertButton from "../ConvertButton/ConvertButton";

const InputCard = ({ setGeneratedShortUrl }) => {
  const [userLongUrl, setUserLongUrl] = useState("");
  const [userUrlAlias, setUserUrlAlias] = useState("");

  const handleUserUrlAliasChange = (e) => {
    setUserUrlAlias(e.target.value);
  };

  const handleUserLongUrlChange = (e) => {
    setUserLongUrl(e.target.value);
  };

  const handleShortUrlChange = (e) => {
    setGeneratedShortUrl(e);
  };

  return (
    <div className="input-card responsive">
      <div className="card-wrapper">
        <div className="input-wrapper">
          <InputBox
            placeholderText={"Enter long URL here"}
            readOnly={false}
            updateFunction={handleUserLongUrlChange}
            inputValue={userLongUrl}
          />
          <div className="hostname-alias-input">
            <input
              className="hostname alias-box"
              type="text"
              placeholder="localhost:3000/"
              readOnly
            />
            <input
              className="alias alias-box"
              type="text"
              placeholder="Alias"
              value={userUrlAlias}
              onChange={(e) => handleUserUrlAliasChange(e)}
            />
          </div>
        </div>
        <div className="button-wrapper">
          <ConvertButton
            longUrl={userLongUrl}
            urlAlias={userUrlAlias}
            updateShortUrl={(e) => handleShortUrlChange(e)}
          />
        </div>
      </div>
    </div>
  );
};

export default InputCard;

// {success && (
//   // <div className="shortened-url">
//   //   {/* <InputBox
//   //     placeholderText={"Copy short URL here"}
//   //     readOnly={true}
//   //     value={generatedShortUrl}
//   //   /> */}
//   //   {generatedShortUrl} //TODO: fix this up so it doesnt look just like
//   //   text
//   // </div>
// )}
